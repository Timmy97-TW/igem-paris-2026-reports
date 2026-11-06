#!/usr/bin/env python3
"""Build the Jekyll data files the site renders from.

  _data/targets.json  the assigned priority targets, pulled out of research/triage_*.md
  _data/teams.json    every accepted team, trimmed for the browse page

Re-run after editing any triage file:  python3 tools/build_site_data.py
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data"
DATA.mkdir(exist_ok=True)

TRIAGE = {
    "A": ("triage_A_agri_env_food.md", "Agriculture, bioremediation, conservation, food"),
    "B": ("triage_B_mfg_foundational_sw_space.md", "Biomanufacturing, foundational, software, space"),
    "C": ("triage_C_health.md", "Therapeutics, oncology, infectious disease"),
}
WHO = {"G": "Gabriel", "Ch": "Chars", "T": "Timmy",
       "Gabriel": "Gabriel", "Chars": "Chars", "Timmy": "Timmy"}

teams = {t["name"]: t for t in json.loads((ROOT / "data/teams_2026.json").read_text())}

targets = []
for key, (fn, slice_label) in TRIAGE.items():
    txt = (ROOT / "research" / fn).read_text()
    for block in re.split(r"\n(?=### )", txt):
        m = re.match(r"### (.+?) — (.+?) \((.+?)\)\n", block)
        if not m:
            continue
        name, title, meta = (x.strip() for x in m.groups())
        who = re.search(r"-\s*\**Assign:?\**:?\s*\**\s*([A-Za-z]+)", block)
        rel = re.search(r"-\s*\**Relevance:?\**:?\s*(.+)", block)
        why = re.search(r"-\s*\**(?:Worth the walk|Why it['’]s worth the walk):?\**:?\s*(.+)", block)
        t = teams.get(name, {})
        relevance = re.sub(r"^to ReLeaf/GEMS:\s*", "", rel.group(1).strip()) if rel else ""
        targets.append({
            "name": name,
            "title": title,
            "meta": meta,
            "who": WHO.get(who.group(1) if who else "", "Unassigned"),
            "relevance": relevance,
            "why": (why.group(1).strip() if why else ""),
            "wiki": t.get("wiki"),
            "village": t.get("village", ""),
            "country": t.get("country", ""),
            "slice": slice_label,
            "id": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"),
        })

targets.sort(key=lambda r: (r["who"], r["name"].lower()))
(DATA / "targets.json").write_text(json.dumps(targets, ensure_ascii=False, indent=1))

rows = []
for t in json.loads((ROOT / "data/teams_2026.json").read_text()):
    if t["status"] != "accepted":
        continue
    ab = t["abstract"].replace("\n", " ").strip()
    rows.append({
        "name": t["name"], "title": t["title"], "village": t["village"] or "Unassigned",
        "country": t["country"], "section": t["section"] or "", "wiki": t["wiki"],
        "page": t["team_page"],
        "blurb": (ab[:240].rsplit(" ", 1)[0] + "…") if len(ab) > 240 else ab,
        # full abstract, lowercased and stripped of punctuation, so search reaches the whole text
        "search": re.sub(r"[^a-z0-9 ]+", " ",
                         f"{t['name']} {t['title']} {t['village']} {t['country']} {ab}".lower()),
        "has_abstract": bool(ab),
    })
rows.sort(key=lambda r: r["name"].lower())
(DATA / "teams.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))

by_person = {}
for t in targets:
    by_person[t["who"]] = by_person.get(t["who"], 0) + 1
print(f"targets: {len(targets)} {by_person}")
print(f"teams:   {len(rows)} ({sum(1 for r in rows if r['has_abstract'])} with abstracts)")
print(f"villages: {len({r['village'] for r in rows})}")
