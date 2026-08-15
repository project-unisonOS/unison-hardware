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
        value = yaml.safe_load(record.read_text())
        jsonschema.validate(value, schema)
        total = sum(item["quantity"] * item["unit_cost_estimate"] for item in value["items"])
        if total <= 0:
            raise SystemExit("BOM estimate total must be positive")
        print(f"validated {record.relative_to(ROOT)}")
    budget = yaml.safe_load((ROOT / "system/power-thermal-budget.yaml").read_text())
    if budget.get("schema_version") != "unison-power-thermal-budget.v1" or budget.get("evidence") != "planned":
        raise SystemExit("power and thermal budget must remain explicitly planned")
    plan = yaml.safe_load((ROOT / "qualification/gpu-workstation-plan.yaml").read_text())
    if plan.get("state") != "deferred" or len(plan.get("test_groups", [])) < 5:
        raise SystemExit("GPU qualification plan must remain deferred with all test groups")
    for name in ("collect_gpu_baseline.py", "run_qualification.py"):
        if not (ROOT / "scripts" / name).is_file():
            raise SystemExit(f"missing qualification tool: {name}")
    print(f"validated {len(interfaces)} interface definitions")


if __name__ == "__main__":
    main()
