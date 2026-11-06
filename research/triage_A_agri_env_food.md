---
layout: doc
title: Agriculture, bioremediation, conservation, food
eyebrow: Triage · slice A
section: Triage
description: 146 teams in the villages closest to ReLeaf, read from their published abstracts.
---

**Teams read:** 146 (40 Agriculture, 50 Bioremediation, 1 Climate Crisis, 22 Conservation, 33 Food & Nutrition)
**Source:** `research/_slices/A_agri_env_food.json` — abstracts only, no wiki fetched.
**For:** Gabriel (G, wet lab), Chars (Ch, wet lab), Timmy (T, PI / dry lab)

## Overview

The crowded ground is the whole-cell reporter biosensor. Somewhere near half this slice is "sensor protein + promoter + colour or fluorescence", applied to heavy metals (Benenden, GeorgetownPrep, HongKong-JSS, VIS, YK Pao, SMS-Shenzhen), PFAS (Berlin, HS-Kentucky, LYON, WageningenUR, UTArlington), food spoilage amines (Aalto-Helsinki, RooseveltSATX, Chalmers, KhanLab-BayArea, China SUIS GB) and fungal VOCs (CAU-China, OTIA-Hangzhou, NTHU, URV-Tarragona). Differentiation inside that crowd now comes almost entirely from the reader hardware and the calibration, not the circuit — Saarland reports fluorescein-equivalent units, CAU-China built a ~$15 phone fluorimeter, HUBU-WUHAN walks a detection limit from 100 µM down to 0.05 µM and names the engineering step behind each decade.

What is rare is actuation and control. Only a handful of teams close a loop: NTHU Taiwan's three-tank CathaBench with automated sensing, SHSID's ESP32 sense–decide–respond drought rig, Toronto's low-cost open-source bioreactors, Saarland's signal-seeking boat. Optogenetic *control* (as opposed to light *sensing*) is almost absent — Guelph, ECUST, BNUZH-China's light-triggered suicide switch, Nanjing-China's light kill switch, UM-Macau's LOV AND-gate, and that is nearly the list. This matters: ReLeaf's green/red CcaSR switch has very little company in this slice, which is both an opening and a warning that judges will have few reference points.

Three things surprised me. First, ACC deaminase shows up independently in three teams — TUS-Japan (surface-displayed on *B. subtilis*), UPF-Barcelona (secreted from *B. subtilis* with γ-PGA) and Zhulu-Union (fused to a cell-penetrating peptide, enzyme-only product). Two of those are ReLeaf's enzyme on ReLeaf's chassis. Second, *B. subtilis* secretion — GEMS's weakest link — is being attempted by at least six teams here (BJWZ-China, TUS-Japan, UPF-Barcelona, SZ-SHD, Hongwen School, DNHS-SanDiego-Ca), and Texas reports a secretion *failure* in E. coli (YebF left the cargo in the membrane) that is more useful than most successes. Third, a different team is also called ReLeaf (WLSA-ShanghaiAcademy, lignocellulose to bioethanol) — worth knowing before someone congratulates the wrong booth.

Honest reporting is itself a differentiator and clusters in a few teams: Oakridge-HYD states its clones are unsequenced and its response flat below 200 µM, Chalmers-Gothenburg states its biosensor was non-functional, LYON reports the scaffold defluorinated the wrong substrate, GeorgetownPrep labels simulations separately from data. These are the booths where the *how* is actually extractable.

## Priority targets

21 entries. More than 18 because the brief requires every close competitor (bioreactor, plant-protection microbe, optogenetics, *B. subtilis* chassis, ACC deaminase, plant stress) to appear even when otherwise weak; the remaining teams in those categories are flagged "competitor" in the full table.

### TUS-Japan — Soilmate (Agriculture, JPN, undergrad)
- Buckets: C
- Why it's worth the walk: This is ReLeaf's enzyme on ReLeaf's chassis for ReLeaf's problem — ACC deaminase on engineered *Bacillus subtilis* to relieve salt-induced ethylene stress. Their route is different and arguably smarter: rather than secreting into the medium they display the enzyme on the surface using a Twin-arginine translocation signal plus a LysM domain anchor, and they explicitly frame it as avoiding modification of the crop. The Tat pathway choice is a direct answer to the question GEMS has not solved.
- Relevance to ReLeaf/GEMS: direct competitor — and the single most useful technique-to-borrow booth in the slice.
- Ask at the booth: Why Tat rather than Sec for ACCD, and did you compare them side by side? How did you quantify that the displayed enzyme is active and still anchored — units per OD, or per cell? What fraction ends up anchored versus released into the medium, and how did you measure the split?
- Assign: G

### UPF-Barcelona — Vinesys (Agriculture, ESP, undergrad)
- Buckets: C, M
- Why it's worth the walk: *B. subtilis* colonising vine roots, overexpressing γ-PGA for water retention *and* ACC deaminase — plus the most interesting control logic in the slice: a two-factor gate combining an osmotic stress promoter with a salt-dependent intein that only splices when intracellular K⁺ rises, so the protein is functional only when both agree. They also report the gate does not work yet: candidate intein HutMCM2 activates at 1.5 M salt while the chassis only reaches 600–725 mM, and lowering it was attempted in silico.
- Relevance to ReLeaf/GEMS: direct competitor, and an alternative to light as the conditional trigger. ReLeaf should be able to say why light beats an osmotic/intein AND-gate.
- Ask at the booth: How did you measure intracellular K⁺ at 600–725 mM external salt, and what instrument? What did the in-silico threshold-lowering actually change in the intein, and was any variant tested at the bench? What ACCD activity assay did you use, and what did the no-drought control give?
- Assign: Ch

### BJWZ-China — Tree Guard (Agriculture, CHN, high-school)
- Buckets: C
- Why it's worth the walk: Engineered *B. subtilis* that continuously secretes a LysM₃-chitinase fusion inside a living peach tree — continuous secretion of a multi-domain protein from this chassis, in planta, which is exactly the gap in ReLeaf. They also claim laboratory confirmation of hyphal inhibition, so there should be a real assay behind it.
- Relevance to ReLeaf/GEMS: direct competitor on chassis and on secretion; technique to borrow on fusion-protein secretion.
- Ask at the booth: Which secretion signal carries the LysM₃-Cat fusion out, and what titre do you get in supernatant? How did you confirm the secreted protein is intact rather than cleaved at the linker? Did you ever recover the strain from the tree after colonisation, and at what density?
- Assign: G

### SZ-SHD — S.A.F.E. Crops (Agriculture, CHN, high-school)
- Buckets: C
- Why it's worth the walk: *B. subtilis* 168Δ4 as a frost-resilient endophyte with a low-temperature-responsive circuit that autonomously controls synthesis and release of antifreeze proteins or protective sugars. Same architecture as ReLeaf — environmental input, conditional protectant production, release to the plant — with temperature as the input instead of light, and the Δ4 protease-deficient strain is a chassis choice GEMS should have an opinion on.
- Relevance to ReLeaf/GEMS: direct competitor. The abstract is all future tense, so expect little data; the chassis and delivery-route choices are the prize.
- Ask at the booth: Why 168Δ4 specifically — which proteases, and did it measurably improve product recovery? Seed soaking versus foliar spray: which gave colonisation, and how did you count it? What is the cold promoter, and what is its leakiness at normal growth temperature?
- Assign: Ch

### BNUZH-China — PineProtector (Conservation, CHN, undergrad)
- Buckets: C
- Why it's worth the walk: *B. subtilis* colonising pine trunks, expressing a protease under a phenolic-acid-induced system plus a Bt toxin — and a KillerRed-based suicide switch where leaving the tree means sunlight exposure, ROS production and death. That is a light-triggered biocontainment design, which is both ReLeaf's weak spot (kill switches) and ReLeaf's own actuator (light) used in the opposite direction.
- Relevance to ReLeaf/GEMS: direct competitor; the kill switch is the main thing to take home.
- Ask at the booth: What light dose kills, and how did you show it does not fire inside the tree — what irradiance did you measure in the trunk? What is the escape rate, i.e. survivors per 10⁸ cells after illumination? Is the phenolic-acid induction system actually tree-specific, or does it fire in soil too?
- Assign: Ch

### NTHU Taiwan — CatharSys (Bioremediation, TWN, undergrad)
- Buckets: C, H
- Why it's worth the walk: Engineered industrial *B. subtilis* in a moving bed biofilm reactor, and they built CathaBench, a three-tank laboratory reactor with automated sensing and control, plus three layers of biosafety measures. This is the closest hardware analogue to ReLeaf in the slice: same chassis, same reactor-plus-instrumentation posture, and a Taiwanese team at a semiconductor-wastewater problem.
- Relevance to ReLeaf/GEMS: direct competitor and benchmark for the bioreactor build.
- Ask at the booth: What sensors are on CathaBench, and what does the control loop actually actuate — aeration, feed, both? How did you calibrate them and how often do they drift? What are the three biosafety layers, and which one would fail first? What was the cost and lead time for the three-tank build?
- Assign: T

### ECUST — The Great Wall (Agriculture, CHN, undergrad)
- Buckets: C, H, M
- Why it's worth the walk: Light-programmable bacteria using LOV–CheZ fusions for protein-level control of motility — regulation at the protein rather than the transcriptional level, which is a different lever from CcaSR. Three variants built, best candidate gave larger swimming halos under blue light than in darkness, and they wrote bacterial tracking software plus an agent-based model. They also built an illuminated screw immersion device, so there is real illumination hardware to inspect.
- Relevance to ReLeaf/GEMS: direct competitor on optogenetics; technique to borrow on light-delivery hardware. Treat the modelled "42.7% greater antigen transport" as a simulation output, not a measurement — the abstract says the model predicted it.
- Ask at the booth: How do you specify and verify the light dose in the immersion device — irradiance at the vessel wall, and how uniform? What was the pulse schedule, and did you test it experimentally or only in the agent-based model? What calibrated the agent-based model's parameters?
- Assign: G

### Guelph — Lumifert (Agriculture, CAN, undergrad)
- Buckets: C, S
- Why it's worth the walk: A duckweed-plus-*Gluconacetobacter* consortium accumulating N and P under optogenetic regulation, produced on-site at the farm, with an explicit commercialisation argument and ongoing industry consultation. Optogenetic control of a nutrient pathway in a two-organism system is a harder control problem than ReLeaf's single chassis.
- Relevance to ReLeaf/GEMS: competitor on optogenetics; new direction on the commercialisation / continued-R&D bucket the advisor's brief asks about.
- Ask at the booth: Which optogenetic system, and how do you get light into a duckweed-bacteria culture at depth? How do you keep the consortium ratio stable, and what do you measure to know it has drifted? What did industry consultation change about the design, concretely?
- Assign: G

### Ionis-Paris — NEWT (Agriculture, FRA, undergrad)
- Buckets: C
- Why it's worth the walk: Closed-loop hydroponics is the deployment setting, which is ReLeaf's setting. They engineer *Pseudomonas putida* to release lytic enzymes only on recognition of *Pythium* cell-wall biomarkers, via a two-component system with a biomarker-binding module — a conditional release design driven by a pathogen signal rather than an operator's light. They state the open question honestly: whether the enzyme expresses and stays bioactive.
- Relevance to ReLeaf/GEMS: direct competitor on conditional protectant release into a recirculating system.
- Ask at the booth: What is the biomarker-binding module built from, and what is the detection threshold in µg/mL of cell-wall material? Is the enzyme released or retained, and what is the mechanism? In a recirculating loop, how do you stop the signal from accumulating and latching the system on?
- Assign: Ch

### Hongwen School — BrewXOS (Food & Nutrition, CHN, high-school)
- Buckets: C, H
- Why it's worth the walk: *B. subtilis* engineered with three complementary enzymes so that enzyme production and substrate conversion happen in one fermentation with no purified enzyme added — a secretion result with an actual number attached (control-adjusted 107.9 mg xylose equivalents per gram dry substrate at 12 h). They also built a compact fermentation-monitoring prototype.
- Relevance to ReLeaf/GEMS: technique to borrow — multi-enzyme co-secretion from *B. subtilis* with a quantified yield, which is what ReLeaf cannot yet report.
- Ask at the booth: Which signal peptides for the three enzymes, and did you screen a library or pick from literature? How did you partition yield between the three enzymes? What does the monitoring prototype measure, and what did it cost?
- Assign: G

### Texas — Engineering Probiotics to Combat Malnutrition (Food & Nutrition, USA, high-school)
- Buckets: C, M, S
- Why it's worth the walk: They fused an enzyme to YebF expecting secretion and got membrane localisation instead — then confirmed the localisation and showed the activity anyway. A documented, diagnosed secretion failure with the assays that caught it is worth more to GEMS than a dozen successful constructs. They also ran MICOM community metabolic modelling and report a negative finding from it.
- Relevance to ReLeaf/GEMS: none-but-instructive, sharply so — this is the failure mode ReLeaf is most likely to hit.
- Ask at the booth: How did you establish membrane localisation rather than secretion — fractionation, microscopy, both? What would you try next for actual export? Why did you trust the activity assay once the location was wrong?
- Assign: G

### Latvia-Riga — TRACE (Food & Nutrition, LVA, undergrad)
- Buckets: C, H
- Why it's worth the walk: *B. subtilis* spore display, fusing passenger proteins to native CotB, CotC and CotG coat proteins with sfGFP as a size placeholder for nanobodies — and an Fe-EDTA-ethanol protocol that renders the spores non-viable before release. Surface display plus a chemical inactivation step is a biocontainment route GEMS has not considered, and the shelf-stable-bioreagent framing is a different product shape.
- Relevance to ReLeaf/GEMS: technique to borrow on display and on non-genetic containment.
- Ask at the booth: Which coat protein tolerated the largest passenger, and what was the display efficiency per spore? What does the Fe-EDTA-ethanol step do to the displayed protein's activity? How did you verify non-viability — plating sensitivity, and at what detection floor?
- Assign: Ch

### SHSID — PlantGuard (Agriculture, CHN, high-school)
- Buckets: C, H
- Why it's worth the walk: A drought system with two modules — a chromoprotein alert in gel beads and in-situ cellulose/hyaluronic acid synthesis for rhizosphere water retention — wired to ADRS hardware with in-situ sensing, ESP32 edge computing, wireless networking and a mobile app, described as a closed sense–decide–respond loop. That is ReLeaf's control architecture applied to plant stress by a high-school team.
- Relevance to ReLeaf/GEMS: direct competitor on closed-loop architecture; benchmark for what the loop has to demonstrate to be believed.
- Ask at the booth: What does the loop actually decide and actuate — is the biology in the loop or only the irrigation? Which sensors, and how are they calibrated against a reference? Has the loop ever run unattended, and for how long?
- Assign: T

### Toronto — PetaBite (Bioremediation, CAN, overgrad)
- Buckets: H, M
- Why it's worth the walk: They searched 27.3 million public sequencing datasets to build a 300-million-homolog enzyme database, trained a protein language model on it for candidate ranking, screen with a high-throughput copper-release assay, and test in low-cost open-source bioreactors. Both halves of Timmy's remit — a real ML pipeline and an open-hardware reactor — in one booth, with an explicit benchmark-beating goal.
- Relevance to ReLeaf/GEMS: technique to borrow (open-source bioreactor design, PLM ranking) and benchmark for the dry-lab claim ladder.
- Ask at the booth: What is the bill of materials and per-unit cost of the open-source bioreactor, and what does it instrument? How did you validate the language model's ranking — what is the hit rate of top-ranked candidates in the copper-release screen? How do you keep a 300M-sequence database from being dominated by near-duplicates?
- Assign: T

### Saarland — OWLET (Bioremediation, DEU, overgrad)
- Buckets: H, M
- Why it's worth the walk: A low-cost 3D-printed fluorescence reader that pumps water into a six-well strip, measures fluorescence and converts it into fluorescein-equivalent units, validated against fluorescein standards and GFP-expressing E. coli — then mounted on a boat that steers toward rising signals and geotags readings. Converting raw counts into a traceable standard unit is precisely the measurement rigour GEMS wants, and it is the same problem as ReLeaf's OD600 photodiode calibration.
- Relevance to ReLeaf/GEMS: technique to borrow — calibration methodology, almost directly transferable to the OD600 channel.
- Ask at the booth: What is the full calibration chain from ADC counts to fluorescein-equivalent units, and what residual error do you report? How do you handle turbidity and temperature drift on a moving boat? What did the optical path cost, and which LED/filter/photodiode combination?
- Assign: T

### CAU-China — Fungal Sentinel (Food & Nutrition, CHN, undergrad)
- Buckets: H, M
- Why it's worth the walk: OptiX, a phone-based fluorimeter costing about $15 in materials, which resolves the reporter spectrum from RAW camera images down to nanomolar levels. Spectral unmixing from a phone RAW file is a cheaper and more interesting measurement route than a dedicated photodiode chain. The living half — a rewired yeast mating pathway with an olfactory receptor and a Gpa1–Gαolf chimera — is a clean example of repurposing native signalling.
- Relevance to ReLeaf/GEMS: technique to borrow on low-cost optical measurement; the nanomolar claim from a phone camera is the one to probe.
- Ask at the booth: How do you get from a phone RAW image to a concentration — what is the unmixing model and what calibrator? What is the limit of detection with error bars, and how many replicates? How much does ambient light and phone model change the answer?
- Assign: Ch

### GeorgetownPrep — SENTINEL-LOOP (Bioremediation, USA, high-school)
- Buckets: H, M, S
- Why it's worth the walk: They verify their own biosensors with an orthogonal method — bismuth-film screen-printed electrodes and square-wave anodic stripping voltammetry — and their open-source analysis pipeline carries provenance labels that separate simulated from experimental evidence. They also state plainly that wet-lab validation was incomplete at Wiki Freeze. That combination of independent verification plus provenance labelling is the measurement-rigour practice GEMS should copy outright.
- Relevance to ReLeaf/GEMS: technique to borrow — the provenance convention and the orthogonal-verification habit.
- Ask at the booth: How do the biosensor and the voltammetry numbers compare where both exist, and how large is the disagreement? How is the provenance label implemented in the pipeline — metadata, file naming, something enforced? What did the electrode workflow cost per measurement?
- Assign: T

### UW-Poland — HYPPE (Agriculture, POL, overgrad)
- Buckets: M
- Why it's worth the walk: A foundation model of fungal promoters trained from scratch on a corpus they assembled — 2,702 RNA-seq runs requantified into 2,332 comparable samples across twenty genomes, every growth condition hand-annotated — encoding promoters as discrete hierarchical symbols so sequences can be read, edited and decoded back to DNA, reaching rank correlation 0.689 on a test split opened once. "Opened once" is the most disciplined ML statement in the slice.
- Relevance to ReLeaf/GEMS: technique to borrow on dry-lab discipline; benchmark for how a model claim should be stated. Their pHYPPE two-reporter ratio cancels copy number and nuclear context — directly applicable to ReLeaf's MEFL-style calibration.
- Ask at the booth: How did you build the held-out split so that opening it once was meaningful, and what would have counted as failure? Why discrete hierarchical symbols rather than a dense embedding — what did you lose? How does the two-reporter ratio behave when the two reporters have different maturation times?
- Assign: T

### Jilin-China — NutriTrace (Food & Nutrition, CHN, undergrad)
- Buckets: M, H
- Why it's worth the walk: A living DNA recorder in *Komagataella phaffii*: stress-responsive promoters driving site-specific recombinases so each cell permanently writes its own stress history, read out by fluorescence after the run, with cells in alginate beads for recovery. Their stated motive is exactly ReLeaf's blind spot — that tank-average probes hide local gradients of nutrients, oxygen and metabolites. This is a way to validate a digital twin against what cells actually experienced, not what the probe at one port saw.
- Relevance to ReLeaf/GEMS: new direction — the strongest idea in the slice for the digital twin and the AI sensor layer.
- Ask at the booth: What is the recorder's dynamic range and time resolution — can you tell a brief severe excursion from a long mild one? What is the false-switching rate with no stress? How do you map a bead's recorded state back to a position in the tank?
- Assign: T

### RUM-UPRM — R-DetoX 2.5 (Bioremediation, PRI, undergrad)
- Buckets: C, H
- Why it's worth the walk: A real reactor claim with a real measurement behind it — 85% extracellular substrate reduction in 20 hours by HPLC with abiotic controls unchanged — plus SeBiS 2.0, a proposed serial bioreactor integrating growth, continuous treatment, biomass recirculation and byproduct mitigation. Biomass recirculation in a serial train is a configuration ReLeaf's closed loop has not addressed.
- Relevance to ReLeaf/GEMS: competitor on the bioreactor; benchmark for how to report a reactor result. Note they label SeBiS 2.0 as proposed, not built.
- Ask at the booth: Was the 85% measured in a reactor or in batch flasks, and at what working volume? What drove the recirculation design — washout calculations, and at what dilution rate? Which byproducts forced the mitigation stage?
- Assign: G

### NU Boston — Soil Shield (Conservation, USA, undergrad)
- Buckets: C, M
- Why it's worth the walk: Three things GEMS needs, in one project: a salicylate-dependent kill switch characterised by flow cytometry rather than plate counts, biodegradable alginate beads as the soil delivery vehicle, and a purpose-built soil chamber to test in dry post-wildfire conditions. Field validation on real substrate plus a quantified kill switch is the combination ReLeaf lacks.
- Relevance to ReLeaf/GEMS: technique to borrow on both biocontainment measurement and field-condition testing.
- Ask at the booth: What does flow cytometry tell you about the kill switch that plating does not, and what escape frequency did you get? How is the soil chamber controlled — water potential, temperature — and how reproducible is it? Did the alginate beads change survival, and over how many days?
- Assign: Ch

## Full triage table

| Team | Title | Buckets | Score 0–3 | One-line hook |
|---|---|---|---|---|
| Aiglon College | UVitis: Improving the Vitality of Grapes | C | 1 | Fusion protein as "double-sided tape" anchoring kaolin to grape cuticle; only fluorescence shown, no retention data. |
| Alicante University | 1,3-Dimethoxybenzene against nematodes | C, M | 1 | Whole pathway still future tense ("will assess"); docking only. |
| BIT-China | HERBAL — rapid bacterial assay for licorice | H, M, S | 2 | Compact reader integrating mixing, temperature control and optics, plus open-source BIO-NET network simulator. |
| BJWZ-China | Tree Guard — B. subtilis LysM₃-ChiA + RNAi | C | 3 | **Competitor**: continuous secretion of a multi-domain fusion from B. subtilis inside a living tree. |
| BWYA | Flowever | C, S | 2 | 159.02 mg/L melatonin and a product built from filtered supernatant to dodge purification cost. |
| CCA-SanDiego | PestiSense | M | 1 | Cell-free FRET aptasensor; admits variability and has no LOD yet. |
| CCU-Taiwan | NoFold — L-limonene vs rice leafroller | C, M, S | 2 | Taiwan pest problem; deliberately sprays extracted product so nothing engineered is released. |
| City-of-London-UK | Vinalysis — smoke-tainted grapes | C, H | 2 | Riboswitch plus DesX conformational change for two phenols in one vineyard-side test. |
| CUHK-Shenzhen | Plant SOS — hormone biosensor complex | M | 2 | **Competitor** (plant stress): SA/JA/ABA triple sensor with a cross-hormone interaction model — the stress input ReLeaf lacks. |
| ECUST | The Great Wall — light-programmable microrobots | C, H, M | 3 | **Competitor**: LOV–CheZ protein-level light control, tracking software, agent-based model, illuminated hardware. |
| GeorgiaState | REDAlert — rice blast early warning | C | 2 | Chimeric receptor drives betalain so the plant turns red pre-symptom; still at protoplast transfection. |
| Guelph | Lumifert | C, S | 3 | **Competitor** (optogenetics): optogenetically regulated duckweed–bacteria fertilizer with a commercialisation argument. |
| HainanU-YZ-China | GreenShield miRNA biopesticide | C, M | 2 | miR393 claimed to act on both pathogen and plant immunity; Hill-XGBoost induction-kinetics model. |
| HIA-Taiwan | AiyUReady — methanol biosensor | C, M, S | 2 | Taiwanese crop, farmer-shaped design, and unusually honest that calibration and field validation are missing. |
| HongKong-JSS | MerMAID — MerR mercury assay | H, M | 2 | Screened 10+ variants to an LOD below WHO limits; alginate encapsulation tested in spiked soil matrices. |
| HSET-China | Silicon Shield | C | 1 | **Competitor** (plant stress): silicon transporters for multi-stress resistance; no data in the abstract. |
| INHA-U Korea | Backyard Guardian — SA-responsive dual biocontrol | C, M | 3 | **Competitor**: measured rhizosphere SA to check the circuit's operating range; T6SS/T1SS effector export. |
| Institut-Le-Rosey-CH | AURA — inline mastitis sensor | H | 2 | FET miRNA sensor built into milking machines with reference electrodes for sample-to-sample calibration. |
| Ionis-Paris | NEWT — hydroponic Pythium biocontrol | C | 3 | **Competitor**: conditional lytic-enzyme release in a closed-loop hydroponic system. |
| MammothEdu-East | BioCall | C | 2 | Five-volatile semiochemical platform to recruit predators rather than kill pests; honest about assembly difficulties. |
| Muenster-University | P.A.C. Immunity | C, S | 2 | Engineered immune receptors as an open-source resistance-design platform; "we design them" is an overreaching claim for the data shown. |
| NACIS SHANGHAI | MelanoShield | C, H, M | 3 | 0.05 g/L melanin blocks 95.4% of UV; ESM-2 workflow with a measured 14.5% titre gain and two hardware prototypes. |
| NEFU-China | AAAgri | C, M | 2 | Waste lipids as sole carbon source to chrysanthemic acid with AI-assisted enzyme engineering; no titres given. |
| NJTECH-CHINA-A | NJF26 zearalenone detox | M | 2 | Computational screen to mutant to calcium-alginate beads that held activity over four uses. |
| NKU-China | Field Detective — nematode yeast biosensor | C, M, S | 2 | GPR2 localisation confirmed, plus dual-channel and economic models that ask when testing is worth it. |
| OTIA-Hangzhou | Detect the Invisible | M | 2 | Four promoters driving luxCDABE, read combinatorially to stage the infection; self-illuminating, no substrate. |
| Oxford | NECTAR | C | 1 | 322-character abstract claims extensive in vivo RNAi validation with nothing to check it against. |
| Rochester | VERDANT | C | 2 | **Competitor**: methyl-salicylate-inducible VIP3A — plant-stress-triggered protectant production, ReLeaf's logic with a chemical input. |
| SHSD | BnDREB1C overexpression | C | 1 | 4.4–11.9-fold expression and earlier flowering, but in Arabidopsis, not rapeseed. |
| SHSID | PlantGuard — dual-module drought system | C, H | 3 | **Competitor**: ESP32 closed sense–decide–respond loop around a drought alert and water-retention polymers. |
| Sorbonne University | PureGrain-Zen | M | 2 | Aptamer plus toehold switch with their own Apta2Switch-Studio software; full pathway still unvalidated, and they say so. |
| SRE-Shanghai | Fishfriend | C | 1 | 1,8-cineole in yeast; every antibacterial effect is "expected", none measured. |
| SZ-SHD | S.A.F.E. Crops — antifreeze endophytes | C | 3 | **Competitor**: B. subtilis 168Δ4 endophyte with a cold-responsive circuit releasing frost protectants. |
| SZU-China | Ciricide — cirRNA pesticide platform | C, M | 3 | Dumbbell circular RNA in minicells that lyse in the pathogen's own acidic microenvironment — smart triggered release. |
| TUS-Japan | Soilmate — surface-displayed ACC deaminase | C | 3 | **Competitor**: ReLeaf's enzyme on ReLeaf's chassis, delivered by Tat secretion plus a LysM anchor. |
| UPF-Barcelona | Vinesys | C, M | 3 | **Competitor**: B. subtilis with ACCD and γ-PGA behind an osmotic-promoter AND salt-dependent-intein gate that admittedly misfires. |
| URV-Tarragona | SCENTINEL — OBP volatile biosensor | H, M | 3 | Custom Python scoring picked the odorant-binding proteins; immobilised on nanoporous alumina with an optical shift readout. |
| UW-Poland | HYPPE — fungal promoter foundation model | M | 3 | Hand-annotated 2,332-sample corpus, decodable symbolic promoter encoding, and a test split opened exactly once. |
| VUB-Brussels | VUBzzz | C, H, M | 3 | YOLO vision gate confirms the species before the trap exposes it to the spore-loaded nanofibers. |
| Worldshaper-Shanghai | SweetCycle | C, M | 2 | SrUGT76G1 T284I gave ~42% higher Reb M, screened in hairy roots; content is "estimated", not assayed. |
| Aix-Marseille | Antibio Wars | C | 2 | Five laccases purified and immobilised two different ways to compare as a degrading filter. |
| Beijing-HS | Uric acid in aquaculture wastewater | C | 1 | Alginate beads for a fluidized-bed reactor and a detect-plus-degrade cascade; no results. |
| Benenden | AQUA SHIELD | H, M | 3 | ESM-2 screen over 2,700 substitutions, cross-reactivity explicitly tested, and a 3D-printed sampling drone. |
| Berlin | Sense PFASt | M | 2 | Three parallel sensing architectures compared rather than one bet; the sub-hour, low-cost claim is unsupported so far. |
| BYHS-CHN | BioShield — asbestos surface treatment | S | 2 | Seven-condition reporter comparison and an unusually candid list of what remains undemonstrated. |
| DTU-Denmark | ByeByeBlade | C, M | 3 | 37 enzymes expressed, 7 active on a resin model compound, inconclusive results labelled inconclusive, plus an LCA. |
| GeorgetownPrep | SENTINEL-LOOP | H, M, S | 3 | Orthogonal voltammetric verification of its own biosensor and provenance labels separating simulation from data. |
| Harvard | MlrAcle on the Charles | C | 1 | Encapsulin-packaged MlrA keyed to bloom detection; entirely intent, no results. |
| HK League | Bioprinted ElectroMining | H | 2 | Syringe bioprinter and BioPrintCAD plus an operated six-stage bead cartridge; carefully separates built from proposed. |
| HK-PLKNPLC | Engineered lanmodulin for terbium | M | 3 | Three variants designed off distances measured in a 1.01 Å structure; a Tyr antenna gives reagent-free luminescent readout. |
| HS-Kentucky | Dual-approach PFAS detection | M | 2 | 50+ mutants through LigandMPNN/AF3/GROMACS/OpenMM, with docking deltas presented as the result. |
| HUBU-WUHAN | Naphthalene degradation + SA biosensing | H, M | 3 | LOD walked 100 → 20 → 0.2 → 0.05 µM with the specific engineering step named for each decade, plus a portable device and app. |
| IISER-TVM | SANJEEVANI | C | 1 | Moss as the chassis because haploid editing shows immediately — the chassis rationale is the takeaway. |
| KCIS | ReBile — waste bile to UDCA | C, M | 1 | Cofactor regeneration and computational enzyme optimisation, no numbers reported. |
| Keystone | Coffee wastewater microflora | C | 2 | Two co-immobilised yeasts with a division of labour, plus a kill switch for containment. |
| LYON | BioThetis — TFA binders | C, M, S | 3 | Reports the scaffold defluorinated DFA but not TFA, and pivoted from degradation to capture — a documented negative. |
| Macquarie-Australia | MagniMO | C, S | 2 | Magnetite biomineralisation for magnetic cell recovery — physical retrieval instead of a kill switch. |
| Madrid-UCM | rePhlow | C | 2 | **Competitor** (bioreactor): alginate-encapsulated cells in a modular bioreactor explicitly to prevent release. |
| MCA-SWIS | Pesticide cleanup | C | 1 | Four recombinant plasmids built for sensing and biotransformation; construction only, no assays. |
| Missouri-Rolla | Metlock | M | 2 | AHL–LuxR quorum control over a surface-displayed metal-binding fusion, with reproducibility as the stated goal. |
| MPAYF-USA | Environd — 2,4-DNT | C | 1 | YhaJ–PyqjF biosensor plus a reconstructed degradation pathway; "efficient mineralization" is asserted, not shown. |
| NTHU Taiwan | CatharSys — B. subtilis TMAH in MBBR | C, H | 3 | **Competitor**: engineered B. subtilis in a three-tank instrumented reactor they built, with three biosafety layers. |
| NWU-CHINA | HYDRA | C | 2 | Seven specialised A. niger strains with real-wastewater removal percentages and 5% NaCl tolerance. |
| NYU-Abu-Dhabi | DuneLock | C | 2 | γ-PGA biofilm stickiness plus carbonic anhydrase crystal precipitation to lock sand grains together. |
| NYU-New-York | PeBet | H | 1 | **Competitor** (bioreactor): a tabletop bioreactor to hold PETase-expressing cells at optimum; no results, no design detail. |
| Oakridge-HYD | BioChronos — DNA exposure recorder | M, S | 3 | States 2.08-fold only at 1000 µM, flat below 200 µM, clones unsequenced, memory modules unvalidated — then revised the model. |
| RUM-UPRM | R-DetoX 2.5 | C, H | 3 | **Competitor** (bioreactor): 85% removal in 20 h by HPLC with abiotic controls, plus a serial reactor with biomass recirculation. |
| Saarland | OWLET | H, M | 3 | 3D-printed fluorescence reader calibrated to fluorescein-equivalent units and mounted on a signal-seeking boat. |
| SCAU-China | CyanoGuard | H, M | 3 | Seven-day environmental model for exceedance risk, fluorescence calibration, and a monitoring boat with a drone release module. |
| SMS-Shenzhen | kisMET | C, S | 2 | Chassis secretes cellulose and metal-binding peptides simultaneously; TEA and LCA, plus a deliberately narrowed role. |
| Squirrel-Beijing | pNProbe | C | 1 | Targeting the bioavailable fraction rather than total concentration is the only distinctive element. |
| Stockholm | T.I.D.E | C | 2 | Three-vector sense–report–degrade platform with an attempted receptor respecification for BPA alternatives. |
| THIS-China | ArtemiSilence | C | 1 | Mesoporous silica nanoparticles delivering RNAi into standing plants; all future tense. |
| TJI-Seoul | CPS Cycle | C | 2 | Non-living recombinant-enzyme material; CotA activity still detectable after incorporation into the citrus-soil matrix. |
| TJUSLS-China | PUReCycle | M | 3 | ~30M metagenomic sequences screened to 19 candidates; double mutant active at both 50 and 60 °C on a standardised UPLC assay. |
| Toronto | PetaBite | H, M | 3 | 300M-homolog database, protein language model ranking, copper-release screen, low-cost open-source bioreactors. |
| UCL | SHELLter | C, S | 2 | Chitinase–deacetylase fusion converts shellfish waste into a cisplatin-capturing cartridge at the point of excretion. |
| UMaryland | AEGIS | C | 0 | A problem statement with no mechanism, no chassis detail and no results. |
| UNIMI-IT | M.A.N.Z.O.N.I. | M | 3 | Retargetable λ-Red integrative overexpressor with 1–5 tandem promoters, built to avoid plasmid burden. |
| UOregon | AquaFlock | C | 2 | Cyanophycin accumulation triggers flocculation so the biomass harvests itself and returns as fertilizer. |
| UOttawa | Nulfur | M | 3 | Graded Golden Gate promoter blocks, a 24-member tuning library, and a modelled consortium to relieve metabolic burden. |
| UTArlington-TexasUSA | ForNever Chemicals | C | 1 | Four-gene defluorination with intracellular fluoride export; the aim is stated as an open question. |
| UVU-Utah | GreenARC | C | 1 | AtzA-F in Chlamydomonas, chosen for large-construct tolerance and environmental resilience. |
| VIS | Cadture | M | 2 | Uses the *loss* of GFP signal as the capture readout and tracked it in real time — a neat inverse assay. |
| VIT-Vellore | Ammonia capture via GlnA–PPK2 | C | 2 | Glutamine synthetase coupled to a PPK2 ATP-regeneration cycle to fix gaseous ammonia into glutamine. |
| WageningenUR | Triton | C, H, M | 3 | **Competitor** (bioreactor): de novo binder on cellulose beads concentrates, a dehalogenase bioreactor destroys, a riboswitch monitors. |
| WestviewHS SanDiego | Project PEARL | C | 1 | Three surface-displayed proteins tested colorimetrically; hedged throughout ("hopefully", "wanted to see"). |
| WLSA-ShanghaiAcademy | ReLeaf — waste to bioethanol | C | 2 | Name collision with GEMS's own project; five enzyme activities actually measured in P. pastoris. |
| Worldshaper-Hangzhou | AirNova | C | 1 | Humidity-activated enzyme spray with no enzymes named and no degradation data. |
| YK Pao | The Golden Cicada's Escape | C, H | 2 | Gas-vesicle buoyancy plus Ag43 aggregation so loaded cells self-collect as floating rafts. |
| Cela | — | — | ? | no abstract — check wiki |
| ABOA | Benzophe-none | C | 2 | Tests two steps of a newly proposed pathway and says outright that experimental data on it is very limited. |
| Alma | Com-BAT-ing White Nose Syndrome | C | 1 | Secreted protease inhibitors against a fungal virulence factor; proposal stage. |
| Athens | ApiconIASIS | C, S | 2 | Mined prophages for endolysins, showed OD drop on the pathogen and no effect on two gut commensals — specificity actually tested. |
| BNUZH-China | PineProtector | C | 3 | **Competitor**: B. subtilis in pine trunks with a KillerRed light-triggered suicide switch. |
| DNHS-SanDiego-Ca | Coral endolysin probiotic | C | 2 | **Competitor** (B. subtilis): secretes an endolysin under an ROS-responsive promoter, with a validated low-stress control. |
| GHCIS | ToeholdX | H, M | 2 | Computationally designed toehold switches plus RPA on paper for equipment-free multiplexed readout. |
| GYHS | ReefBond | C | 2 | Mussel-adhesive domains fused to a mineralisation peptide; "strong underwater adhesion" is preliminary and unquantified. |
| HG-Tokyo | R.E.I.G.N. | C | 2 | Fuses royalisin to a phage endolysin for two attack mechanisms against a spore-forming pathogen. |
| Hong Kong-CUHK | BeeTrix | C | 2 | Living bacteria as self-renewing factories inside the hive to beat the short half-life of the active compound. |
| IISER-Kolkata | FINS | C, M | 3 | Holin/endolysin kill switch, deterministic *and* stochastic circuit modelling with sensitivity and error analysis, plus UV tanks for escapees. |
| IL Tech Chicago | SynBeeGee | C | 2 | Engineers the host's native gut symbiont rather than the host or the environment. |
| Lambert-GA | SWARM | C, H, M | 3 | De novo minibinder claimed as the first validated anti-iflavirus binder at <1% of industry cost, plus PRINCE software and Vapor-X hardware. |
| Nanjing-China | PhosArmor | C | 2 | **Competitor** (optogenetics): a light-controlled kill switch, explicitly flagged as pending functional validation. |
| NU Boston | Soil Shield | C, M | 3 | Flow-cytometry-characterised kill switch, alginate bead delivery, and a purpose-built dry-soil chamber. |
| NWAFU-China | AMPlify | M, S | 3 | TAM-Flow generative model made 10,000 peptides; 7 went to MD and in vitro, with hemolysis and cytotoxicity feeding back. |
| Peking | TermiTox | C | 2 | Yeast bait spread by trophallaxis, with hypoxia- and acetate-responsive promoters as the containment layer. |
| RDFZ-China | GlacierGuard | C | 1 | Bacterial cellulose as a glacier blanket; the water-retention mechanism is asserted, not measured. |
| REC-CHENNAI | THULIR | C | 2 | **Competitor** (plant stress): engineered LEA proteins with a cell-penetrating peptide delivered into seed embryos without touching the genome. |
| SarvBiome | — | — | ? | no abstract — check wiki |
| Shanghai-city | Sentinel of Light Pollution | C | 1 | Light-pollution biosensor on the argument that electronics lack biological relevance; 398 characters, no mechanism. |
| UNILausanne | Detect, Disarm, Defend | C, H | 3 | Field-validated LAMP with a portable incubator they built, plus a measured dsRNA yield gain from four flanking terminators. |
| UZurich | SeisMIC | C, M | 2 | Directed evolution for cold adaptation with a reported shorter lag phase; carbonic anhydrase results left open. |
| Aalto-Helsinki | DAHLIA | C, H | 2 | Two-enzyme cascade on a strip, each enzyme fused to a cellulose-binding module to self-immobilise. |
| Anatolia College-GR | Chlorella iron bioavailability | C | 1 | Boosts vitamin C to raise non-heme iron absorption; in-vitro digestion assessment still planned. |
| BOKU-Vienna | Algaeneering | C, S | 2 | States that the folate transformation is unconfirmed and that stakeholders pushed them toward trust and acceptance work. |
| Bonn | PotyGuard⁺ | C, M | 3 | **Competitor** (plant stress): split proteins with intein and inhibitory peptide cages turn viral protease activity into a programmable output in planta. |
| Cataverse-Beijing | Cerium MOF nanozyme detection | H | 2 | Phage receptor-binding proteins on magnetic beads plus a nanozyme and a phone app — mostly chemistry, not synbio. |
| Cataverse-Shanghai | Novel plant proteins | C | 1 | Three storage proteins expressed in P. pastoris for plant-based meat texture; no results. |
| CAU-China | Fungal Sentinel | H, M | 3 | OptiX, a ~$15 phone fluorimeter resolving the reporter spectrum from RAW images to nanomolar levels. |
| Chalmers-Gothenburg | CHYMERA | M | 3 | Reports the biosensor was non-functional under the tested conditions and localises the receptors to vacuole and ER — a clean failure analysis. |
| China SUIS GB | Fish Spoilage Biosensor | C, H | 2 | Two-strain relay with a cold-inducible promoter for 0–4 °C operation, immobilised in a dual-layer gas-permeable device. |
| DEPU | Acrylamide dual-enzyme degradation | C | 2 | Uses LEA peptides to raise thermostability for high-temperature food processing — an unusual stabilisation route. |
| HKSSC | Waste-to-watt | C, S | 2 | Removes a preservative that inhibits downstream digesters; 16 characterised parts and a structured IHP framework. |
| Hongwen School | BrewXOS | C, H | 3 | B. subtilis co-secretes three enzymes in one fermentation for 107.9 mg/g yield, plus a compact fermentation monitor. |
| Jilin-China | NutriTrace — living DNA recorder | M, H | 3 | Recombinase-based per-cell stress history in a fermenter, aimed squarely at the gradients a single probe averages away. |
| JZIB-QDHS | SULT-targeting functional foods | M | 1 | Docking plus Chou-Talalay synergy analysis; weight-loss framing is the weakest claim in the slice. |
| KCIS-Xiugang-Taipei | Herculyeast | C, S | 2 | Taiwan ASF policy deadline as the driver; MFα1 prepro-leader for secretion, product uses enzymes not live cells. |
| KhanLab-BayArea | The Cluck is Ticking | C, M | 2 | Chromoprotein cadaverine sensor paired with a model that would replace static expiry dates with live ones. |
| Kyoto | OiLipase | C, M | 3 | A protease that acts at the oil–water interface and self-inactivates on a timed split-protease mechanism — unusually elegant control. |
| Latvia-Riga | TRACE | C, H | 3 | B. subtilis spore display on CotB/CotC/CotG plus an Fe-EDTA-ethanol step that inactivates spores before release. |
| NPSI Singapore | ProbioRegulon | C, S | 2 | Redesigned the peptide partly to get around a patent on the natural sequence; food-grade probiotic as the delivery route. |
| NTHU | AeroSense | H, M | 3 | Four-channel optical reader built and tested against fluorescent standards, with transport/optical modelling and a fly-inspired decoding network. |
| NYCU-Taiwan | BITE | H, M | 2 | Magnetic enrichment, Cas12a recognition and a G4–hemin colorimetric readout chained into one visual test. |
| Okinawa | pHlex | M | 2 | Built an AI platform to predict sequences conferring acid resistance in phages; engineering still ahead of them. |
| OUC-China | Pro-TPSP | M | 2 | Tet-On plus uORF translational control to tune polysaccharide molecular weight; preliminary MW increase reported. |
| RooseveltSATX | Amisense | C | 1 | Colour-changing histamine biosensor; 667 characters with no construct detail. |
| SCU-China | DunaTerp | C, M | 3 | Interchangeable enzyme cassettes off a β-carotene hub in D. salina, with a salt-dependent mazE-mazF switch as biocontainment. |
| SHSBNU-China | BLISS | C, H, M | 2 | Active inclusion bodies with SAP and adapter tags to simplify recovery, plus a palm-sized microscope for outreach. |
| SSBS | Low-GI resistant starch | C | 1 | Three-enzyme hydrolysis/elongation/debranching cascade evaluated by SEM and RS content. |
| Tec-Chihuahua | BruSafe | C, S | 2 | MS2 virus-like particle carrying mRNA, argued as DIVA-compatible and cold-chain tolerant against named failings of current vaccines. |
| Texas | Engineering probiotics vs malnutrition | C, M, S | 3 | YebF fusion unexpectedly stayed in the membrane — a diagnosed secretion failure, plus a negative modelling finding. |
| Thailand-RIS | BetterSweet | C | 1 | Mogroside pathway steps moved into N. benthamiana as a faster production host. |
| UFRGS-Brazil | 2,4-Detector | H, M | 3 | Repurposes a metal-responsive regulator pair for a herbicide, cell-free for containment, with field-reading hardware and a reporting forum. |
| UM-Macau | Guarding the Fridge | M | 2 | **Competitor** (optogenetics): a blue-light LOV input as the second term of an AND gate for viability discrimination. |
| Zhulu-Union | Persephone | C | 3 | **Competitor** (ACC deaminase): ACCD and MnSOD fused to the BP100 cell-penetrating peptide, delayed banana yellowing ~3 days versus 1-MCP. |

**Note on the input file:** `research/_slices/A_agri_env_food.json` was readable at the start of this session but the `research/_slices/` directory is now empty on disk. The triage above was completed from the full abstract text captured during the first read, so all 146 teams are covered, but the slice file itself should be regenerated or restored.
