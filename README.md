# Paris Grand Jamboree 2026 — the instructors' hub

Three instructors from **GEMS Taiwan** (Timmy, PI / dry lab · Chars, wet lab · Gabriel, wet lab)
attend the Grand Jamboree in Paris, 13–16 November 2026, and each owes a written research report
afterwards. This repo is the plan, the shared evidence base and the three reports, published as a
GitHub Pages site.

Live at <https://timmy97-tw.github.io/igem-paris-2026-reports/>. The students' own trip site is
[ReLEAF to Paris](https://timmy97-tw.github.io/releaf-jamboree/); logistics numbers here come from it.

## The plan in one paragraph

The Jamboree publishes **799 sessions**, of which 423 are closed judging slots and 305 are
ten-minute student team talks. That leaves **71 official sessions** — keynotes, featured panels, the
iGEM Technology panels, the BioInnovation Summit, the Responsibility Conference and the Community
workshops, all given by industry and academic speakers. All 71 are triaged: **48 attended, 23
dropped**. Every attended session is tagged with one of **eight GEMS capability tracks**, so the
three reports combine into one institutional document.

## How it is organised

| Path | What it holds |
|---|---|
| `index.html` | The hub |
| `schedule.html` | **The four days** — the plan, hour by hour, filterable per person |
| `duties.html` | **帶隊分工表** — the 10–18 Nov duty roster: squads, roll call, duty rota, training, booth, materials, safety, emergency cards (zh-Hant) |
| `research-log.md` | **研究紀錄** — the nightly research discussion and the 2027 topic table |
| `tracks.html` | **Growth tracks** — the eight capabilities, what we have, what we are missing |
| `before.md` | Before we fly: the nine-day trip, what to settle at badge pickup, what to carry |
| `ground.md` | On the ground: venue, rooms, transport, the booth, emergencies |
| `after.md` | After we land: notes → three reports → one plan for 2027 |
| `program.html` | All 376 open sessions, searchable |
| `brief.md` | Pak's brief and our working rules |
| `plan/instructor_plan.json` | **The judgment layer.** Hand-authored: who attends what, and why |
| `floor-plan.html` | The 57 pre-trip team targets, searchable, tickable |
| `teams.html` | All 452 accepted teams, searchable across full abstracts |
| `research/` | Pre-trip triage of every 2026 team from their published abstracts |
| `notes/` | **On the trip.** One file per session, from `notes/_TEMPLATE.md` |
| `buckets/` | **After.** Synthesis across the four themes of the brief |
| `reports/` | The three individual reports — the actual deliverable |
| `followups.md` | Who to contact after returning, and about what |
| `gaps.md` | What we did not see, and why |
| `_data/` | Generated. What the interactive pages render |
| `data/` | Cached API pulls: the programme, the teams |

## The eight growth tracks

The four themes of Pak's brief (**C** concepts · **H** hardware · **M** computation · **S** science
for good) set what the report answers. The tracks are what each session is chosen against:

| | Track | Feeds |
|---|---|---|
| T1 | Measurement you can defend | Measurement + Hardware awards, the OD600 channel, the DNPH assay |
| T2 | The self-running experiment | the digital twin, the AI sentinel layer |
| T3 | Hosts that actually secrete | the four ABDI secretion blockers |
| T4 | Parts other people can use | registry, standards, open science |
| T5 | Responsibility as design | Safety & Security, IHP, the kill switch |
| T6 | From project to product | whether a GEMS project outlives its competition year |
| T7 | The pipeline | the 2027 cohort, Pak's research-methods class |
| T8 | Why it didn't reproduce | institutional memory of our own failures |

## Regenerating

The programme comes from iGEM's public API. These endpoints need no login:

```
GET /v1/events                           the jamboree for each year
GET /v1/events/{uuid}                    venue, expo groups, pod hours
GET /v1/events/{uuid}/sessions/schedule  all 799 sessions
GET /v1/events/{uuid}/sessions/metadata  locations, types, label tree
```

Note `/sessions` without `/schedule` returns 401. All API times are UTC; Paris in November is UTC+1.

```bash
python3 tools/fetch_teams.py          # re-pull the 463 teams
python3 tools/fetch_schedule.py       # re-pull the programme
python3 tools/build_site_data.py      # _data/targets.json, _data/teams.json
python3 tools/build_schedule_data.py  # _data/program.json, fullprog.json, jamboree.json
```

`build_schedule_data.py` exits non-zero if a key in `plan/instructor_plan.json` matches zero or
several sessions. **Run the two build scripts after editing any triage file or the plan**, or the
site keeps showing old numbers.

## Working rules

1. **One note per session, from the template.**
2. **Mechanism, not claim.** Record how they did it.
3. **Mark where it came from.** `confidence:` separates what you were told, what you read off a
   poster, and what you worked out yourself.
4. **Fill `relevance:` on the spot.**
5. **Do not all walk the same aisle.** The plan splits the official programme three ways.
6. **Write the notes the same evening.** Budget 45 minutes each night.

## Photographs

Posters and booths are fine. **Ask before photographing people, and ask before photographing
anything that may be unpublished.** For each team shoot three frames: the poster wide, the one figure that matters, and
something with the team name legible.
