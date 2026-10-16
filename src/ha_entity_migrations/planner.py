"""Pure planner. Values are declarations, never inferred hardware evidence."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .io import InputError, escape, fingerprint, parse_json, read_regular, resolve, source_path

ENTITY = re.compile(r"[a-z][a-z0-9_]*\.[a-z0-9_]+\Z")
MENTION = re.compile(r"(?<![\w.])[a-z][a-z0-9_]*\.[a-z0-9_]+(?![\w.])")
SHA = re.compile(r"[a-f0-9]{64}\Z")
POLICIES = {"follows_role", "follows_hardware", "retire"}
MAX_ITEMS = 5000
MAX_FILES = 64


def schema(ok: bool, where: str) -> None:
    if not ok:
        raise InputError("schema_invalid", where)


def fields(value: Any, required: set[str], optional: set[str], where: str) -> None:
    schema(isinstance(value, dict), where)
    schema(required <= value.keys() and value.keys() <= required | optional, where)


def text(value: Any) -> bool:
    return isinstance(value, str) and 0 < len(value) <= 256 and not any(ord(c) < 32 for c in value)


def strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) <= 64
        and all(text(item) for item in value)
        and len(set(value)) == len(value)
    )


def endpoint(entity: dict) -> tuple[str, str]:
    return entity["hardware_id"], entity["channel"]


def validate_entity(entity: Any, where: str) -> None:
    fields(entity, {"entity_id", "hardware_id", "channel", "role", "capabilities"}, set(), where)
    schema(text(entity["entity_id"]) and bool(ENTITY.fullmatch(entity["entity_id"])), where)
    schema(all(text(entity[key]) for key in ["hardware_id", "channel", "role"]), where)
    schema(strings(entity["capabilities"]), where)


def walk(document: Any, pointer: str = ""):
    if isinstance(document, dict):
        for key, value in sorted(document.items()):
            path = pointer + "/" + escape(key)
            if any(token in key for token in ("{{", "{%", "{#")):
                yield "dynamic_reference", path, ""
            elif MENTION.search(key):
                yield "embedded_reference", path, ""
            if key in {"device_id", "area_id", "label_id"}:
                yield "indirect_target", path, ""
            if isinstance(value, str) and key in {"action", "service"}:
                if any(token in value for token in ("{{", "{%", "{#")):
                    yield "dynamic_reference", path, ""
                elif (
                    value.startswith("script.")
                    and ENTITY.fullmatch(value)
                    and value
                    not in {"script.turn_on", "script.turn_off", "script.toggle", "script.reload"}
                ):
                    # Direct script calls are both service names and entity references.
                    yield "reference", path, value
                # Standard service identifiers are not entity references.
                continue
            yield from walk(value, path)
    elif isinstance(document, list):
        for index, value in enumerate(document):
            yield from walk(value, pointer + "/" + str(index))
    elif isinstance(document, str):
        if any(token in document for token in ("{{", "{%", "{#")):
            yield "dynamic_reference", pointer, ""
        elif ENTITY.fullmatch(document):
            yield "reference", pointer, document
        elif MENTION.search(document):
            yield "embedded_reference", pointer, ""


def plan(
    manifest: dict, snapshot: dict, sources: dict[str, tuple[bytes, Any]], snapshot_hash: str
) -> dict:
    """Return a deterministic report; never mutate any input document."""
    fields(
        manifest,
        {"version", "snapshot_sha256", "sources", "assignments", "consumers"},
        set(),
        "manifest",
    )
    schema(type(manifest["version"]) is int and manifest["version"] == 1, "manifest.version")
    schema(
        isinstance(manifest["snapshot_sha256"], str)
        and bool(SHA.fullmatch(manifest["snapshot_sha256"])),
        "manifest.snapshot_sha256",
    )
    schema(
        isinstance(manifest["sources"], dict) and 0 < len(manifest["sources"]) <= MAX_FILES,
        "manifest.sources",
    )
    for name, digest in manifest["sources"].items():
        schema(
            text(name) and isinstance(digest, str) and bool(SHA.fullmatch(digest)),
            "manifest.sources",
        )
    for key in ["assignments", "consumers"]:
        schema(
            isinstance(manifest[key], list) and len(manifest[key]) <= MAX_ITEMS, "manifest." + key
        )
    fields(snapshot, {"version", "entities"}, set(), "snapshot")
    schema(type(snapshot["version"]) is int and snapshot["version"] == 1, "snapshot.version")
    schema(
        isinstance(snapshot["entities"], list) and 0 < len(snapshot["entities"]) <= MAX_ITEMS,
        "snapshot.entities",
    )

    diagnostics: list[dict] = []
    edits: list[dict] = []

    def issue(code: str, location: str, severity: str = "error"):
        diagnostics.append({"code": code, "location": location, "severity": severity})

    if snapshot_hash != manifest["snapshot_sha256"]:
        issue("stale_snapshot", "snapshot")
    schema(set(sources) == set(manifest["sources"]), "sources")
    for name, (raw, _) in sorted(sources.items()):
        if fingerprint(raw) != manifest["sources"][name]:
            issue("stale_source", name)

    before = {}
    by_endpoint = {}
    roles = set()
    for index, entity in enumerate(snapshot["entities"]):
        validate_entity(entity, f"snapshot.entities/{index}")
        if (
            entity["entity_id"] in before
            or endpoint(entity) in by_endpoint
            or entity["role"] in roles
        ):
            issue("source_collision", f"snapshot.entities/{index}")
        before[entity["entity_id"]] = entity
        by_endpoint[endpoint(entity)] = entity
        roles.add(entity["role"])

    after = dict(by_endpoint)
    assigned = set()
    for index, entity in enumerate(manifest["assignments"]):
        validate_entity(entity, f"manifest.assignments/{index}")
        key = endpoint(entity)
        if key not in by_endpoint:
            issue("unknown_hardware", f"manifest.assignments/{index}")
        if key in assigned:
            issue("assignment_collision", f"manifest.assignments/{index}")
        assigned.add(key)
        after[key] = entity
    ids, after_roles = set(), {}
    for key, entity in sorted(after.items()):
        if entity["entity_id"] in ids or entity["role"] in after_roles:
            issue("destination_collision", entity["entity_id"])
        ids.add(entity["entity_id"])
        after_roles[entity["role"]] = entity

    policies = {}
    retire_scopes: dict[str, list[str]] = {}
    for index, consumer in enumerate(manifest["consumers"]):
        where = f"manifest.consumers/{index}"
        fields(
            consumer,
            {"file", "pointer", "policy"},
            {"kind", "allowed_roles", "required_capabilities", "service_pointer", "retire_scope"},
            where,
        )
        schema(
            text(consumer["file"]) and consumer["file"] in sources and text(consumer["pointer"]),
            where,
        )
        schema(isinstance(consumer["policy"], str) and consumer["policy"] in POLICIES, where)
        key = consumer["file"], consumer["pointer"]
        if key in policies:
            issue("consumer_collision", where)
        policies[key] = consumer
        doc = sources[key[0]][1]
        if doc is None:
            issue("unsupported_source", key[0], "unresolved")
            continue
        value = resolve(doc, key[1])
        schema(isinstance(value, str) and bool(ENTITY.fullmatch(value)), where + ".pointer")
        if value not in before:
            issue("unmodeled_reference", key[0] + "#" + key[1], "unresolved")
            continue
        if consumer["policy"] == "retire":
            schema(set(consumer) == {"file", "pointer", "policy", "retire_scope"}, where)
            scope = consumer["retire_scope"]
            schema(text(scope) and key[1].startswith(scope + "/"), where + ".retire_scope")
            retired = resolve(doc, scope)
            schema(isinstance(retired, dict), where + ".retire_scope")
            refs = list(walk(retired))
            if any(kind != "reference" or ref != value for kind, _, ref in refs):
                issue("retire_scope_mixed", key[0] + "#" + scope)
                continue
            retire_scopes.setdefault(key[0], []).append(scope)
            edits.append(
                {
                    "operation": "remove_consumer",
                    "file": key[0],
                    "pointer": scope,
                    "reference": value,
                }
            )
            continue
        schema("retire_scope" not in consumer, where)
        schema(
            isinstance(consumer.get("kind"), str)
            and consumer["kind"] in {"action", "display", "reference"},
            where + ".kind",
        )
        schema(
            strings(consumer.get("allowed_roles")) and len(consumer["allowed_roles"]) > 0,
            where + ".allowed_roles",
        )
        schema(strings(consumer.get("required_capabilities")), where + ".required_capabilities")
        if consumer["kind"] == "action":
            schema(text(consumer.get("service_pointer")), where + ".service_pointer")
            resolve(doc, consumer["service_pointer"])
        else:
            schema("service_pointer" not in consumer, where)

    # No candidate edits on conflicting/stale snapshots. This avoids plausible but invalid plans.
    fatal_model = bool(diagnostics)
    seen = set()
    for name, (_, doc) in sorted(sources.items()):
        if doc is None:
            issue("unsupported_source", name, "unresolved")
            continue
        for kind, pointer, value in walk(doc):
            location = name + "#" + pointer
            if any(
                pointer == scope or pointer.startswith(scope + "/")
                for scope in retire_scopes.get(name, [])
            ):
                continue
            if kind != "reference":
                issue(kind, location, "unresolved")
                continue
            seen.add((name, pointer))
            if value not in before:
                issue("unmodeled_reference", location, "unresolved")
                continue
            consumer = policies.get((name, pointer))
            if consumer is None:
                issue("missing_policy", location, "unresolved")
                continue
            if fatal_model or consumer["policy"] == "retire":
                continue
            old = before[value]
            target = (
                after_roles.get(old["role"])
                if consumer["policy"] == "follows_role"
                else after[endpoint(old)]
            )
            if target is None:
                issue("role_retired", location)
                continue
            if target["role"] not in consumer["allowed_roles"]:
                issue("role_not_allowed", location)
                continue
            if not set(consumer["required_capabilities"]) <= set(target["capabilities"]):
                issue("capability_missing", location)
                continue
            old_domain, new_domain = (
                old["entity_id"].split(".")[0],
                target["entity_id"].split(".")[0],
            )
            if old_domain != new_domain:
                if consumer["kind"] == "display":
                    issue("display_domain_review", location, "unresolved")
                elif consumer["kind"] == "action":
                    service_path = consumer["service_pointer"]
                    service = resolve(doc, service_path)
                    parent_path = service_path.rsplit("/", 1)[0]
                    action = resolve(doc, parent_path)
                    if not isinstance(action, dict) or not isinstance(service, str):
                        issue("service_domain_review", location, "unresolved")
                    elif (
                        not pointer.startswith(parent_path + "/target/entity_id")
                        and pointer != parent_path + "/entity_id"
                    ):
                        issue("service_scope_mismatch", location)
                    elif action.get("data") or action.get("data_template"):
                        issue("service_data_review", location, "unresolved")
                    elif service not in {
                        old_domain + "." + verb for verb in ["turn_on", "turn_off", "toggle"]
                    } | {
                        "homeassistant.turn_on",
                        "homeassistant.turn_off",
                        "homeassistant.toggle",
                    } or {old_domain, new_domain} != {"light", "switch"}:
                        issue("service_domain_review", location, "unresolved")
                    elif service.startswith(old_domain + "."):
                        # A shared service may target other entities; all must have the same planned domain.
                        action_refs = [
                            v
                            for k, _, v in walk(
                                action.get("target", {"entity_id": action.get("entity_id")})
                            )
                            if k == "reference"
                        ]
                        if action_refs != [value]:
                            issue("mixed_action_targets", location, "unresolved")
                        else:
                            edits.append(
                                {
                                    "operation": "replace_service",
                                    "file": name,
                                    "pointer": service_path,
                                    "before": service,
                                    "after": new_domain + "." + service.split(".")[1],
                                }
                            )
            if value != target["entity_id"]:
                edits.append(
                    {
                        "operation": "replace_reference",
                        "file": name,
                        "pointer": pointer,
                        "before": value,
                        "after": target["entity_id"],
                        "policy": consumer["policy"],
                    }
                )
    # Retire policies were accounted for as whole containers above.
    for (name, pointer), consumer in policies.items():
        if consumer["policy"] != "retire" and (name, pointer) not in seen:
            issue("unused_policy", name + "#" + pointer)

    if fatal_model:
        edits = []
    # Reject overlapping edits rather than suggesting an ambiguous order of operations.
    touched: set[tuple[str, str]] = set()
    for edit in sorted(edits, key=lambda item: (item["file"], item["pointer"])):
        parts = edit["pointer"].split("/")
        if any((edit["file"], "/".join(parts[:i])) in touched for i in range(1, len(parts) + 1)):
            issue("overlapping_edits", edit["file"] + "#" + edit["pointer"])
        touched.add((edit["file"], edit["pointer"]))
    unique_issues = {tuple(sorted(item.items())): item for item in diagnostics}
    diagnostics = sorted(unique_issues.values(), key=lambda item: (item["location"], item["code"]))
    return {
        "schema_version": 1,
        "tool_version": "0.1.0",
        "status": "blocked" if diagnostics else "ready",
        "read_only": True,
        "scope": "supplied_files_only",
        "snapshot_sha256": snapshot_hash,
        "source_sha256": {name: fingerprint(raw) for name, (raw, _) in sorted(sources.items())},
        "assignments": sorted(manifest["assignments"], key=lambda value: endpoint(value)),
        "edits": sorted(edits, key=lambda item: (item["file"], item["pointer"], item["operation"])),
        "diagnostics": diagnostics,
    }


def load_plan(manifest_path: Path, snapshot_path: Path, root: Path) -> dict:
    manifest = parse_json(read_regular(manifest_path), "manifest")
    snapshot_raw = read_regular(snapshot_path)
    snapshot = parse_json(snapshot_raw, "snapshot")
    schema(
        isinstance(manifest, dict) and isinstance(manifest.get("sources"), dict), "manifest.sources"
    )
    schema(0 < len(manifest["sources"]) <= MAX_FILES, "manifest.sources")
    sources = {}
    total = 0
    for name in sorted(manifest["sources"]):
        path = source_path(root, name)
        raw = read_regular(path)
        total += len(raw)
        if total > 16 * 1024 * 1024:
            raise InputError("size_limit", "sources")
        if path.suffix.lower() == ".json":
            document = parse_json(raw, name)
        else:
            # Raw YAML/Jinja/storage is deliberately not executed or permissively parsed.
            document = None
        sources[name] = (raw, document)
    return plan(manifest, snapshot, sources, fingerprint(snapshot_raw))
