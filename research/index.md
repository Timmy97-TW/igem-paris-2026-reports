---
layout: doc
title: Pre-trip triage
eyebrow: Before we fly
section: Triage
description: Every accepted 2026 team, read from its published abstract and ranked against the four themes.
---

Built before leaving, from the published abstracts of all **452 accepted** teams. Nothing here is an
observation — it is a reading list, so the floor time in Paris is deliberate.

Start with the [floor plan]({{ '/floor-plan.html' | relative_url }}): the {{ site.data.targets | size }} targets these four
documents produced, split between the three of us.

## The four slices

| Slice | Villages | Teams |
|---|---|---|
| [A]({{ '/research/triage_A_agri_env_food.html' | relative_url }}) | Agriculture, bioremediation, conservation, food | 146 |
| [B]({{ '/research/triage_B_mfg_foundational_sw_space.html' | relative_url }}) | Biomanufacturing, foundational advance, software &amp; AI, space | 135 |
| [C]({{ '/research/triage_C_health.html' | relative_url }}) | Therapeutics, oncology, infectious diseases | 98 |
| [D]({{ '/research/triage_D_dx_fashion_other.html' | relative_url }}) | Diagnostics, fashion &amp; cosmetics | 73 |

Every accepted team appears in exactly one of them. Teams with no published abstract are marked `?`
and need their wiki opened, or a look at the board on the day.

## What came out of it

Four things worth knowing before the floor:

- **ACC deaminase is not ours alone.** Three other teams use it, and TUS-Japan surface-displays it on
  *Bacillus subtilis* via Tat secretion with a LysM anchor — our exact enzyme, our exact chassis, and
  our exact unsolved problem.
- **Our secretion blocker has precedents.** *B. subtilis* secretion appears in at least six teams.
  Hongwen School is the only one quoting a yield; Texas and Stony Brook both document secretion
  *failures*, which are worth more to us than the successes.
- **The closest hardware analogue is Taiwanese.** NTHU Taiwan built a self-built three-tank
  instrumented reactor with three biosafety layers.
- **Another team is also called ReLeaf** — WLSA-ShanghaiAcademy, lignocellulose to bioethanol. Worth
  knowing before someone congratulates the wrong booth.

## How to read it

These are abstracts the teams wrote to sell their projects, read by a language model, not by us. A
ranking is a reason to walk over, never a finding about the work. Where a claim looked unsupported
the triage says so — those are the questions to open with.

The inputs can be rebuilt: `tools/fetch_teams.py` re-pulls the team list from the iGEM API,
`tools/make_slices.py` splits it, and `tools/build_site_data.py` regenerates what this site renders.
