# Worked examples

[Input model](model.md) · [Architecture](architecture.md) · [Русский](../ru/examples.md)

All hardware and roles here are synthetic. Recreate identical inputs with
`python3 tools/generate_examples.py`. No command connects to Home Assistant.

## A lamp role leaves a repurposed plug

Run the README command for `examples/role-swap`. Initially `plug-a/1` owns
`light.workbench` and `plug-b/1` owns `switch.spare`. The manifest assigns the pump
role to plug A and the workbench role to plug B. The lighting automation uses
`follows_role` and allows only `workbench`. Its entity reference remains
`light.workbench` while the destination hardware changes. This absence of a text
edit is the intended result, not a missing migration. The report's `assignments`
contains the hardware changes for human review.

The old spare consumer is retired at `/1`, the whole second automation object.
This does not leave an empty action sequence. The report is advisory; no JSON
array element is removed by the program. If applying several proposed array
removals manually, account for shifted indexes and rerun from a fresh snapshot.

Change the first policy to `follows_hardware` while leaving its allowed role as
`workbench`: the plan blocks with `role_not_allowed`. Broadening that allowed-role
list to include a pump is an explicit dangerous intent change, not a routine way
to clear the error. Restore the correct policy instead.

## A relay changes from light to switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

The two proposed edits change the target and its `light.turn_off` service. Add
brightness data to the source action, update the approved source fingerprint,
and rerun: `service_data_review` blocks automatic conversion. Do not discard
brightness settings merely to satisfy the tool; review the desired behavior.

## An unresolved template

Run the same command with `examples/blocked-template`. The target is dynamic
Jinja. The tool does not evaluate it and returns code 3. A complete supported
plan requires explicit configuration with provable literal targets; otherwise
retain this as a documented manual migration outside the ready scope. Ignoring
the exit code does not resolve the template.

## Drift and repeatability

Editing a source without changing its manifest hash produces `stale_source`.
Editing the snapshot produces `stale_snapshot`. No candidate reference edits are
emitted for these stale models. On unchanged files the JSON result is deterministic
apart from your selected language. Source files remain byte-for-byte unchanged.

For a real project, copy the format into a private folder, verify physical
identities, enumerate consumers and run the planner. Review all assignments and
edits, perform HA's own checks in your established deployment process, then make
a new read-only snapshot to verify the result. This project does not implement
that deployment or a rollback executor.
