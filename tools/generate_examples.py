"""Generate deterministic synthetic inputs. Does not read a home inventory."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "examples"


def entity(identifier, hardware, role, caps=None):
    return {
        "entity_id": identifier,
        "hardware_id": hardware,
        "channel": "1",
        "role": role,
        "capabilities": caps or ["on_off"],
    }


def write(name, entities, assignments, config, consumers):
    folder = ROOT / name
    folder.mkdir(exist_ok=True)
    hashes = {}
    for filename, doc in [
        ("snapshot.json", {"version": 1, "entities": entities}),
        ("automations.json", config),
    ]:
        raw = (json.dumps(doc, ensure_ascii=False, indent=2) + "\n").encode()
        (folder / filename).write_bytes(raw)
        hashes[filename] = hashlib.sha256(raw).hexdigest()
    manifest = {
        "version": 1,
        "snapshot_sha256": hashes["snapshot.json"],
        "sources": {"automations.json": hashes["automations.json"]},
        "assignments": assignments,
        "consumers": consumers,
    }
    (folder / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main():
    write(
        "role-swap",
        [
            entity("light.workbench", "plug-a", "workbench"),
            entity("switch.spare", "plug-b", "spare"),
        ],
        [
            entity("switch.pump_enable", "plug-a", "pump_enable"),
            entity("light.workbench", "plug-b", "workbench"),
        ],
        [
            {
                "alias": "Synthetic lights off",
                "actions": [
                    {"action": "light.turn_off", "target": {"entity_id": "light.workbench"}}
                ],
            },
            {
                "alias": "Retired spare example",
                "actions": [{"action": "switch.turn_off", "target": {"entity_id": "switch.spare"}}],
            },
        ],
        [
            {
                "file": "automations.json",
                "pointer": "/0/actions/0/target/entity_id",
                "policy": "follows_role",
                "kind": "action",
                "allowed_roles": ["workbench"],
                "required_capabilities": ["on_off"],
                "service_pointer": "/0/actions/0/action",
            },
            {
                "file": "automations.json",
                "pointer": "/1/actions/0/target/entity_id",
                "policy": "retire",
                "retire_scope": "/1",
            },
        ],
    )
    write(
        "domain-change",
        [entity("light.table", "plug-c", "table")],
        [entity("switch.table", "plug-c", "table")],
        [{"actions": [{"action": "light.turn_off", "target": {"entity_id": "light.table"}}]}],
        [
            {
                "file": "automations.json",
                "pointer": "/0/actions/0/target/entity_id",
                "policy": "follows_hardware",
                "kind": "action",
                "allowed_roles": ["table"],
                "required_capabilities": ["on_off"],
                "service_pointer": "/0/actions/0/action",
            }
        ],
    )
    write(
        "blocked-template",
        [entity("light.table", "plug-c", "table")],
        [entity("switch.table", "plug-c", "table")],
        [
            {
                "actions": [
                    {
                        "action": "light.turn_off",
                        "target": {"entity_id": "{{ states('input_text.selected_light') }}"},
                    }
                ]
            }
        ],
        [],
    )


if __name__ == "__main__":
    main()
