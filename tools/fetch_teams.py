#!/usr/bin/env python3
"""Fetch every iGEM 2026 team with its village, project title, abstract and wiki URL.

Source: the public api.igem.org endpoints that teams.igem.org itself calls.
  GET /v1/teams?year=2026&pageSize=100&page=N   team list
  GET /v1/villages?year=2026                     village names + colours
  GET /v1/teams/{id}/artifacts                   'description' artifact = title + abstract
  GET /v1/teams/wikis?teamIDs=a,b,c              wiki URLs

Writes data/teams_2026.json (raw, for reuse) and data/teams_2026.md (human-readable).
Re-run any time; it is read-only against the API and rate-limited.
"""
import json, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

API = "https://api.igem.org/v1"
YEAR = 2026
OUT = Path(__file__).resolve().parent.parent / "data"
UA = {"User-Agent": "GEMS-Taiwan-jamboree-notes/1.0"}


def get(path, params=None, tries=4):
    url = f"{API}/{path}" + ("?" + urllib.parse.urlencode(params) if params else "")
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                print(f"FAIL {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2 * (i + 1))


def main():
    teams, page = [], 1
    while True:
        d = get("teams", {"year": YEAR, "pageSize": 100, "page": page})
        teams += d["data"]
        if len(teams) >= d["total"] or not d["data"]:
            break
        page += 1
    print(f"{len(teams)} teams listed")

    villages = {v["uuid"]: v["latestVersion"]["title"] for v in get("villages", {"year": YEAR})}

    def artifacts(t):
        time.sleep(0.15)
        return t["id"], get(f"teams/{t['id']}/artifacts") or []

    with ThreadPoolExecutor(4) as ex:
        arts = dict(ex.map(artifacts, teams))

    wikis = {}
    ids = [t["id"] for t in teams]
    for i in range(0, len(ids), 40):
        for w in get("teams/wikis", {"teamIDs": ",".join(map(str, ids[i:i + 40]))}) or []:
            wikis[w["teamID"]] = w.get("pageURL")

    rows = []
    for t in teams:
        desc = next((a["metadata"] for a in arts[t["id"]] if a["type"] == "description" and a.get("metadata")), {}) or {}
        rows.append({
            "id": t["id"], "name": t["name"], "status": t["status"], "section": t["section"],
            "program": t["program"], "region": t["region"], "country": t["country"], "city": t["city"],
            "village": villages.get(t["villageUUID"], "—"),
            "title": (desc.get("title") or "").strip(),
            "abstract": (desc.get("abstract") or "").strip(),
            "wiki": wikis.get(t["id"]),
            "team_page": f"https://teams.igem.org/{t['id']}",
        })
    rows.sort(key=lambda r: (r["village"], r["name"].lower()))

    OUT.mkdir(exist_ok=True)
    (OUT / "teams_2026.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))

    have = sum(1 for r in rows if r["abstract"])
    md = [f"# iGEM {YEAR} — all teams and project abstracts", "",
          f"Pulled {time.strftime('%Y-%m-%d')} from api.igem.org (`tools/fetch_teams.py`). "
          f"{len(rows)} teams; {have} have a published abstract. Grouped by village, alphabetical within.", ""]
    cur = None
    for r in rows:
        if r["village"] != cur:
            cur = r["village"]
            n = sum(1 for x in rows if x["village"] == cur)
            md += ["", f"## {cur} ({n})", ""]
        links = f"[team page]({r['team_page']})" + (f" · [wiki]({r['wiki']})" if r["wiki"] else "")
        md += [f"### {r['name']} — {r['title'] or '*(no title)*'}",
               f"*{r['country']} · {r['section']} · {r['status']}* · {links}", "",
               (r["abstract"] or "*(no abstract published)*").replace("\n", "\n\n"), ""]
    (OUT / "teams_2026.md").write_text("\n".join(md))
    print(f"wrote {OUT}/teams_2026.{{json,md}} — {have}/{len(rows)} with abstracts")


if __name__ == "__main__":
    main()
