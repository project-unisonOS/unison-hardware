# Open hardware design conventions

Status: required repository convention

- Store editable sources beside generated PDF, STEP, Gerber, drill, and BOM outputs.
- Record tool name, version, units, coordinate origin, layer mapping, and generation command.
- Use stable identifiers that link requirements, interfaces, BOM items, schematics, boards, harnesses, and qualification evidence.
- Never commit vendor files without redistribution permission.
- Record every safety-critical assumption and review owner.
- Mark concept, candidate, prototype, qualified, superseded, and rejected revisions explicitly.
- A generated artifact without its editable source is not an accepted Unison design source.
- No fabrication or redistribution license is implied until `LICENSE-STATUS.md` records the selected license.
