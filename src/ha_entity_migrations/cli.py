from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .i18n import LANGUAGES, tr
from .io import InputError, fingerprint, read_regular
from .planner import load_plan


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    lang = "en"
    for index, value in enumerate(argv):
        if value == "--lang" and index + 1 < len(argv) and argv[index + 1] in LANGUAGES:
            lang = argv[index + 1]
        elif value.startswith("--lang=") and value.split("=", 1)[1] in LANGUAGES:
            lang = value.split("=", 1)[1]

    class Parser(argparse.ArgumentParser):
        def error(self, message):
            self.print_usage(sys.stderr)
            self.exit(2, tr(lang, "arguments") + "\n")

    def add_help(parser):
        parser.add_argument("-h", "--help", action="help", help=tr(lang, "help"))

    parser = Parser(description=tr(lang, "description"), add_help=False)
    add_help(parser)
    parser.add_argument("--lang", choices=LANGUAGES, default=lang, help=tr(lang, "language"))
    parser.add_argument(
        "--version", action="version", version=__version__, help=tr(lang, "version_help")
    )
    sub = parser.add_subparsers(dest="command", required=True)
    command = sub.add_parser("plan", help=tr(lang, "plan_help"), add_help=False)
    add_help(command)
    command.add_argument("--manifest", type=Path, required=True, help=tr(lang, "manifest_help"))
    command.add_argument("--snapshot", type=Path, required=True, help=tr(lang, "snapshot_help"))
    command.add_argument("--root", type=Path, required=True, help=tr(lang, "root_help"))
    command.add_argument(
        "--format", choices=("json", "text"), default="json", help=tr(lang, "format_help")
    )
    fp = sub.add_parser("fingerprint", help=tr(lang, "fingerprint_help"), add_help=False)
    add_help(fp)
    fp.add_argument("file", type=Path, help=tr(lang, "fingerprint_help"))
    args = parser.parse_args(argv)
    try:
        if args.command == "fingerprint":
            print(fingerprint(read_regular(args.file)))
            return 0
        report = load_plan(args.manifest, args.snapshot, args.root)
        for diagnostic in report["diagnostics"]:
            diagnostic["message"] = tr(lang, diagnostic["code"])
        report["language"] = lang
        report["summary"] = tr(lang, report["status"])
        if args.format == "json":
            print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
        else:
            print(report["summary"])
            print(f"{tr(lang, 'edits')}: {len(report['edits'])}")
            for edit in report["edits"]:
                print(json.dumps(edit, ensure_ascii=False, sort_keys=True))
            for item in report["diagnostics"]:
                print(f"{item['code']} {item['location']}: {item['message']}")
        return 0 if report["status"] == "ready" else 3
    except InputError as exc:
        print(
            json.dumps(
                {
                    "schema_version": 1,
                    "status": "invalid",
                    "read_only": True,
                    "language": lang,
                    "diagnostics": [
                        {"code": exc.code, "location": exc.location, "message": tr(lang, exc.code)}
                    ],
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
