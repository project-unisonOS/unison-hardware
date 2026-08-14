#!/usr/bin/env python3
"""Validate hardware registries and BOM records without implying qualification."""

from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    interface_registry = yaml.safe_load((ROOT / "interfaces/registry.yaml").read_text())
    interfaces = interface_registry.get("interfaces", [])
    if not interfaces:
        raise SystemExit("interface registry is empty")
    identifiers = [item["interface_id"] for item in interfaces]
    if len(identifiers) != len(set(identifiers)):
        raise SystemExit("interface IDs must be unique")

    schema = yaml.safe_load((ROOT / "bom/bom.schema.json").read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    for record in sorted((ROOT / "bom").glob("*.yaml")):
        jsonschema.validate(yaml.safe_load(record.read_text()), schema)
        print(f"validated {record.relative_to(ROOT)}")
    print(f"validated {len(interfaces)} interface definitions")


if __name__ == "__main__":
    main()
