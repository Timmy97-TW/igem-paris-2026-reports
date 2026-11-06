# Triage B — Biomanufacturing, Foundational Advance, Software & AI, Space

Source: `research/_slices/B_mfg_foundational_sw_space.json` — 135 entries read (Biomanufacturing 56, Foundational Advance 47, Space 17, Software & AI 15). The slice file was missing when this triage was written; it was regenerated from `data/teams_2026.json` by taking all **accepted** teams in those four villages (138 records in those villages minus Arizona and FHSW, withdrawn, and OPTIC-8, disqualified), which reproduces the stated count of 135 exactly. Built from abstracts only — nothing fetched from the web. 11 entries carry no abstract at all; one more (`Example`, FRA) is a placeholder joke entry.

Theme codes follow `_BRIEF.md`: **C** novel concepts & interdisciplinary · **H** hardware & automation · **M** computation/modelling/data · **S** science for good.

Patterns across the slice, each tied to teams:

1. **Everyone is doing "AI-guided protein engineering" and almost nobody reports a prospective win.** NJTech-China (5.6-fold TPH7 mutant), NFLSHS-CHINA (+113% crocetin), SZSAIS-BaoAn (K406S, +52.3%), NNU-China, NBJF, Yucai-SZ, HK-Joint-School and NEBS-VCA all run the same loop: structure/docking/language-model screen, then confirm a handful of variants. Only NJU-China (ATLAS) names a specific previously unannotated protein — UniProt M5AW86 — confirmed active prospectively, and only Tsinghua-A and Al-Nahrain-IRAQ state plainly where their predictors are not yet validated. This is the slice's dominant genre and its weakest point; ask what the hit rate was, not what the best hit was.
2. **Bioreactors appear as scale-up vessels, not as instrumented systems.** Jiangnan-China (4.93 g/L in a 5 L bioreactor over 120 h) and NJTech-China (20.0 g/L in 5 L) are the real fermentation benchmarks here, but neither describes in-line sensing. The teams that actually built a vessel are Mingdao (benchtop fermentor), AshesiGhana (grinder plus reactor, with a GolS biosensor used as an in-line efficiency readout) and KAUST-KSA (a bioreactor designed for space conditions). ReLeaf's instrumented closed loop has very little direct competition in this slice.
3. **Closed-loop control is being reinvented as intracellular control.** KAIST Korea (RATAtouille), NUS-Singapore (ORCHID), Patras-Med (ICHNOS) and USTC (TEMPO) all argue that the controller should sit inside the cell — autoregulatory circuits, multiplexed stress biosensors plus ML, a fluorescent timer that reconstructs past stress, a clock-and-counter. ReLeaf puts the controller outside, in the light panel and the sensor stream. That contrast is the single best conversation available in this slice.
4. **Optogenetics is used to switch physical state far more than to switch product.** McGill (light-triggered yeast aggregation for harvest), NAU-CHINA (light-driven condensate formation), WHU-China (light-induced dedifferentiation), NUS-SPS (light-controlled biofilm thinning) and YHA-HWFLA (a portable blue-light activator paired with a light-protective spray) use light for handling; only HiZJU-China (light-controlled CRISPRi balancing growth against fuel synthesis) and NMU-China use it the way ReLeaf does, to time production.
5. **Biocontainment is the slice's best-developed answer to a question we are weak on, and the numbers are uneven.** XMU-China reports a self-targeting circuit reducing survival by up to five orders of magnitude; Virginia (ChronoContain) and USTC build time-triggered lysis rather than environment-triggered; Tongji China, HiZJU-China, UCSC and Uni-Padua-IT each bolt a containment module onto an environmental release. Most state the mechanism and not the escape frequency.
6. **B. subtilis and plant-stress work are both present but thin and scattered.** B. subtilis appears as chassis in Tongji China, NUS-SPS and KAUST-KSA, as a parts standard in Concordia-Montreal (extending SubtiToolKit), and only as a gene donor in UCNZ (xynA) and HK-Joint-School (BslA). Plant-side work is HAS (engineered E. coli lowering ABA/IAA in roots), BGCFullerton (protecting mycorrhizal fungi against regolith oxidative stress) and Marburg (inducible chloroplast expression). Secretion — our stated weakness — is addressed head-on only by UCNZ (YebF fusion), Thailand-XCLASB (glycosylated secreted hydrolase in Pichia) and HK-Joint-School, which says outright that its two-layer design exists to get past secretion limits.

---

## Priority targets

22 entries. Nine of them are in the same space as ReLeaf and are marked `same space` whether or not they are otherwise strong; GEMS-Taiwan's own entry (6072) is in the full table but is not a target. `Assign` splits the floor between **G** (Gabriel, wet lab), **Ch** (Chars, wet lab) and **T** (Timmy, PI/dry lab) so nobody walks the same poster twice.

### NUS-Singapore — ORCHID: Observation of Real-time Cellular Health and Intracellular Dynamics for Predictive Biomanufacturing (Biomanufacturing, SGP, undergrad)
- Themes: M, C
- Worth the walk: they build modular multiplexed intracellular biosensors that report several stress signals at once during a culture, and feed that high-dimensional stream into ML to predict titre/rate/yield before the process degrades. Their stated argument is exactly ours — current practice is reactive, adjusting conditions after the damage shows — but their sensor lives inside the cell rather than in the vessel wall. The abstract claims predictive insight without naming a single prediction horizon, accuracy figure or test fermentation, so the claim is at the same maturity as our own anomaly layer.
- Relevance: benchmark
- Ask at the poster: How many signals do you read simultaneously, and how did you demonstrate they are orthogonal rather than all reporting general stress? What is the earliest lead time at which the model called a drop in yield, and on how many independent runs? When the model was wrong, was it a false alarm or a miss, and what did you change?
- Assign: T

### KAIST Korea — RATAtouille: Multi-Layer Genetic Circuits for Dynamic Metabolic Control (Biomanufacturing, KOR, undergrad)
- Themes: C, M
- Worth the walk: the framing is the sharpest in the slice — performance is decided by *when* genes switch on, not which are present — and they build input modules reading precursor level, population density and an external signal into one shared output format, then use hierarchical logic so the delay through each layer splits the pathway in time. Their test case is lutein, where a promiscuous cyclase feeds both product and byproduct and cannot be deleted, so timing is the only lever. No titres, fold changes or delay measurements appear in the abstract.
- Relevance: benchmark
- Ask at the poster: What delay does each logic layer actually add in minutes, and how did you measure it? How did you normalise three different input modules to one output format without the strong input swamping the weak ones? What is the lutein-to-byproduct ratio with timed versus constitutive expression?
- Assign: Ch

### William-and-Mary — BRO[K]EN: Building Resilient Optimized Engineered Networks (Foundational Advance, USA, undergrad)
- Themes: M, S
- Worth the walk: they run longitudinal experiments on four engineered circuits in laboratory and simulated environmental conditions and try to DETECT, MITIGATE and PREDICT circuit failure from mutation, selection, burden and stress, with multitiered functional and molecular measurements. This is the failure-analysis discipline our digital twin and sentinel layer assume but have never tested — our longest record is one 434 h run.
- Relevance: technique to borrow
- Ask at the poster: How long did the longitudinal runs last in generations, and what fraction of each population had lost function by the end? Which failure mode did your ML model predict worst? What measurement told you a circuit was degrading before the output did?
- Assign: T

### Patras-Med — ICHNOS: Trace the Invisible (Foundational Advance, GRC, undergrad)
- Themes: M, C
- Worth the walk: a stress-responsive sensor drives a TetR circuit and a tandem fluorescent timer, so the cell records the intensity and timing of a stress event that has since faded; ICHNOS-Vail then estimates the past event from image analysis plus a model. That is our two-event finding in the 434 h run solved biologically instead of statistically — a record written by the cells rather than inferred from a photodiode trace.
- Relevance: technique to borrow
- Ask at the poster: Over what window back in time can you still resolve an event, and what sets that limit? How do you separate a long weak stress from a short strong one when both leave the same timer ratio? What did the model get wrong on a known stress you applied deliberately?
- Assign: T

### AshesiGhana — Recovering Gold from E-Waste / SynMine (Biomanufacturing, GHA, overgrad)
- Themes: H, C, S
- Worth the walk: the only entry here that reports building the whole physical chain — grinder and reactor included — around a biological process, with a GolS-based biosensor reporting gold concentration in solution as an in-line efficiency metric, and a chain-level model. They also claim selectivity for Au(I) while copper, nickel, zinc and tin stay in solution, and that engagement with Agbogbloshie workers, miners and Ghana's EPA shaped design decisions. Numbers for recovery per pass are absent.
- Relevance: technique to borrow
- Ask at the poster: How did you calibrate the GolS biosensor into a concentration rather than a relative signal, and against what reference method? What is the recovery per cycle and how far does it fall after re-use of cells? Which design decision did the EPA conversation actually change?
- Assign: Ch

### ULethbridge — Utilizing MOSMAGE to engineer optimized microbial chassis (Biomanufacturing, CAN, overgrad)
- Themes: H, M
- Worth the walk: MOSMAGE is a low-cost modular open-source hardware platform built from consumer-grade components to automate MAGE workflows, with integrated thermal, fluidics, electroporation and spectrophotometric modules. The spectrophotometric module is the same engineering problem as our in-line OD600 on low-cost photodiodes, and the fluidics-plus-thermal integration is the closest thing in the slice to an open lab-automation stack. The validation is stated in the future tense ("we will measure" TAL production), so the hardware may be further along than the biology.
- Relevance: technique to borrow
- Ask at the poster: Which consumer parts did you use for the spectrophotometric module, and what is its noise floor and drift over a day? How do you keep electroporation voltages reproducible with consumer-grade components? What did the platform cost in total, and which module failed most often?
- Assign: T

### FHS-China — ProLac (Foundational Advance, CHN, high-school) 
- Themes: H, M, S
- Worth the walk: an explicitly observation-first project — they characterise an existing acid- and oxygen-tolerant probiotic instead of building a new strain, run a COBRApy manM knockout simulation on a published genome-scale model, and, because their wet-lab readouts were failing, built their own multifunctional fluorometer. They also released an open-source campus biology map. The self-built instrument driven by a measurement problem is the useful part; the in silico knockout is never tested in the strain they characterised.
- Relevance: technique to borrow
- Ask at the poster: What was failing in the commercial readout that made you build the fluorometer, and how did you calibrate it? What are its detection limit and linear range against a reference instrument? Why did you not test the manM knockout prediction in CICC 6109?
- Assign: T

### EPFL — OrbitAl (Space, CHE, undergrad)
- Themes: H, M, C
- Worth the walk: two things we need. First a designed protein that folds around Al3+, an ion with no natural biological sensor, plus engineered E. coli reporters that distinguish Fe(III) from Fe(II) — speciation, not just concentration. Second, and more important for us, mass spectrometry quantifies the same samples so the biological signal always has a chemical reference. They also built a balloon-borne sampler that keeps stratospheric aerosols intact and uncontaminated to the lab.
- Relevance: technique to borrow
- Ask at the poster: How closely did the biosensor track the MS numbers, and where did the two diverge? What is the cross-reactivity of the Al3+ binder against the other metals in a real aerosol sample? How did you show the sampler itself was not the source of the aluminium?
- Assign: T

### Uni-Padua-IT — C.O.S.M.I.C. (Space, ITA, undergrad)
- Themes: H, M, C
- Worth the walk: they engineered a non-invasive acoustic oxygen sensor so the vessel is never opened, and it quantifies dissolved and gaseous fractions separately — directly relevant to our in-line sensing and to the TMP/OD readings that sat below the sensor floor in the 0902 run. They also wrote ReTIsigner, an open-source codon-optimisation tool for non-standard chassis, and designed an inducible kill switch justified against planetary-protection guidelines. The chassis is Nostoc sp. PCC 7120 with pprA from D. radiodurans added for radiation tolerance.
- Relevance: technique to borrow
- Ask at the poster: How does the acoustic sensor separate the dissolved from the gaseous fraction, and what did you calibrate it against? What is its resolution and drift over a multi-day run? What escape frequency does the kill switch achieve, and which guideline clause set the target?
- Assign: T

### Virginia — ChronoContain (Foundational Advance, USA, undergrad)
- Themes: C
- Worth the walk: they argue that environment-triggered biocontainment fails precisely when real-world conditions change, and replace the trigger with a clock: a modular timed kill switch in E. coli using phage holin–antiholin systems to lyse the cells after a defined interval. For an organism we intend to release to plants through a membrane, a timer is a far more defensible containment story than a chemical or nutrient trigger. No escape frequency or timing spread is reported.
- Relevance: technique to borrow
- Ask at the poster: How wide is the distribution of lysis times across a population, and what sets that spread? What escape frequency did you measure, and over how many generations? What happens to the timer if growth stalls, as it does in a feed-limited culture?
- Assign: G

### XMU-China — STING: Small TnpB-based Innovative Nuclease toolkit (Foundational Advance, CHN, undergrad)
- Themes: M, C
- Worth the walk: the one containment claim in the slice with a number attached — a self-targeting biocontainment circuit reducing bacterial survival by up to five orders of magnitude. The rest is a compact TnpB editing toolkit with per-host efficiency ranges honestly spread (4.2–100% deletion in E. coli, 30–44% in P. putida), structure-guided evolution to five noncanonical TAMs, and registered core parts. Reporting a range that starts at 4.2% rather than a best case is unusual here.
- Relevance: technique to borrow
- Ask at the poster: How did you measure the five-log survival reduction — plating, or a longer selection — and over what time? What made deletion efficiency vary from 4.2% to 100% across loci? Would the self-targeting circuit work in a Gram-positive host like B. subtilis?
- Assign: G

### UCSC — AMPiary (Biomanufacturing, USA, undergrad)
- Themes: M, C
- Worth the walk: a modular antimicrobial-peptide manufacturing pipeline — a standardised AMP expression plasmid plus AMPexchange, which swaps the AMP gene without full reassembly — in E. coli hosts carrying a dual-mechanism biosafety system, with a ML genetic algorithm (reVAMP) that improves on assay data. They designed, synthesised, purified and validated one novel peptide, apiarin. This is the BoPep4 problem solved as a platform: peptide production plus containment plus a design loop closed with real assay data.
- Relevance: technique to borrow
- Ask at the poster: How do you keep an antimicrobial peptide from killing its own producer, and what yield do you get per litre? Did reVAMP's predictions improve measurably after the first round of assay data, and by how much? What are the two mechanisms in the biosafety system, and were they tested together?
- Assign: Ch

### Korea-HS — Melano Shield (Biomanufacturing, KOR, high-school)
- Themes: C, S
- Worth the walk: not our field at all, and the best measurement writing in the slice. They report 419 mg/L dried pigment, matching a commercial Sepia melanin standard to within 0.5% in log-linear absorbance slope, an empty-vector control giving none, mass loss of 3.06 ± 0.73% against 9.36 ± 1.82% untreated oak and 3.67 ± 0.73% for a commercial product — then state plainly that at three specimens per condition they match that product and do not beat it, and that this is to their knowledge the first fire test of a bacterially produced melanin coating. A high-school team is modelling the reporting standard we want for our own chlorophyll and DNPH numbers.
- Relevance: none but instructive
- Ask at the poster: How did you decide three specimens per condition was enough to claim parity but not superiority? Why the log-linear absorbance slope rather than absolute absorbance as the comparison to the standard? What would it take to show you beat the commercial product?
- Assign: Ch

### Tongji China — Virock: Intelligent Microbial Self-Healing Concrete System (Biomanufacturing, CHN, undergrad)
- Themes: C, S
- Worth the walk: `same space` — B. subtilis as chassis, expressing mineralisation-assisting proteins for calcium carbonate deposition in concrete cracks, with a biosafety containment system that restricts survival outside the intended environment via cell lysis and growth inhibition. Same chassis, same problem of a deliberately released engineered organism, different application. The abstract is written almost entirely in intent ("designs", "we expect") with no deposition rates or crack-closure data.
- Relevance: same space
- Ask at the poster: Which mineralisation-assisting proteins, and are they secreted or surface-displayed in B. subtilis? How much crack width did you actually close, and over how long? Does the containment system fire inside concrete, where nutrients are scarce anyway?
- Assign: G

### NUS-SPS — AEGIS: Astro-Engineered Guardian of Interface Surfaces (Space, SGP, undergrad)
- Themes: C, H
- Worth the walk: `same space` and the closest architectural neighbour in the slice — a non-pathogenic B. subtilis strain with an optogenetic switch wired to biofilm-thinning genes, so external light controls biofilm on demand, used to competitively exclude biofilm-forming E. coli in the ISS water processor. Light in, B. subtilis phenotype out, in a flow system: that is ReLeaf's control loop pointed at a different output. Ecological competition as the mitigation strategy is a genuinely different idea from killing the incumbent.
- Relevance: same space
- Ask at the poster: Which optogenetic system did you use in B. subtilis, and what light intensity and wavelength reach the cells through the vessel wall? How did you quantify competitive exclusion — biomass, CFU, or imaging? Does the light switch still work once a biofilm is thick enough to shade itself?
- Assign: G

### KAUST-KSA — SHIHAB (Space, SAU, overgrad)
- Themes: C, H
- Worth the walk: `same space` — B. subtilis is one of three chassis (with S. cerevisiae and P. pastoris), engineered for radiation and stress resilience, and the whole thing is integrated into a custom-designed bioreactor built for operation under space conditions for autonomous on-demand protein production. On-demand production in a purpose-built vessel is our exact claim; theirs is for astronauts rather than plants. The abstract names no therapeutic, no titre, and no bioreactor specification, so the vessel may be a design rather than a build.
- Relevance: same space
- Ask at the poster: Is the bioreactor built, and what is its working volume, mixing method and sensor set? Which of the three chassis won on resilience, and against what dose? What does "autonomous" mean in practice — does anything close a loop, or is it a fixed programme?
- Assign: Ch

### Concordia-Montreal — BiblioTK: Engineering a Gram-Positive Toolkit System (Foundational Advance, CAN, overgrad)
- Themes: M, C
- Worth the walk: `same space` by parts rather than application — they extend SubtiToolKit, the B. subtilis Golden Gate standard, with Part E (modular, independently exchangeable origins of replication inside STK's grammar) and pGRAMLIN, a split-marker shuttle vector that couples antibiotic selection to correct recircularisation to raise transformation efficiency in Gram-positive hosts. Transformation efficiency and vector choice are our routine friction. Project Bookmark, their statistical promoter-finder, is a secondary tool.
- Relevance: same space
- Ask at the poster: What transformation efficiency does pGRAMLIN give in B. subtilis compared with your previous vector, and in what units? Which origins did you put in Part E and what copy numbers do they give? Did any Part E origin break STK compatibility?
- Assign: G

### HAS — AstroFlora: Solutions for Plant Growth in Microgravity (Space, CHN, high-school)
- Themes: C, H
- Worth the walk: `same space` — an engineered E. coli plant probiotic that reduces excessive ABA and IAA accumulation in roots under microgravity stress, plus Floraspin, their own hardware for simulating microgravity plant growth, verified as promoting Arabidopsis germination. Lowering a stress hormone in the root with a bacterium is structurally the same intervention as our ACC deaminase lowering ethylene; they have a plant readout, which is a weakness of ours. How a bacterium reduces plant hormone levels is not explained in the abstract.
- Relevance: same space
- Ask at the poster: By what mechanism does the bacterium lower root ABA and IAA — degradation, uptake, or signalling? What germination and root-length numbers did you get, with how many plants per condition? How do you know Floraspin's rotation is simulating microgravity rather than just stirring the medium?
- Assign: Ch

### BGCFullerton — MycoVela: Protecting Mycorrhizal Fungi for Future Space Agriculture (Space, USA, high-school)
- Themes: C, S
- Worth the walk: `same space` — a cell-free antioxidant carrier that protects Rhizophagus irregularis spores and hyphae from oxidative stress in lunar regolith simulant, using pyomelanin made by heterologous HPPD expression in E. coli and a catalase designed for activity in regolith. They state the Earth application plainly: better AMF symbiosis raises crop yield. Honest about status — the experiments are "proposed", with named controls (pyomelanin carrier vs ascorbic acid vs carrier-only vs stress-only) and named readouts (spore viability, hyphal growth, oxidative-stress response). A designed control set with no data yet is still a usable template.
- Relevance: same space
- Ask at the poster: Has any of the proposed comparison been run, and what did the carrier-only control show? Why pyomelanin over ascorbic acid, given ascorbic acid is your comparator? What makes the catalase "optimized for regolith" — pH, metal tolerance, something else?
- Assign: Ch

### HiZJU-China — UNICO-fuel (Space, CHN, undergrad)
- Themes: C, M
- Worth the walk: `same space` on the mechanism that matters most to us — a light-controlled CRISPRi system used to dynamically balance cell growth against product synthesis in engineered P. pastoris, with auxotrophic containment, suicide switches and radiation protection on top. Growth-versus-production is the trade-off our green-light schedule BO is optimising, and they attack it with light and repression rather than scheduling. The upstream photocatalytic CO2-to-methanol step is chemistry, not biology, and the abstract gives no titre for epi-isozizaene.
- Relevance: same space
- Ask at the poster: What does light-controlled CRISPRi do to the growth rate when it is on, and how fast does repression relax when the light goes off? How did you choose the switching point between growth and production? What is the EPI titre, and is it from methanol or from glucose controls?
- Assign: G

### YHA-HWFLA — Fel d1 Eraser (Biomanufacturing, CHN, high-school)
- Themes: H, C
- Worth the walk: `same space` by mechanism — precise optogenetic regulation of enzyme activity, shipped as a product pair: a light-protective spray plus a portable blue-light activator. That is our light panel reduced to a consumer handheld, and they also claim to have established standardised parts for heterologous protease expression. Light-controlled enzyme activity in a formulation the user triggers is a delivery idea we have not considered for the membrane release step. No degradation percentages, intensities or exposure times appear.
- Relevance: same space
- Ask at the poster: What is in the activator — wavelength, intensity, exposure time — and how did you pick them? Is the light controlling expression or the activity of already-made protease? How much Fel d 1 is degraded, measured how, and what happens on a surface in ambient light?
- Assign: Ch

### Mingdao — Ethanol from Paper Waste (Biomanufacturing, TWN, high-school)
- Themes: H, M, C
- Worth the walk: `same space` as a vessel-building team, and Taiwanese, so worth the contact regardless. They built a benchtop fermentor, ran one-pot simultaneous saccharification and fermentation with cellulase, β-glucosidase and Zymomonas mobilis on plastic-lined paper containers, and — the part worth copying — characterised both enzymes under fermentation-compatible conditions far from their optima, then modelled the enzyme–microbe coupling. Characterising a component at the condition you will actually run it at, not at its optimum, is precisely the discipline our CcaSR induction work needed. No ethanol yield is given.
- Relevance: same space
- Ask at the poster: What did the enzyme activities drop to at fermentation conditions versus their optima? What ethanol yield per gram of container did you reach, and what limits it — enzyme, sugar inhibition, or the plastic? What does the fermentor measure in line, and what did you build it from?
- Assign: T

## Full table

All 135 entries, in slice order (Biomanufacturing, then Foundational Advance, then Software & AI, then Space; alphabetical within each).

| Team | Title | Themes | Score 0-3 | One-line hook |
|---|---|---|---|---|
| AshesiGhana | Recovering Gold from E-Waste | H C S M | 3 | Built the grinder and the reactor; a GolS biosensor reports gold concentration as an in-line efficiency metric. |
| ASIJ-Tokyo | 茶(Sa)kure-it-all | C | 1 | Dual-strain yeast with biosensor flux control and transport engineering; written entirely as aims. |
| BGI-College | BioH₂ | C M | 2 | 46.92% vs 40.20% hydrogen content, and the spent broth then grows B. subtilis for biofertiliser. |
| Bioreactor Sentinels | — | ? | ? | no abstract — check wiki |
| BUCT-China | CycloGlass | C M | 2 | 97.8% transmittance films from β-cyclodextrin host–guest pairs; ML-guided CGTase hit at 59.0% starch conversion. |
| CaptuREE | — | ? | ? | no abstract — check wiki |
| Cell Forge | — | ? | ? | no abstract — check wiki |
| Duesseldorf | Cozyme | C | 1 | Two engineered yeasts split one pathway, coordinated by a MoClo co-culture circuit; modularity asserted, not shown. |
| ESSENTIAL KOREA | EcoPatch | H C | 2 | Reports that its own alginate degradation products did nothing, and built a nanowire resistance sensor for hydrogel deformation. |
| GEMS-Taiwan | Releaf | C H M S | n/a | Our own entry. |
| HAMK | ReFab | C | 1 | Self-healing protein applied to inactivated mycelial material; one protein expressed, framing mostly philosophical. |
| HangzhouFourteenAP | Multi-enzyme and AMP system for dental plaque | C | 1 | DNase, protease and glycosidase against the biofilm matrix plus tooth-binding AMPs; no results in the abstract. |
| HI-Iceland | Making the strongest spider silk UV resistant | C | 1 | Says plainly the UV half of the engineering cycle was not finished; one silk construct appears to have expressed. |
| HK-Joint-School | FlaminGone | C M | 2 | A two-layer curli coating designed specifically to get past secretion limits, with an Arabidopsis ecotoxicity assay. |
| HSAS-China | BrewZyme | C | 2 | Quorum-quenching enzymes immobilised on a spent-coffee scaffold, with retained activity, leaching and reuse all measured. |
| IIT Bombay | BIFROST | C M | 1 | One FAS2 point mutation plus CFD for immersion cooling; the target coolant molecule has not been made yet. |
| Jiangnan-China | Yarrowia for 7-DHC | M C | 3 | 462.1 mg/L in flasks to 4.93 g/L after 120 h in a 5 L bioreactor, with enzyme-constrained modelling — the fermentation benchmark here. |
| KAIST Korea | RATAtouille | C M | 3 | Argues performance is set by when genes switch, not which; hierarchical logic splits a pathway in time. |
| Korea-HS | Melano Shield | C S | 3 | 419 mg/L pigment, 3.06 ± 0.73% mass loss, and the sentence "we match that product, not beat it". |
| MammothEdu-United | BioSonde | C M S | 2 | PETase variants stabilised for high salt and heat, an LCA that credits the TPA co-product, and a four-gate adoption plan. |
| McGill | LanTurn | C M | 2 | Light-triggered yeast aggregation to make harvesting easy — optogenetics used for handling, not for product. |
| Mingdao | Ethanol from Paper Waste | H M C | 3 | Built a benchtop fermentor and characterised both enzymes at fermentation conditions far from their optima. |
| MycoFab | — | ? | ? | no abstract — check wiki |
| NBJF | ThermoTdT | M | 1 | Deep learning for TdT thermostability with no temperature, activity or yield figure anywhere in the abstract. |
| NFLSHS-CHINA | Crocetin via CsCCD2 engineering | M C | 2 | Names zeaxanthin accumulation as the real bottleneck, then reports one mutant at +113% crocetin. |
| NJTech-China | 5-HTP via multi-scale engineering | M C | 3 | 20.0 g/L 5-HTP in a 5 L bioreactor without exogenous tryptophan, from a 5.6-fold TPH7 quadruple mutant. |
| NNU-China | Chitosanase for higher-DP COS | M C | 2 | Shifted the product profile from DP2–DP3 to DP3–DP6 and ran fed-batch at 24–26 °C with no external heating. |
| NNU-Nanjing-China | Indigo in E. coli | M C | 2 | 0.580 → 3.199 g/L via AI-designed disordered proteins forming membraneless organelles; 5.52x on their own baseline. |
| NUS-Singapore | ORCHID | M C | 3 | Multiplexed intracellular stress biosensors plus ML to predict titre/rate/yield before the process degrades. |
| Oros Biotech | — | ? | ? | no abstract — check wiki |
| OUC-Haide | Carbotex | C M | 2 | 26 g/L poly(malic acid) from lignocellulosic hydrolysate after unlocking xylose use via AraR and XlnR. |
| Phyto-X | — | ? | ? | no abstract — check wiki |
| PSI Korea | Bio Color ID | H M C | 2 | 60 optical features per tag across five LEDs and four backgrounds, with replicate tags checked for consistency. |
| RUBochum | Cat PURr | M | 1 | Enzyme discovery for aromatic carbamate cleavage via the Pythia framework; still at candidate-selection stage. |
| SCU-BSE-China | SynAmine | M C | 2 | Fusion-orientation result worth hearing: forward GGGS gave 214.20 mg/L against 118.41 reversed, so domain order beat linker choice. |
| SDU-Denmark | Shewanode | C | 2 | Overexpresses mtrCAB and omcA and destabilises the outer membrane to shed more vesicles for extracellular electron transfer. |
| SHIFTER | — | ? | ? | no abstract — check wiki |
| Squirrel-Guangzhou | Cardivit | C | 0 | Salvianic acid A in E. coli, described entirely in intent with no construct, titre or method. |
| SZSAIS-BaoAn | From Fermenter to Cold Table | M C S | 2 | 23.37 → 39.1 mg/L ergothioneine by swapping in ADO1, then +52.3% from the K406S Egt1 variant. |
| Thailand-XCLASB | Melanify | C | 2 | Secreted hydrolase glycosylated in Pichia to raise its own thermal stability — a secretion trick worth asking about. |
| Tongji China | Virock | C S | 2 | B. subtilis making calcium carbonate in concrete cracks, with lysis-and-growth-inhibition containment; all written as intent. |
| TU Delft | MOSAIC implant coatings | C M S | 2 | Elastin-like polypeptide coatings with built-in protease sites for on-demand release, plus a design tool and regulatory analysis. |
| UCNZ | NanoBrew | C M | 2 | Secretes both enzymes from E. coli by YebF fusion specifically to make scale-up easier, and simulates a one-pot bioreactor. |
| UCS-A | Tea to Bioplastic | C | 0 | Tea residue to PHB straws, with no strain, titre or pretreatment detail given. |
| UCSC | AMPiary | M C | 3 | AMP gene swapping without reassembly, dual-mechanism biosafety host, and one novel peptide actually purified and validated. |
| UESTC-China | UpPlast | C M | 2 | Ethylene glycol as sole carbon source into itaconic acid, then esterified into a DLP-printable resin monomer. |
| ULethbridge | MOSMAGE | H M | 3 | Open-source MAGE automation from consumer parts, including thermal, fluidics, electroporation and spectrophotometric modules. |
| Ulink-SZ | Chitinova | C | 1 | LPMO plus chitinase secreted from E. coli to open crystalline chitin; aims only, no yields. |
| UniCRETE | RHAea | C S | 2 | Three-stage olive-mill wastewater cascade ending in a test of whether the treated water is fit for fertigation. |
| VGA-Pinion | AstraEV | C M | 2 | Plant-derived exosome-like vesicles instead of mammalian exosomes, with a kinetic and a spatial model to find the limiting step. |
| Worldshaper-Nanjing | MUSCLE-SHIELD | C | 0 | L-carnosine in E. coli, entirely in the future tense ("we plan to engineer"). |
| YCYW-China | BioCapsule Delivery Platform | C | 1 | Reports that their recombinant laccase yield was too low and that they switched to a commercial enzyme — a usable honesty example. |
| YHA-HWFLA | Fel d1 Eraser | H C | 2 | Optogenetic control of enzyme activity shipped as a spray plus a portable blue-light activator. |
| YNU-China | RBC-membrane mitochondrial delivery | C M | 2 | Seven lipid formulations screened, hypotonic load-and-reseal, and a dye-independent mito-GFP readout at BSL-1. |
| Yucai-SZ | SpotAway | C M | 2 | Water-free xerogel activated by two drops, with two binder–enzyme fusions and four DBTL cycles reported. |
| ZJU-China | NEST | C | 1 | Silk-elastin cartilage scaffold with magnetic alignment and inflammation-responsive release; heavy on vision, light on data. |
| Austin-UTexas | RAD to the Future | C M | 2 | Golden Gate parts for Deinococcus radiodurans plus TnpB and dTnpB repression in a polyploid genome. |
| Bologna | PHAGED-IT | C | 2 | Splits a base editor across two retargeted M13 phages so two surface receptors form an AND gate; honest that parts are still in preparation. |
| CalPolySLO | Synthetic Cells | H S M | 2 | Low-cost emulsion hardware and a real-time multi-substrate PPK2 assay, with open protocols and a taught course behind them. |
| Claremont CA | Phagenomics | M C | 2 | Modelling redirected the project: the recognition step turned out to be protein–sugar, so they reconstructed ancestral depolymerases. |
| Columbia NYC | Project SENTINEL | M | 2 | Sparse autoencoders on ESM to make binder design interpretable rather than a black box, benchmarked against other architectures. |
| Concordia-Montreal | BiblioTK | M C | 3 | Extends SubtiToolKit with exchangeable origins and a split-marker vector that ties selection to correct recircularisation. |
| Duke | PACERS | C | 1 | Toehold switch upstream of gene III to stop leaky pIII in PACE; stated as aim, no evolution results. |
| DUT-China | SHUFFLE | M C | 2 | ~50% editing at tested loci from a TadDE/nCas9-NG/AlkA stack, with the editor itself evolved by EvolvePro. |
| ETH-Zurich | preCISe | M C | 2 | Bacterial nanosyringes retargeted by swapping binding domains, with cargo split across two eCISs for dual-receptor specificity. |
| Evry-Paris-Saclay | ORBIT | M C | 3 | Built all 16 ribosome plasmids and nine reporters, then reports the improvements do not transfer between architectures. |
| Example | Best year yet | — | 0 | Placeholder entry ("Maybe this is our year?") — not a real project. |
| FHS-China | ProLac | H M S | 3 | Built their own multifunctional fluorometer because the wet-lab readout was failing, and characterised an existing probiotic instead of making one. |
| Fudan | GlycoGarden | C | 1 | Programmable yeast surface glycosylation platform, described without a single glycan output or assay. |
| GTIIT-China | Self-exciting quantum dots | C M | 2 | NanoLuc fused to a CdSe-binding peptide excites biosynthesised quantum dots with an enzyme instead of a lamp. |
| Heidelberg | VOYAGE | M C S | 2 | Gas vesicles as an ultrasound interface, an ATLAS model stack, and a Fail Forward initiative about publishing setbacks. |
| HKUST | Promoter toolkit for Clostridium butyricum | C | 1 | Four sentences; a promoter set is promised and nothing is characterised in the abstract. |
| HongKong-PuiChing | CLASP | M C | 2 | Rigid CTPR backbone for nanometre-precision induced proximity, with a physics-based active-learning tool to pick geometries. |
| IITKGP | dSyPhER | C | 2 | Synthetic receptors turning TNFα or rapalog binding into programmable phosphorylation cascades in HEK293T. |
| Imperial College | reGELerate | C M | 2 | Treats prion fibrils as discrete mechanical struts, chose HET-s for its lack of polymorphism, and modelled every step. |
| JLU-CP | DigiCAT | M C | 2 | Turns a continuous metabolite signal into discrete integrase-set states, with RBS tuning and modelling to place the thresholds. |
| Keio-Japan | One Direction | C | 1 | Localises adhesion machinery to both poles of rod-shaped E. coli to control cell orientation, not just adhesion selectivity. |
| KIT | ENCORE | C M | 2 | Golden Gate system for encapsulins in yeast that splits the CDS position so shell, tag, linker and cargo swap independently. |
| Leiden | VESSL | C M | 2 | Self-assembling coiled-coil peptide scaffold for organoid vascularisation, produced three ways including cell-free. |
| Marburg | CLiPPR | C M | 2 | Synthetic PPR proteins binding engineered 5'UTRs to make chloroplast expression inducible — dynamic control in a plant. |
| Munich | Primetheus | C M | 2 | Prime editing pushed into mitochondria by importing the Cas-RT and the pegRNA separately, plus a live RNA-delivery readout. |
| NAU-CHINA | CellApp | C M | 2 | Membraneless organelles in E. coli switchable by light, temperature, pH, and intein-mediated enzyme swapping. |
| NUDT-CHINA | Ubik | M C | 2 | AI-designed artificial ubiquitin-transfer modules to bypass the natural E3 ligase bottleneck entirely. |
| Patras-Med | ICHNOS | M C | 3 | A tandem fluorescent timer plus image analysis that reconstructs a stress event after the response has faded. |
| Princeton | SymPleco | C M | 2 | Sortase-functionalised M13 phage for toxin sequestration, with macrophage digestion shown as the disposal route. |
| Queens-Canada | MOSAIC (AND-gated biosensors) | C M | 2 | Interchangeable two-component systems feeding a split T7 AND gate, offered as a toolkit for later teams. |
| Rice | DigiActivate | C M | 2 | Reports its own modest numbers honestly: 1.3, 1.7 and 1.9-fold eGFP for inducer B, A and A+B on a two-switch dCas9 array. |
| ShanghaiTech-China | MOSAIC (consortia) | H M | 2 | Cre-lox then Bxb1 recombination to set population ratios, evaluated through their own hardware and software workflow. |
| TAU-Israel | CERNAL | M C | 2 | A compiler that turns differential expression data into RNA logic circuits, validated on a PFAS biosensor and a therapeutic case. |
| Tianjin | Genome Revival | C M | 2 | Recovers a yeast lineage using a helper cell, then removes the helper chromosomes; includes a DNA watermark for lineage ID. |
| Toulouse-INSA-UT | CHIRALYS | C | 2 | Mirror-image L-DNA aptamers to evade degradation, with the mirror-life risk debate taken on explicitly. |
| Tsinghua | NucleArk | C | 1 | Phase-separated condensates for plasmid nuclear delivery into slowly dividing cells; aims only. |
| TU-Dresden | MOCHI | C | 1 | Adds an RNA-dependent RNA polymerase to make RNAi in Komagataella self-sustaining; hypothesis stated as hypothesis. |
| USTC | TEMPO | C M | 3 | Separates timekeeping from execution: oscillator CLOCK, binary DNA MEMORY, ACTUATOR, with biocontainment as one output. |
| UTDallas | SPARC | C | 2 | Protease cascade instead of transcription for speed, ending in a secreted enzyme output. |
| Utrecht | EVerse | C | 2 | SpyCatcher on the vesicle surface so one nanobody swap retargets the whole carrier; honest that transport is not yet established. |
| Vilnius-Lithuania | BMClick | C M | 2 | One modified bacterial microcompartment trimer gives either a closed cargo shell or an open cargo-holding surface. |
| Virginia | ChronoContain | C | 3 | Replaces environmental triggers with a clock: holin–antiholin lysis after a defined time, because triggers fail in the field. |
| Washington | HedgehogSense | C M | 2 | Chemically induced recruitment of an E3 ligase to a ciliary receptor, with designed miniproteins as the opposing lever. |
| WHU-China | Differphase | C M | 2 | Biases plasmid partitioning via phase separation to make daughter cells differ, with a light-driven route back to the founder state. |
| William-and-Mary | BRO[K]EN | M S | 3 | Longitudinal failure analysis on four circuits in lab and simulated field conditions — detect, mitigate and predict circuit breakdown. |
| XJTLU-China | dogmaOS | M C | 2 | Treats codon choice and tRNA pool as one co-design problem, with a model linking elongation rate to co-translational folding. |
| XMU-China | STING | M C | 3 | Deletion efficiency reported as 4.2–100%, and a self-targeting containment circuit cutting survival by up to five orders of magnitude. |
| Al-Nahrain-IRAQ | SYNOVA | M S | 2 | States in its own abstract that the kinetic engine is "not yet shown to predict real batches" — rare and useful candour. |
| BostonU | Cirrus | H M | 2 | Takes budget, owned equipment, floor plan and protocol frequency and emits a build-ready cloud-lab blueprint. |
| ChronoSplice | — | ? | ? | no abstract — check wiki |
| Denmark-GA | ECLIPSE | M | 2 | Charge scanning plus thermodynamic modelling for LOCKR peptide binders, aimed at the HRP2-deletion malaria diagnostic gap. |
| DKU | PeptiCraft | M C | 2 | 849 million sequences through nine filters with safety as a hard veto, and one construct taken to a cell-based assay. |
| EdgeSci-THU-China | ECoPI | M | 1 | Multi-agent LLM system turning literature into mechanism–effect–risk chains; no validation of any prediction. |
| HelioSynth Research | — | ? | ? | no abstract — check wiki |
| NEBS-VCA | Mechanism-guided PETase engineering | M | 2 | Two beneficial variants explained by MD and quantum chemistry, and says outright which extensions remain unvalidated. |
| NJU-China | Starase Atlas | M | 3 | Top-ranked candidate M5AW86, previously unannotated, confirmed experimentally — the only prospective hit in the slice's AI crowd. |
| Nuclex | — | ? | ? | no abstract — check wiki |
| Phage Haven | — | ? | ? | no abstract — check wiki |
| SJTU-Software | Owl-Eyezyme | M | 2 | A multi-agent virtual lab that keeps the evidence chain, including recorded failures and uncertainties, with fixed reproducible pipelines. |
| Tsinghua-A | mRNA for feline immunocastration | M | 2 | +33.1% and +42.8% mean *predicted* MRL, and says the reporter measurements left real uncertainty. |
| USP-Brazil | S(H)ARP | M C S | 2 | BGC finder plus the first Golden Gate system for Streptomyces in iGEM, with public actinobacteria collection across Brazil. |
| XJTLU-Software | AMPilot | M | 2 | AMP design workbench that keeps evidence sources and prediction limitations visible and decisions with the researcher. |
| AEI Prep-Taiwan | synPETic | C M S | 2 | Scaffolded two-enzyme PETosome depolymerising PET at 37–50 °C, measured by HPLC, with a costed pre-commercial pathway. |
| AFMU-China | NEXO | C M | 2 | Living cells kept viable inside GelMA microneedles to secrete exosomes, and states plainly it is still an in vitro prototype. |
| Barcelona-UB | Guard's Up | C | 2 | Tardigrade Dsup kept episomal so the protection can be cleared with a doxycycline pill — containment by non-integration. |
| BGCFullerton | MycoVela | C S | 2 | Protects mycorrhizal fungi against regolith oxidative stress; experiments proposed, but with named controls and readouts. |
| BIT-LIFE | Mars Magnet | M H | 2 | Reports its own ML metrics (P@20 = 1.00, R² = 0.5684) and that only two of five designed promoters tracked iron. |
| BNDS-China | OrbitColi | C | 2 | Split T7 AND gate requiring both a feeding biomarker and an oxidative-stress signal before the probiotic acts. |
| BUCT | Air2Protein | C M | 2 | Electrocatalytic CO₂-to-formate feeding a reductive glycine pathway in E. coli — chemistry and biology in series. |
| EPFL | OrbitAl | H M C | 3 | Balloon-borne sampler, a designed Al³⁺ binder, Fe(III)/Fe(II) discrimination, and MS run on the same samples as a reference. |
| HAS | AstroFlora | C H | 2 | Engineered E. coli lowering root ABA and IAA under microgravity, plus their own Floraspin rig verified on Arabidopsis. |
| HiZJU-China | UNICO-fuel | C M | 2 | Light-controlled CRISPRi used to balance growth against product synthesis, with auxotrophy and suicide switches on top. |
| KAUST-KSA | SHIHAB | C H | 2 | B. subtilis among three stress-hardened chassis inside a bioreactor designed for space; no titres or vessel specs given. |
| LZU-Northwest | Sybio-Gutweaver | C | 1 | DHICA-rich melanin for radical scavenging in the gut, with colonisation control and an arabinose safety system still at design stage. |
| NMU-China | StellaCista | C | 2 | Cyanobacteria feed sucrose to yeast, and light-controlled pathways make the yeast's flavonoids — optogenetics timing product. |
| NUS-SPS | AEGIS | C H | 3 | B. subtilis with an optogenetic switch on biofilm-thinning genes, out-competing biofilm formers instead of killing them. |
| SZU-SIAT China | Friskoli | M H | 2 | Chemotaxis to close the microbe–substrate gap, with a microfluidic rig and AI tracking; the 2.5x benefit is model-only so far. |
| UFlorida | Omni-Sensing System | M | 2 | RFdiffusion 3 and BindCraft binders against osteocalcin and PD-L1, with MD used to feed features back into the design model. |
| Uni-Padua-IT | C.O.S.M.I.C. | H M C | 3 | Non-invasive acoustic oxygen sensor that never opens the vessel, plus an open codon tool and a planetary-protection kill switch. |

Row count: 135, matching the 135 entries read.

Note on `Bioreactor Sentinels` (GBR, Biomanufacturing, id 6562): no abstract, but the team name alone puts it in our space. Someone should open its wiki before the trip rather than discover it on the floor.
