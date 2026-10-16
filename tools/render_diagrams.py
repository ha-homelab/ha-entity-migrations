"""Original deterministic SVG diagrams; no downloaded media or measurements."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "diagrams"


def start(title, description, height=440):
    return [
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#334155"/></marker></defs>
<rect width="960" height="{height}" fill="#f8fafc"/>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:#0f172a}}.title{{font-size:25px;font-weight:bold}}.label{{font-size:18px;font-weight:bold}}.small{{font-size:15px}}.caption{{font-size:16px;fill:#475569}}</style>
<text x="32" y="44" class="title">{escape(title)}</text>'''
    ]


def box(x, y, w, title, subtitle, color="#e2e8f0"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="76" rx="6" fill="{color}" stroke="#64748b"/><text x="{x + 16}" y="{y + 29}" class="label">{escape(title)}</text><text x="{x + 16}" y="{y + 54}" class="small">{escape(subtitle)}</text>'


def arrow(x1, y1, x2, y2):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>'


def caption(x, y, text):
    return f'<text x="{x}" y="{y}" class="caption">{escape(text)}</text>'


def finish(name, parts):
    (ROOT / name).write_text("\n".join(parts + ["</svg>", ""]), encoding="utf-8")


def main():
    parts = start(
        "A role moves; hardware keeps its own identity",
        "Synthetic before and after. The lighting automation still follows the workbench lamp role on plug B. Plug A becomes pump power and is excluded from the lighting action.",
    )
    parts += [
        caption(32, 83, "BEFORE · synthetic example"),
        caption(520, 83, "AFTER · proposed assignments"),
    ]
    parts += [
        box(32, 103, 390, "Plug A / channel 1", "light.workbench · role: workbench"),
        box(32, 213, 390, "Plug B / channel 1", "switch.spare · role: spare"),
    ]
    parts += [
        box(
            520, 103, 408, "Plug A / channel 1", "switch.pump_enable · role: pump_enable", "#ffedd5"
        ),
        box(520, 213, 408, "Plug B / channel 1", "light.workbench · role: workbench", "#ccfbf1"),
    ]
    parts += [
        arrow(422, 141, 508, 141),
        arrow(422, 251, 508, 251),
        box(
            190,
            333,
            570,
            "Lighting action follows the workbench role",
            "Allowed roles reject accidental pump control",
            "#ccfbf1",
        ),
    ]
    parts += [arrow(723, 289, 650, 322)]
    finish("role-transfer.svg", parts)
    parts = start(
        "Read files → verify declarations → review a plan",
        "Offline data flow with strict JSON input, byte fingerprints, semantic checks and a read-only report. No Home Assistant connection or apply stage.",
        380,
    )
    parts += [
        box(32, 105, 250, "Explicit private inputs", "Manifest · snapshot · JSON"),
        box(354, 105, 252, "Validate and resolve", "Hashes · roles · capabilities"),
        box(678, 105, 250, "Report to stdout", "ready / blocked / invalid"),
    ]
    parts += [
        arrow(282, 143, 341, 143),
        arrow(606, 143, 665, 143),
        caption(32, 234, "Unresolved templates, indirect targets or unsupported formats → blocked"),
        caption(
            32,
            278,
            "No network client. No template execution. No files changed. No physical acceptance claimed.",
        ),
        caption(
            32,
            328,
            "Scope: only supplied files and declared identities. Report operations are advisory, not JSON Patch.",
        ),
    ]
    finish("pipeline.svg", parts)
    parts = start(
        "Explicit consumer policies and guardrails",
        "A literal source reference follows role, follows hardware, or retires its declared object. Capability and role guards apply; ambiguity blocks the plan.",
        470,
    )
    parts += [
        box(32, 92, 230, "Literal source reference", "Exact JSON pointer"),
        box(344, 92, 258, "follows_role", "Locate destination by role"),
        box(344, 203, 258, "follows_hardware", "Locate the physical channel"),
        box(344, 314, 258, "retire", "Review whole object removal"),
    ]
    parts += [
        arrow(262, 130, 331, 130),
        '<path d="M296,130 L296,241 L331,241" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>',
        '<path d="M296,241 L296,352 L331,352" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#arrow)"/>',
        box(682, 142, 246, "Check declared guards", "Role · capabilities · domain", "#ccfbf1"),
        box(682, 285, 246, "Needs manual review?", "BLOCKED · manual review", "#ffedd5"),
        arrow(602, 130, 670, 165),
        arrow(602, 241, 670, 195),
        arrow(805, 218, 805, 273),
        caption(
            32,
            437,
            "Synthetic process illustration. A passing declaration is not proof that hardware is safe or correctly identified.",
        ),
    ]
    finish("policy.svg", parts)


if __name__ == "__main__":
    main()
