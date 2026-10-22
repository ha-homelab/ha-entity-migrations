#!/usr/bin/env python3
"""Check documentation languages, relative links and original SVG syntax."""

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path, PurePosixPath
from urllib.parse import unquote
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parents[1]
paths = [
    root / p
    for p in subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    if p
]
errors = []
for name in (
    "README.md",
    "README.ru.md",
    "README.de.md",
    "README.es.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "wiki/Home.md",
    "wiki/_Sidebar.md",
):
    if not (root / name).is_file():
        errors.append("Missing " + name)
for path in paths:
    if path.suffix == ".svg":
        try:
            ET.parse(path)
        except ET.ParseError:
            errors.append("Invalid SVG " + str(path.relative_to(root)))
    if path.suffix != ".md":
        continue
    body = path.read_text(encoding="utf-8")
    links = re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', body)
    links += re.findall(r'href="([^"]+)"', body)
    for link in links:
        if link.startswith(("http:", "https:", "mailto:", "#")):
            continue
        dest = unquote(link.split("#")[0]).strip("<>")
        if not dest:
            continue
        target = path.parent / dest
        if "wiki" in path.relative_to(root).parts and not target.suffix:
            target = target.with_suffix(".md")
        if not target.exists():
            errors.append(str(path.relative_to(root)) + ": broken relative link " + dest)
# Full guide families are deliberately separate from the existing CLI/README locales.
NAV = re.compile(
    r"\n*<!-- language-navigation:start -->.*?<!-- language-navigation:end -->\n*", re.S
)
FENCE = re.compile(r"^```[^\n]*\n.*?^```", re.M | re.S)
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
EXPECTED = set(
    "en ar bn cs de es fa fr he hi id it ja ko nl pl pt ru th tr uk vi zh-Hans zh-Hant".split()
)


def content(text):
    return NAV.sub("\n\n", text).strip()


def localized(source, code):
    if source.parent == root / "docs/en":
        return root / "docs" / code / source.name
    return source.with_name(source.stem + ("" if code == "en" else "-" + code) + ".md")


def navigation_target(source, code):
    if source.parent == root / "docs/en":
        return (PurePosixPath("..") / code / source.name).as_posix()
    return localized(source, code).name


def translated_link(link, source, code):
    """Preserve external references and localize complete documentation families."""
    if code == "en" or "#" in link or "?" in link:
        return link
    docs_prefix = "https://github.com/ha-homelab/ha-entity-migrations/blob/main/docs/en/"
    if link.startswith(docs_prefix):
        return docs_prefix.replace("/en/", "/" + code + "/") + link[len(docs_prefix) :]
    wiki_prefix = "https://github.com/ha-homelab/ha-entity-migrations/wiki/"
    if link.startswith(wiki_prefix) and link[len(wiki_prefix) :] in {
        "Home",
        "Installation",
        "Model",
        "Troubleshooting",
    }:
        return link + "-" + code
    # Relative links inside docs/<language>/ already select that language.
    return link


def structure(text):
    prose = FENCE.sub("", text)
    return (
        re.findall(r"^(#{1,6}) ", prose, re.M),
        len(re.findall(r"^\s*[-*] ", prose, re.M)),
        len(re.findall(r"^\s*\d+\. ", prose, re.M)),
    )


manifest = json.loads((root / "docs/translations.json").read_text(encoding="utf-8"))
catalog = json.loads((root / manifest["languages"]).read_text(encoding="utf-8"))
codes = [item["code"] for item in catalog]
if len(codes) != 24 or set(codes) != EXPECTED:
    errors.append("Documentation catalog must contain each of the 24 reference languages once")
if manifest.get("version") != 1 or len(manifest["families"]) != 10:
    errors.append("Invalid guide translation manifest")
for item in catalog:
    expected_direction = "rtl" if item["code"] in {"ar", "fa", "he"} else "ltr"
    if item.get("dir", "ltr") != expected_direction or not item.get("label"):
        errors.append("Invalid language direction or label: " + item["code"])
for family in manifest["families"]:
    source = root / family["source"]
    if not source.is_file():
        errors.append("Missing source: " + family["source"])
        continue
    original = content(source.read_text(encoding="utf-8"))
    if hashlib.sha256(original.encode()).hexdigest() != family["source_sha256"]:
        errors.append(
            f"{family['source']}: English changed; review all translations and update digest"
        )
    for item in catalog:
        code = item["code"]
        target = localized(source, code)
        if not target.is_file():
            errors.append("Missing translation: " + str(target.relative_to(root)))
            continue
        text = target.read_text(encoding="utf-8")
        name = str(target.relative_to(root))
        navs = NAV.findall(text)
        expected_links = [
            '<a href="'
            + navigation_target(source, other["code"])
            + '" lang="'
            + other["code"]
            + '" dir="'
            + other.get("dir", "ltr")
            + '">'
            + other["label"]
            + "</a>"
            for other in catalog
        ]
        if len(navs) != 1 or re.findall(r"<a\b[^>]*>.*?</a>", navs[0]) != expected_links:
            errors.append(name + ": incomplete or invalid language navigation")
        translated = content(text)
        if FENCE.findall(translated) != FENCE.findall(original):
            errors.append(name + ": fenced code differs from English")
        if Counter(re.findall(r"`([^`\n]+)`", translated)) != Counter(
            re.findall(r"`([^`\n]+)`", original)
        ):
            errors.append(name + ": inline code differs from English")
        if Counter(LINK.findall(translated)) != Counter(
            translated_link(link, source, code) for link in LINK.findall(original)
        ):
            errors.append(name + ": Markdown destinations differ from English")
        if structure(translated) != structure(original):
            errors.append(name + ": heading or list structure differs from English")
        if re.search(r"@@BLOCK\d+@@", translated):
            errors.append(name + ": unresolved authoring placeholder")
        if code in {"ar", "fa", "he"}:
            if f'<div dir="rtl" lang="{code}">\n\n' not in text:
                errors.append(name + ": missing RTL prose container")
            for block in FENCE.findall(translated):
                if '<div dir="ltr">\n\n' + block + "\n\n</div>" not in text:
                    errors.append(name + ": code block needs explicit LTR container")

if errors:
    raise SystemExit("\n".join(errors))
print("PASS: 10 complete guide families in 24 languages, source digests, links and SVG XML.")
