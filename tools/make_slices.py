#!/usr/bin/env python3
"""Split data/teams_2026.json into the four village slices used for pre-trip triage."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLICES = {
    "A_agri_env_food": ["Agriculture", "Bioremediation", "Conservation", "Climate Crisis", "Food & Nutrition"],
    "B_mfg_foundational_sw_space": ["Biomanufacturing", "Foundational Advance", "Software & AI", "Space"],
    "C_health": ["Therapeutics", "Oncology", "Infectious Diseases"],
    "D_dx_fashion_other": ["Diagnostics", "Fashion & Cosmetics", "—"],
}
KEEP = ("id", "name", "village", "country", "section", "title", "abstract", "wiki")

teams = [t for t in json.loads((ROOT / "data/teams_2026.json").read_text()) if t["status"] == "accepted"]
out = ROOT / "research/_slices"
out.mkdir(parents=True, exist_ok=True)
for name, villages in SLICES.items():
    rows = [{k: t[k] for k in KEEP} for t in teams if t["village"] in villages]
    (out / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=0))
    print(f"{name}: {len(rows)}")
