"""Bounded, duplicate-rejecting input; paths cannot escape the supplied input root."""

from __future__ import annotations

import hashlib
import json
import math
import os
import stat
from pathlib import Path
from typing import Any

MAX_BYTES = 2 * 1024 * 1024
MAX_NODES = 100_000
MAX_DEPTH = 40


class InputError(ValueError):
    def __init__(self, code: str, location: str = ""):
        self.code, self.location = code, location
        super().__init__(code)


def read_regular(path: Path) -> bytes:
    """Reject symlinks/non-regular files before reading, and bound the actual read."""
    try:
        if path.is_symlink():
            raise InputError("unsafe_file", str(path))
        fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0))
        with os.fdopen(fd, "rb") as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode):
                raise InputError("unsafe_file", str(path))
            if info.st_size > MAX_BYTES:
                raise InputError("size_limit", str(path))
            content = stream.read(MAX_BYTES + 1)
            if len(content) > MAX_BYTES:
                raise InputError("size_limit", str(path))
            return content
    except OSError as exc:
        raise InputError("read_failed", str(path)) from exc


def fingerprint(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def parse_json(content: bytes, location: str = "") -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise InputError("duplicate_key", location)
            result[key] = value
        return result

    def reject_constant(_):
        raise InputError("invalid_json", location)

    try:
        value = json.loads(
            content.decode("utf-8"), object_pairs_hook=pairs, parse_constant=reject_constant
        )
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError, ValueError) as exc:
        if isinstance(exc, InputError):
            raise
        raise InputError("invalid_json", location) from exc
    nodes = 0
    pending = [(value, 0)]
    while pending:
        node, depth = pending.pop()
        nodes += 1
        if depth > MAX_DEPTH or nodes > MAX_NODES:
            raise InputError("structure_limit", location)
        if isinstance(node, float) and not math.isfinite(node):
            raise InputError("invalid_json", location)
        children = (
            node.values() if isinstance(node, dict) else node if isinstance(node, list) else []
        )
        pending.extend((child, depth + 1) for child in children)
    return value


def source_path(root: Path, name: str) -> Path:
    if not isinstance(name, str) or not name or "\\" in name:
        raise InputError("unsafe_path")
    relative = Path(name)
    if relative.is_absolute() or any(part in ("..", ".") for part in name.split("/")):
        raise InputError("unsafe_path", name)
    candidate = root / relative
    for path in [candidate, *candidate.parents]:
        if path == root.parent:
            break
        if path.is_symlink():
            raise InputError("unsafe_path", name)
    try:
        candidate.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise InputError("unsafe_path", name) from exc
    return candidate


def escape(token: str) -> str:
    return token.replace("~", "~0").replace("/", "~1")


def resolve(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise InputError("invalid_pointer", str(pointer))
    current = document
    try:
        for raw in pointer[1:].split("/"):
            # Only the two escapes defined by RFC 6901 are accepted.
            import re

            if re.search(r"~(?![01])", raw):
                raise InputError("invalid_pointer", pointer)
            token = raw.replace("~1", "/").replace("~0", "~")
            if isinstance(current, list):
                if not token.isdecimal() or (token.startswith("0") and token != "0"):
                    raise InputError("invalid_pointer", pointer)
                current = current[int(token)]
            elif isinstance(current, dict):
                current = current[token]
            else:
                raise InputError("invalid_pointer", pointer)
        return current
    except (KeyError, IndexError, ValueError) as exc:
        if isinstance(exc, InputError):
            raise
        raise InputError("invalid_pointer", pointer) from exc
