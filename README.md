# Paris Grand Jamboree 2026 — adviser field reports

Private repo. Three advisers from **GEMS-Taiwan** (Gabriel, wet lab · Chars, wet lab · Timmy, PI /
dry lab) attend the Grand Jamboree in Paris and each owes a written research report afterwards.
This repo is the shared evidence base and the three reports, published as a GitHub Pages site.

## How it is organised

| Path | What it holds |
|---|---|
| `index.md` | Site homepage — what we went looking for |
| `research/` | **Pre-trip.** Triage of all 2026 teams from their published abstracts, by village slice |
| `data/teams_2026.md` | All 463 teams for 2026, grouped by village, with project title and abstract |
| `tools/fetch_teams.py` | Re-pulls that list from the public iGEM API |
| `notes/` | **On the trip.** One file per team or talk, from `notes/_TEMPLATE.md` |
| `buckets/` | **After.** Synthesis across teams, under the four themes of the brief |
| `reports/` | The three individual reports — the actual deliverable |
| `followups.md` | Who to contact after returning, and about what |
| `gaps.md` | What we did not see, and why |
| `photos/` | Images, named `<team>_<what>.jpg` |

## The four themes

Everything is filed under the themes of the adviser's brief:

- **C** — novel concepts and interdisciplinary work
- **H** — hardware and automation
- **M** — computation, modelling, data
- **S** — science for good

## Working rules

1. **One note per team, from the template.** Free-form notes do not merge across three people.
2. **Mechanism, not claim.** Record how they did it. A note with no "how" is a photo caption.
3. **Mark where it came from.** `confidence:` separates what a team member told you from what you
   read off a poster from what you worked out yourself. In six months this is the difference
   between a usable note and a rumour.
4. **Decide the relevance on the spot.** A note without a `relevance:` is an unfinished note.
5. **Do not all walk the same aisle.** The assignments in `research/` split the floor three ways.
6. **Write the notes the same evening.** Notes written on the flight home are a fraction of what
   you saw. Budget 45 minutes each night.

## Photographs

Posters and booths are fine and teams are usually pleased to be asked. **Ask before photographing
people, and ask before photographing anything that may be unpublished** — some teams are sitting on
a manuscript. "May I photograph this?" also opens the conversation that gets you the mechanism,
which is what you came for.

For each team shoot three frames: the poster wide, the one figure that matters, and something with
the team name legible — then the photos label themselves later.

## Publishing

GitHub Pages, from `main`. Keep the repo private; the Pages site inherits that.
