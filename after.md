---
section: After we land
title: After we land
description: How three sets of notes become three reports and one plan for 2027 — the sequence, the deadlines and what each report has to contain.
eyebrow: 17 November onward · Taipei
---

Pak's brief asks for one report per instructor. The risk is three travelogues that overlap in the
middle and miss the point at the edges. This page is the sequence that avoids that.

## The sequence

| When | What | Who |
|---|---|---|
| **Each evening in Paris** | One note per session, from the template. Forty-five minutes, before dinner | each of us |
| **Mon 16 Nov, morning** | Report skeletons: the eight tracks, what goes under each, what is missing | all three, together |
| **Within 3 days of landing** | Notes tidied and pushed. Anything still only in a notebook is lost | each of us |
| **Within 1 week** | Follow-up emails sent, before anyone forgets a face | each of us |
| **Within 2 weeks** | First draft of each report, circulated to the other two | each of us |
| **Within 3 weeks** | One cross-read: where do the three disagree? | all three |
| **Then** | Final reports to Pak, plus one combined page on what changes for 2027 | all three |

The cross-read is the step that is easy to skip and worth the most. Three people watched different
rooms with the same eight questions; where their conclusions differ, one of them is wrong, and that
is more interesting than anywhere they agree.

## What each report has to contain

Beyond whatever Pak's brief specifies, three things that only work if they are written deliberately:

**1. A mechanism, not a claim.** For every team or speaker you write about, how they did it. A
paragraph with no "how" in it is a photo caption. This is rule two of
[the brief](brief.html) and it is the whole difference between a report that is useful in 2027 and
one that is not.

**2. Marked provenance.** What you were told, what you read off a poster, and what you worked out
yourself are three different kinds of statement and they age differently. In six months this is the
difference between a usable note and a rumour. The note template has a `confidence:` field for
exactly this.

**3. What we did not see.** 452 teams were accepted and we will reach a fraction of them.
Every official session is accounted for on [the four days](schedule.html) — 48 attended and 23
given up with the reason — so the shape of what we missed is already written down. A report that
states its limits is worth more than one that implies coverage it does not have.
[Gaps](gaps.html) is where the honest version lives.

## The institutional output

The three reports are the deliverable. The thing that makes them worth writing is a fourth, shorter
document that none of us owns alone: **what changes for 2027.**

Work it from [the eight tracks](tracks.html). For each one:

- the state of the art, as seen rather than as read;
- our actual gap, named against our own numbers;
- the one change that would close it inside one cycle.

Then cut it to the three or four changes we will actually make. A list of twelve improvements is a
list of zero improvements. Candidates already visible before the trip:

- **Measurement (T1).** Our calibration is single-point and our reference channel is 32 counts wide.
  If Paris gives us a defensible calibration protocol, that is a Measurement medal criterion and a
  year of credibility.
- **Reproducibility (T8).** Four formula errors in one experiment, a 1.460× standard-concentration
  error, an OD dip that was 40% instrument. We find these by re-reading, not by process. A method
  for reading our own failures is the cheapest capability on the list.
- **Open science (T4).** Our wiki freezes in October like everyone else's. The one dropped session
  worth chasing a speaker for is about exactly this.
- **The pipeline (T7).** The 2027 cohort gets built on Pak's 52-hour research-methods class. The HS
  PI Roundtable and the recruitment and workforce workshops are three sessions aimed straight at it.

## Follow-ups

[Follow-ups](followups.html) is the list of people we owe an email and what to ask them. It is
worth being blunt about how this usually goes: **an unanswered row on that page in six months is a
conversation that produced nothing.** Send them in the first week, while they can still place your
face, and keep each one to three sentences and one question.

The known ones before we even fly: the three other teams working on ACC deaminase, TUS-Japan above
all, who put our enzyme on our chassis and hit our problem; and the speaker from
**Beyond the Hype: Synthetic Biology's Next Decade**, which is the best single fit to the dry-lab
report in the whole programme and which runs across our own team talk.

## Where this lives

Everything is in [the repository](https://github.com/Timmy97-TW/igem-paris-2026-reports) and
published from it. Notes go in `notes/`, one file per session from `notes/_TEMPLATE.md`. Reports go
in `reports/`. Synthesis across teams goes in `buckets/`, under the four themes of the brief.

After editing any data or triage file, regenerate what the site renders:

```bash
python3 tools/build_site_data.py && python3 tools/build_schedule_data.py
```
