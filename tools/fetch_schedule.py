#!/usr/bin/env python3
"""Pull the 2026 Grand Jamboree programme from the public iGEM API.

The schedule page at jamboree.igem.org is a React SPA. It reads two endpoints
that need no login, found by grepping its JS bundle (assets/data-access-*.js):

    GET /v1/events                              -> the jamboree for each year
    GET /v1/events/{uuid}                       -> venue, expo groups, pod hours
    GET /v1/events/{uuid}/sessions/schedule     -> every session (799 of them)
    GET /v1/events/{uuid}/sessions/metadata     -> locations, types, label tree

Note /v1/events/{uuid}/sessions (without /schedule) returns 401. Use /schedule.

All times in the API are UTC. Paris in November is UTC+1.

Writes:
    data/event_2026.json        the event record
    data/schedule_2026.json     all sessions
    data/schedule_meta.json     locations / types / labels
    data/schedule_2026.md       readable programme, judging sessions excluded

Re-run:  python3 tools/fetch_schedule.py
"""
import json
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

API = "https://api.igem.org/v1"
YEAR = 2026
PARIS = timedelta(hours=1)  # Europe/Paris in November
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def get(path):
    req = urllib.request.Request(f"{API}/{path}", headers={"User-Agent": "igem-report/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def paris(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).replace(tzinfo=None) + PARIS


def main():
    DATA.mkdir(exist_ok=True)

    events = get("events")
    ev = next(e for e in events if (e.get("competition") or {}).get("year") == YEAR)
    uuid = ev["uuid"]

    event = get(f"events/{uuid}")
    sessions = get(f"events/{uuid}/sessions/schedule")
    meta = get(f"events/{uuid}/sessions/metadata")

    (DATA / "event_2026.json").write_text(json.dumps(event, ensure_ascii=False, indent=1))
    (DATA / "schedule_2026.json").write_text(json.dumps(sessions, ensure_ascii=False, indent=1))
    (DATA / "schedule_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))

    # Readable programme. 423 of the 799 sessions are closed judging slots; they
    # carry no content, so the markdown keeps only the ones you can walk into.
    open_sessions = [s for s in sessions if s["type"] != "judging-session"]
    open_sessions.sort(key=lambda s: (s["startTime"], (s.get("location") or {}).get("displayTitle") or ""))

    out = [
        "# 2026 iGEM Grand Jamboree — programme",
        "",
        f"{event['title']} · {event['metadata']['venue']['name']}, "
        f"{event['metadata']['venue']['detail']}",
        f"{paris(event['startDate']):%d %B} – {paris(event['endDate']):%d %B %Y} · "
        "all times Paris (UTC+1)",
        "",
        f"Pulled from the public iGEM API. {len(sessions)} sessions in total; "
        f"{len(sessions) - len(open_sessions)} are closed judging slots and are not listed here.",
        "",
    ]
    day = None
    for s in open_sessions:
        a, b = paris(s["startTime"]), paris(s["endTime"])
        if a.date() != day:
            day = a.date()
            out += ["", f"## {a:%A %d %B}", ""]
        loc = (s.get("location") or {}).get("displayTitle") or "—"
        team = (s.get("team") or {}).get("name")
        who = f"{team} · " if team else ""
        org = ", ".join(o["label"] for o in (s.get("metadata") or {}).get("organizers", []))
        out.append(f"### {a:%H:%M}–{b:%H:%M} · {loc} · {s['type']}")
        out.append("")
        out.append(f"**{who}{s['title']}**")
        out.append("")
        if s.get("hook"):
            out.append(s["hook"])
            out.append("")
        bits = []
        if org:
            bits.append(f"Organiser: {org}")
        if s["labels"]:
            bits.append("Topics: " + ", ".join(l["name"] for l in s["labels"]))
        if bits:
            out.append(" · ".join(bits))
            out.append("")

    (DATA / "schedule_2026.md").write_text("\n".join(out))

    print(f"event:    {event['title']} {event['startDate'][:10]} -> {event['endDate'][:10]}")
    print(f"venue:    {event['metadata']['venue']['name']}, {event['metadata']['venue']['detail']}")
    print(f"sessions: {len(sessions)} ({len(open_sessions)} open, "
          f"{len(sessions) - len(open_sessions)} judging)")


if __name__ == "__main__":
    main()
