#!/usr/bin/env python3
"""Merge the iGEM programme with our instructor plan into what the site renders.

Reads:
    data/schedule_2026.json     from tools/fetch_schedule.py
    data/event_2026.json
    plan/instructor_plan.json   the hand-authored decisions
    _data/targets.json          from tools/build_site_data.py

Writes:
    _data/jamboree.json   event facts, counts, conflicts, open questions
    _data/program.json    one row per planned session, with who/tier/why/ask
    _data/fullprog.json   every open session in the programme, for browsing

Fails loudly if a plan key matches zero or several sessions, so a schedule
change at iGEM's end cannot silently drop an entry.

Re-run:  python3 tools/build_schedule_data.py
"""
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "_data"
PARIS = timedelta(hours=1)
PEOPLE = ("Gabriel", "Chars", "Timmy")


def paris(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).replace(tzinfo=None) + PARIS


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:70]


def main():
    sched = json.loads((DATA / "schedule_2026.json").read_text())
    event = json.loads((DATA / "event_2026.json").read_text())
    plan = json.loads((ROOT / "plan/instructor_plan.json").read_text())
    targets = json.loads((OUT / "targets.json").read_text())
    tgt_by_name = {t["name"]: t for t in targets}

    open_s = [s for s in sched if s["type"] != "judging-session"]
    by_title = {}
    by_team = {}
    for s in open_s:
        by_title.setdefault(s["title"], []).append(s)
        if s["type"] == "team-talk":
            by_team.setdefault(s["team"]["name"], []).append(s)

    errors = []
    rows = []

    def row(s, who, tier, why, ask=None, team=None, drop=False, track=None,
            ambient=False):
        a, b = paris(s["startTime"]), paris(s["endTime"])
        loc = (s.get("location") or {}).get("displayTitle") or "—"
        t = tgt_by_name.get(team) if team else None
        return {
            "id": slug((team or "") + "-" + s["title"]),
            "day": f"{a:%Y-%m-%d}",
            "dayname": f"{a:%a}",
            "start": f"{a:%H:%M}",
            "end": f"{b:%H:%M}",
            "mins": int((b - a).total_seconds() // 60),
            "where": loc,
            "type": s["type"],
            "title": s["title"],
            "team": team,
            "village": (t or {}).get("village", ""),
            "country": (t or {}).get("country", ""),
            "wiki": (t or {}).get("wiki"),
            "relevance": (t or {}).get("relevance", ""),
            "who": who,
            "tier": tier,
            "why": why,
            "ask": ask,
            "drop": drop,
            "track": track or "",
            "ambient": ambient,
            "official": s["type"] != "team-talk",
            "hook": s.get("hook") or "",
            "topics": [l["name"] for l in s.get("labels", [])],
            "org": ", ".join(o["label"] for o in (s.get("metadata") or {}).get("organizers", [])),
        }

    for p in plan["sessions"]:
        got = by_title.get(p["key"], [])
        if len(got) != 1:
            errors.append(f'session key matched {len(got)}: "{p["key"]}"')
            continue
        rows.append(row(got[0], p["who"], p["tier"], p["why"], p.get("ask"),
                        drop=p.get("drop", False), track=p.get("track"),
                        ambient=p.get("ambient", False)))

    for p in plan["team_sessions"]:
        got = by_team.get(p["team"], [])
        if len(got) != 1:
            errors.append(f'team key matched {len(got)}: "{p["team"]}"')
            continue
        rows.append(row(got[0], p["who"], p["tier"], p["why"], p.get("ask"),
                        team=p["team"], drop=p.get("drop", False)))

    for p in plan["own_blocks"]:
        a = datetime.strptime(f'{p["day"]} {p["start"]}', "%Y-%m-%d %H:%M")
        b = datetime.strptime(f'{p["day"]} {p["end"]}', "%Y-%m-%d %H:%M")
        rows.append({
            "id": slug(p["title"]), "day": p["day"], "dayname": f"{a:%a}",
            "start": p["start"], "end": p["end"],
            "mins": int((b - a).total_seconds() // 60),
            "where": p["where"], "type": "ours", "title": p["title"], "team": None,
            "village": "", "country": "", "wiki": None, "relevance": "",
            "who": p["who"], "tier": p["tier"], "why": p["why"], "ask": None,
            "drop": False, "track": "", "ambient": False, "official": False,
            "hook": "", "topics": [], "org": "",
        })

    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        sys.exit(1)

    rows.sort(key=lambda r: (r["day"], r["start"], r["end"]))
    for r in rows:
        r["group"] = "|".join(PEOPLE) if r["who"] == "All" else r["who"]

    # A bonus team talk is only worth listing if it fits around that person's
    # official plan. Work it out here rather than by hand, so the plan file
    # never has to be re-checked when an official pick moves.
    def span(r):
        s = datetime.strptime(f'{r["day"]} {r["start"]}', "%Y-%m-%d %H:%M")
        e = datetime.strptime(f'{r["day"]} {r["end"]}', "%Y-%m-%d %H:%M")
        return s, e

    for r in rows:
        if r["tier"] != "bonus":
            r["clash"] = ""
            continue
        rs, re_ = span(r)
        hit = None
        for o in rows:
            if o["tier"] == "bonus" or o["drop"] or o["tier"] == "own" \
                    or o["ambient"]:
                continue
            if o["who"] not in (r["who"], "All"):
                continue
            os_, oe = span(o)
            if os_ < re_ and rs < oe:
                hit = o
                break
        r["clash"] = hit["title"] if hit else ""

    (OUT / "program.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))

    # the whole programme, trimmed, so the browse page can search it
    full = []
    for s in sorted(open_s, key=lambda s: s["startTime"]):
        a, b = paris(s["startTime"]), paris(s["endTime"])
        team = (s.get("team") or {}).get("name")
        full.append({
            "day": f"{a:%Y-%m-%d}", "dayname": f"{a:%a}",
            "start": f"{a:%H:%M}", "end": f"{b:%H:%M}",
            "where": (s.get("location") or {}).get("displayTitle") or "—",
            "type": s["type"], "title": s["title"], "team": team,
            "hook": s.get("hook") or "",
            "planned": team in tgt_by_name if team else False,
            "search": re.sub(r"[^a-z0-9 ]+", " ", " ".join([
                s["title"], team or "", s.get("hook") or "",
                (s.get("location") or {}).get("displayTitle") or "", s["type"],
                " ".join(l["name"] for l in s.get("labels", [])),
            ]).lower()),
        })
    (OUT / "fullprog.json").write_text(json.dumps(full, ensure_ascii=False, indent=1))

    days = []
    for d in sorted({r["day"] for r in rows}):
        dt = datetime.strptime(d, "%Y-%m-%d")
        rs = [r for r in rows if r["day"] == d]
        days.append({
            "day": d, "label": f"{dt:%a %d %b}", "short": f"{dt:%a}".upper(),
            "n": sum(1 for r in rs
                     if not r["drop"] and r["tier"] != "bonus"),
            "anchors": sum(1 for r in rs if r["tier"] == "anchor"),
        })

    official = [r for r in rows if r["official"] and r["tier"] != "bonus"]
    tracks = []
    for t in plan["tracks"]:
        feed = [r for r in official if r["track"] == t["id"] and not r["drop"]]
        tracks.append({**t,
                       "n": len(feed),
                       "who": sorted({r["who"] for r in feed}),
                       "sessions": [{"title": r["title"], "who": r["who"],
                                     "dayname": r["dayname"], "start": r["start"],
                                     "where": r["where"], "tier": r["tier"],
                                     "ask": r["ask"], "id": r["id"]}
                                    for r in feed]})

    venue = event["metadata"]["venue"]
    (OUT / "jamboree.json").write_text(json.dumps({
        "title": event["title"],
        "venue": venue["name"], "detail": venue["detail"],
        "lat": venue["latitude"], "lon": venue["longitude"],
        "start": event["startDate"][:10], "end": event["endDate"][:10],
        "sessions_total": len(sched),
        "sessions_open": len(open_s),
        "sessions_judging": len(sched) - len(open_s),
        "team_talks": sum(1 for s in open_s if s["type"] == "team-talk"),
        "official_total": len(open_s) - sum(1 for s in open_s if s["type"] == "team-talk"),
        "official_planned": sum(1 for r in official if not r["drop"]),
        "official_dropped": sum(1 for r in official if r["drop"]),
        "bonus_free": sum(1 for r in rows if r["tier"] == "bonus" and not r["clash"]),
        "planned": sum(1 for r in rows if not r["drop"] and r["tier"] != "bonus"),
        "dropped": sum(1 for r in rows if r["drop"]),
        "tracks": tracks,
        "targets": len(targets),
        "targets_with_talk": sum(1 for t in targets if t["name"] in by_team),
        "booth_only": sorted(t["name"] for t in targets if t["name"] not in by_team),
        "per_person": {p: sum(1 for r in rows
                              if r["who"] in (p, "All") and not r["drop"]
                              and r["tier"] != "bonus")
                       for p in PEOPLE},
        "days": days,
        "expo": event["metadata"]["expoDayPlan"],
        "pods": event["metadata"]["podOpeningHours"],
        "conflicts": plan["conflicts"],
        "unresolved": plan["unresolved"],
    }, ensure_ascii=False, indent=1))

    off_total = len(open_s) - sum(1 for s in open_s if s["type"] == "team-talk")
    print(f"official: {sum(1 for r in official if not r['drop'])} attending, "
          f"{sum(1 for r in official if r['drop'])} considered and dropped, "
          f"of {off_total} in the programme")
    print(f"per head: {Counter(r['who'] for r in official if not r['drop']).most_common()}")
    print(f"tiers:    {Counter(r['tier'] for r in rows).most_common()}")
    print(f"bonus:    {sum(1 for r in rows if r['tier'] == 'bonus')} team talks, "
          f"{sum(1 for r in rows if r['tier'] == 'bonus' and not r['clash'])} fit the gaps")
    print(f"tracks:   {[(t['id'], t['n']) for t in tracks]}")
    print(f"fullprog: {len(full)} open sessions")


if __name__ == "__main__":
    main()
