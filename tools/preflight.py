#!/usr/bin/env python3
"""Lay every sheet over the others: list unfilled cells and unresolved references."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent / "sheets"
sheets = {p.stem: json.loads(p.read_text()) for p in sorted(root.glob("*.json"))}
ids = {r["id"] for rows in sheets.values() for r in rows}
refcols = {"spawnHook","convertHook","giveHook","playHook","inputHook","uiHook","engineSound","sound","entries"}
issues = []
for name, rows in sheets.items():
    for r in rows:
        for col, val in r.items():
            if val is None or val is False and col in {"verified","tested"}:
                issues.append(f"UNFILLED  {name}/{r['id']}.{col}")
            if col in refcols and val is not None:
                for ref in (val if isinstance(val, list) else [val]):
                    if ref not in ids:
                        issues.append(f"BROKEN    {name}/{r['id']}.{col} -> {ref}")
print("\n".join(issues))
print(f"\n{len(issues)} open cells/references across {sum(map(len, sheets.values()))} rows")
sys.exit(1 if issues else 0)
