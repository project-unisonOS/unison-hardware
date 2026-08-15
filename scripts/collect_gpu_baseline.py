#!/usr/bin/env python3
"""Collect content-free hardware inventory after the workstation arrives."""
import argparse, json, platform, shutil, subprocess
from pathlib import Path

def command(args):
    if not shutil.which(args[0]): return {"available": False, "rows": []}
    result = subprocess.run(args, capture_output=True, text=True, check=False, timeout=20)
    return {"available": True, "exit_code": result.returncode,
            "rows": [line for line in result.stdout.splitlines() if line.strip()]}

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--output", required=True); args = parser.parse_args()
    evidence = {"schema_version": "unison-gpu-baseline.v1", "evidence_class": "physical-inventory",
        "system": platform.platform(), "machine": platform.machine(),
        "gpu": command(["nvidia-smi", "--query-gpu=name,memory.total,driver_version,pci.bus_id", "--format=csv,noheader"]),
        "block_devices": command(["lsblk", "--json", "--bytes"]), "network": command(["ip", "-json", "link"])}
    path = Path(args.output); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(path)
if __name__ == "__main__": main()
