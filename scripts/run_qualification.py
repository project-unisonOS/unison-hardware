#!/usr/bin/env python3
"""Fail closed until a named physical test adapter is configured."""
import argparse
GROUPS = {"inference", "rebuild", "power-thermal", "resilience"}
parser = argparse.ArgumentParser(); parser.add_argument("--group", choices=sorted(GROUPS), required=True)
args = parser.parse_args()
raise SystemExit(f"{args.group} qualification requires the named workstation, fixtures, and measurement adapter")
