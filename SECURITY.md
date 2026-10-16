# Security and privacy

This tool reads explicit local files and writes a report to stdout. It does not
connect to HA, import Home Assistant configuration code, render Jinja, load YAML
tags, run shell commands or apply edits. Reports still contain entity names,
hardware/channel identifiers and file paths supplied by you. Keep inputs and
reports private; stdout redirection and terminal history are your responsibility.
Snapshot fingerprints detect a changed input, not authenticity or trusted intent.

JSON inputs reject duplicate keys, non-finite numbers, invalid UTF-8 and excessive
depth/nodes. Each file is limited to 2 MiB; source data is limited to 16 MiB and
64 files; inventory/assignment/consumer lists are bounded. Files must be regular,
not symlinks, FIFOs or devices. Source paths cannot escape their explicit root.
These are robustness controls, not an operating-system sandbox: run untrusted
inputs under a restricted account/container when appropriate. Do not process
directories that another user can mutate concurrently.

Unknown templates, indirect targets, unsupported formats, mixed domain targets
and incomplete consumer coverage block a plan. A malicious or mistaken manifest
can still lie about roles or capabilities. Review the physical mapping and any
proposal before manually changing your home. Never use a `ready` result as
evidence of electrical safety or successful physical commissioning.

For vulnerabilities, use GitHub private vulnerability reporting when enabled,
or contact the repository owner privately. Do not open a public issue containing
credentials or live inventories. Public reports should use synthetic examples.
