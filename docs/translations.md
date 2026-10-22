# Maintaining documentation translations

The six detailed guides and four checked-in wiki pages have complete versions
in the 24 languages from [`languages.json`](languages.json), following the
[ha-homelab catalog](https://github.com/ha-homelab/.github/blob/main/languages.json).
CLI messages and README translations retain their existing four-language scope.

The English detailed sources live in `docs/en/`. Other languages use matching
files in `docs/<language>/`. The checked-in wiki pages are separate concise
introductions, not generated mirrors: their English files are `wiki/Home.md`,
`wiki/Installation.md`, `wiki/Model.md` and `wiki/Troubleshooting.md`, with
`-<language>` before `.md` for translations. Publishing the checked-in pages to
the separately hosted GitHub wiki remains a separate operation.

When English changes, update every complete translation of that family. Keep
all procedures, limitations, diagnostics, privacy boundaries and examples, not
just a summary. Commands, inline technical literals and external links stay
exact. Links between translated guides and wiki pages follow the reader's
language. Links to the untranslated README or security policy remain unchanged.
Each family page links to all 24 languages of the same page.

Arabic, Persian and Hebrew prose uses explicit right-to-left containers; fenced
code and the language navigation use left-to-right containers. Keep a blank line
after HTML containers so GitHub parses the enclosed Markdown.

After reviewing the translations, update the English source digest in
[`translations.json`](translations.json). Each digest is SHA-256 of the UTF-8
source after replacing the language-navigation block and its adjacent newlines
with one blank line, then stripping surrounding whitespace. All other whitespace,
including blank lines in executable examples, remains significant. This makes later
English changes fail the documentation check until their translations are reviewed.

Stage added files and run `python3 tools/check_docs.py`. The existing CI validates
all 240 family pages, English digests, language navigation and text direction,
fenced code, inline literals, Markdown destinations, headings and lists, relative
links and SVG XML. Structural parity cannot establish linguistic accuracy;
review translated prose and preview representative GitHub pages, including RTL
instructions with a code block. Application behavior and permissions do not
change with documentation language coverage.
