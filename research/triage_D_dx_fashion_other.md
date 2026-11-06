# Triage D — Diagnostics, Fashion & Cosmetics, and unassigned teams

Source: `research/_slices/D_dx_fashion_other.json` (73 teams). Built only from the abstracts in that file; nothing was fetched from the web. Wiki links are given so each advisor can read further before or after the trip.

Slice composition: Diagnostics 45 teams (35 with abstracts, 10 abstract-less), Fashion & Cosmetics 28 teams (all with abstracts). The slice label mentions "no village assigned" teams, but every record in this file carries one of those two villages — the 10 abstract-less Diagnostics entries are the placeholder-looking ones and are listed separately at the end.

Bucket codes follow the professor's brief: **C** novel concepts & interdisciplinary, **H** hardware & automation, **M** computation/modelling/data, **S** science for good.

---

## 1. How to split this slice between three advisors

This slice is lopsided: Diagnostics is almost entirely **H** (readers, cartridges, portable kits) with a strong **M** sub-layer (crRNA/toehold/aptamer design software); Fashion & Cosmetics is almost entirely **C** (sustainable materials, art/craft/economics mash-ups) with scattered **S** (commercialisation plans, stigma work).

Suggested division of labour:

- **Advisor H (hardware/automation):** Diagnostics hall, reader-and-cartridge teams. Core list: NU-Kazakhstan, IOANNINA, IIT-Madras, Hamburg, BIT, BYU-Provo, Eton-College-UK, ASU, Labi-Taiwan. Add two Fashion teams that built their own fabrication rigs: Cornell (coaxial electrospinner) and HUST-China (controlled-atmosphere spin-coater), plus Westlake's automated blending hardware and TU Darmstadt's home-built thermophile equipment.
- **Advisor M (computation/modelling/data):** Charlotte-HS, DelNorte-SD, Puebla, Labi-Taiwan, UMA Malaga, Lorraine, Tsinghua-T, Qingdao-China, IITDelhi, BK-Denmark, SPC, NENU-China.
- **Advisor C/S (concepts, interdisciplinary, science for good):** the whole Fashion & Cosmetics hall, led by CAFA-LZU, HUST-China, Cataverse-Union, Concordia-Shanghai, QingdaoAcademy, TU Darmstadt, GreatBay-SCIE, HKUST-GZ, plus Oneonta and Puebla from Diagnostics for the community/health-equity angle.

Taiwan-relevant teams to make sure at least one advisor sees: **WIST** (TWN, Taiwan FIT screening gap, pre-registered acceptance gates), **Labi-Taiwan** (TWN, cell-free + ML), **QingdaoAcademy** (algal-bloom waste upcycling — direct analogue to Taiwan coastal green tides), **IITDelhi** (air-pollution-responsive living product), **TU Darmstadt** (textile waste, Taiwan's textile industry), **Usherbrooke** and **HKUST-GZ** (both *Bacillus subtilis*, same chassis as ReLeaf).

---

## 2. Priority tier — visit these first

| Team | Country | Village | Buckets | Why it earns a slot |
|---|---|---|---|---|
| [NU-Kazakhstan](https://2026.igem.wiki/nu-kazakhstan) | KAZ | Dx | H M S | Full chain built and named: biosensor (DAScovery) → 3D-printed smartphone reader (G-lighten) → software (ColoRisk) → a stated clinical decision rule with a threshold. The cleanest "biology to portable instrument to decision" story in the slice. |
| [IIT-Madras](https://2026.igem.wiki/iit-madras) | IND | Dx | H M | Hand-held silicon-photomultiplier luminometer they designed themselves, plus linker design by multi-objective genetic algorithm, constant-pH MD, and a reaction–diffusion transport model. Best hardware+modelling pairing here. |
| [WIST](https://2026.igem.wiki/wist) | TWN | Dx | C M | Taiwanese; ultrasound readout via gas vesicles instead of a sample; an AND gate; and — the real reason to visit — acceptance gates fixed in writing two weeks before the run, plus an openly reported OFF-state failure (fold capped at 1.31×/1.69×). Methodologically the closest team in the slice to ReLeaf's frozen-criteria practice. |
| [Charlotte-HS](https://2026.igem.wiki/charlotte-hs) | USA | Dx | M S | Three open software tools (crRNA design, plate-reader analysis, kinetic modelling), 19 Registry parts, and a published synthetic-biology book plus learning platform. High-school team out-delivering many undergrads on the M and S buckets. |
| [HKUST-GZ](https://2026.igem.wiki/hkust-gz) | CHN | F&C | C S M | Engineered *Bacillus subtilis* (ReLeaf's chassis) with an LCFA-responsive sensor, a xylose- and density-dependent biosafety switch, and a three-stage commercialisation ladder (non-viable → postbiotic → self-limiting live). The containment and regulatory reasoning is directly transferable. |
| [HUST-China (IRIS)](https://2026.igem.wiki/hust-china) | CHN | F&C | C H S | Cultural craft (Dian Cui kingfisher-feather art) replaced by cellulose-nanocrystal structural colour made from fashion waste, with a purpose-built controlled-atmosphere spin-coater. The strongest art × materials × hardware mash-up in the slice. |
| [Puebla (NEUMA)](https://2026.igem.wiki/puebla) | MEX | Dx | M S | Amplification-free dCas9 on a phase-sensitive SPR chip; Quality-by-Design model ranking which measurement to run first; and they report that whole-plasmid sequencing found dCas9 lost to a 52 bp direct repeat and that the model ruled out that mutation as the sole cause. Model-vs-data honesty worth studying. |
| [IOANNINA (LEDA)](https://2026.igem.wiki/ioannina) | GRC | Dx | C H | Radiation dosimetry reframed from "dose at the badge" to "damage in the person", two biomarkers chosen so each disambiguates the other, with a small smartphone reader and risk-level app. Clean problem-framing lesson. |
| [Concordia-Shanghai (SCOPE)](https://2026.igem.wiki/concordia-shanghai) | CHN | F&C | C S M | Life-cycle analysis against four substrates with a quantified water figure (6.3 mL per functional unit), economist-sourced product choice, and HALO — a wheelchair-mounted lab organiser co-designed with wheelchair-using scientists. Accessibility-of-the-lab work is rare. |
| [CAFA-LZU](https://2026.igem.wiki/cafa-lzu) | CHN | F&C | C | Red- and blue-light-induced yeast making linalool vs limonene — two-colour optogenetic control of product identity, run out of an art academy with curated bio-art exhibitions. Nearest neighbour to ReLeaf's green/red CcaS-CcaR light control, from an entirely different motive. |

---

## 3. Diagnostics — the H bucket in detail

Portable readers and field kits (the brief's core H target):

- [NU-Kazakhstan](https://2026.igem.wiki/nu-kazakhstan) (KAZ) — **H M S** — 3D-printed reader using an ordinary smartphone camera for fluorescence quantification; ask the per-unit cost and how they calibrated camera-to-concentration.
- [IIT-Madras](https://2026.igem.wiki/iit-madras) (IND) — **H M** — hand-held SiPM luminometer for stool luminescence. Ask about SiPM cost, dark-count handling and whether the design files are open.
- [Hamburg](https://2026.igem.wiki/hamburg) (DEU) — **H S** — LB-Cas12a + gold-nanoparticle visual point-of-care AMR test; optical sensing hardware tested, and they say the hardware design was heavily shaped by human practices. Good example of IHP actually changing a device.
- [BIT](https://2026.igem.wiki/bit) (CHN) — **H M C** — paper aptamer chip embedded in a menstrual product, custom reader with FluoroCheck image-analysis software. Unusual sample route (menstrual effluent); strong C as well.
- [IOANNINA](https://2026.igem.wiki/ioannina) (GRC) — **H C** — smartphone photographs two channels, app returns a risk level.
- [ASU](https://2026.igem.wiki/asu) (USA) — **H C** — portable kit bundling incubation control, optical sensing and software; biology novelty is using *Acinetobacter baylyi* natural competence as the detection step.
- [Eton-College-UK](https://2026.igem.wiki/eton-college-uk) (GBR) — **H C** — multiplexed electrochemical disposable cartridge for wound protease activity, with computationally designed cleavable peptides; frames wound care as measurement rather than visual judgement, and carries an NHS cost figure.
- [BYU-Provo](https://2026.igem.wiki/byu-provo) (USA) — **H S C** — dinosaur-shaped carryable allergen detector for children with automated extract/detect/clean cycling, paired to a caregiver phone. Industrial-design-led; the mental-health framing is the S hook.
- [Labi-Taiwan](https://2026.igem.wiki/labi-taiwan) (TWN) — **H M** — portable cell-free electrochemical readout plus ML-guided three-way-junction and toehold design; also a documented biomarker-selection pipeline.
- [BK-Denmark](https://2026.igem.wiki/bk-denmark) (DNK) — **H M S** — colorimetric methanol biosensor with hardware, and an ultrafiltration step to strip food colourants from the beverage sample. Note the honest negative: seven engineered PcAOX variants expressed and confirmed by Western blot, but no detectable enzymatic activity.
- [SRE-China](https://2026.igem.wiki/sre-china) (CHN) — **H C** — one-pot E-RCA + Cas12a staged purely by temperature (30 °C then 60 °C, with an ssRNA blocker that dissociates on heating); no sample purification. Elegant way to avoid fluidics.
- [UBC-Vancouver](https://2026.igem.wiki/ubc-vancouver) (CAN) — **H** — biosensors-on-a-chip bedside antibiotic susceptibility test. Abstract is thin; worth a booth visit to see whether a device exists.
- [ZZU](https://2026.igem.wiki/zzu) (CHN) — **H S** — deliberately two-format: fluorescence assay for hospitals, lateral-flow strip for community screening. Good model for "same biology, two deployment tiers".
- [Oneonta](https://2026.igem.wiki/oneonta) (USA) — **H S** — nanobody lateral-flow for cTnI and h-FABP, paired with CPR training and a survey of cardiac-emergency readiness in schools. The strongest "immediate action plus long-term tool" S story in the Diagnostics hall.
- [WUXI-DSAS](https://2026.igem.wiki/wuxi-dsas) (CHN) — **H** — whole-cell gentisic-acid biosensor normalised by a chemical creatinine assay, reported as a ratio. The normalisation discipline is the transferable part.

M-bucket Diagnostics (software, design pipelines, modelling):

- [Charlotte-HS](https://2026.igem.wiki/charlotte-hs) (USA) — three open tools; one reaction per miRNA target so collateral cleavage does not blur identity.
- [DelNorte-SD](https://2026.igem.wiki/delnorte-sd) (USA) — **M H** — two tools (Strand Analyzer for thermodynamic sequence optimisation, Cell Analyzer for automated image quantification); also a hard-won empirical constraint, a 4–6 h imaging window set by cytosolic ssRNA degradation.
- [UMA Malaga](https://2026.igem.wiki/uma-malaga) (ESP) — **M S C** — three named pillars (assay / bioinformatics / human-centred); Diana auto-generates and ranks gRNA candidates from clinical mutation input. The "question of postcode, not biology" framing is a good line for the report.
- [Lorraine University](https://2026.igem.wiki/lorraine-university) (FRA) — **M S** — molecular biosensor deliberately paired with a symptom-based ML pipeline; two evidence streams for one diagnosis.
- [Puebla](https://2026.igem.wiki/puebla) (MEX) — QbD model from plasmid to detection limit; 25 clinicians and three focus groups shaped the output format.
- [UBrawijaya Indonesia](https://2026.igem.wiki/ubrawijaya-indonesia) (IDN) — **M** — de novo computational nanobody design, then expression as an intimin fusion and a cell-cell adhesion readout.
- [UFABC-Brazil](https://2026.igem.wiki/ufabc-brazil) (BRA) — **M C** — claims the first toehold switches designed for tRNA-derived fragments; NUPACK design, cell-free and whole-cell comparison, with a candid note that the whole-cell platform performed only as a preliminary proof of concept.
- [SZPU-CHINA](https://2026.igem.wiki/szpu-china) (CHN) — **M H** — worth visiting precisely because it is a documented null result: Ste2-based constructs stayed α-factor responsive but neither gating design gave HA-dependent activation, and they say so, offering parts and iteration records rather than a deployable detector. Also built a temperature-controlled optical readout prototype.

Concept-led Diagnostics (C bucket):

- [Edinburgh](https://2026.igem.wiki/edinburgh) (GBR) — **C** — liquid-liquid phase separation as a post-translational readout, so the signal needs no new gene expression; modular sensor domain, fixed reporter.
- [UofGlasgow](https://2026.igem.wiki/uofglasgow) (GBR) — **C** — gut-brain axis route to Alzheimer's screening in *Lactobacillus gasseri*, with a nisin-inducible lysis device doing double duty as signal release and biocontainment, and a stated adhesion number (1.7%).
- [WIST](https://2026.igem.wiki/wist) (TWN) — ultrasound as the readout channel.
- [HongKong-HS](https://2026.igem.wiki/hongkong-hs) (HKG) — **C H** — enzyme-free hybridisation chain reaction for an at-home urine kit, after toehold switches proved too insensitive; assay chemistry changed twice (G4-ThT → hemin-G4/TMB) and they name the remaining false-positive problem.
- [ICT-Mumbai](https://2026.igem.wiki/ict-mumbai) (IND) — **C** — whole-cell TB sensor with a two-component system and a plain X-gal blue readout; deliberately low-tech.
- [NotreDame](https://2026.igem.wiki/notredame) (USA) — **S C** — glycol contamination in paediatric syrups, aimed at LMIC manufacturers rather than clinics. Unusual choice of user.
- [NIS-Kazakhstan](https://2026.igem.wiki/nis-kazakhstan) (KAZ) — **M S** — seven-variant DPYD qPCR panel with full reporting (36 oligos, 66/66 expected probe signals, clean NTCs). Pharmacogenomic access gap in a specific health system.
- [BAID-China](https://2026.igem.wiki/baid-china) (CHN), [YiYe](https://2026.igem.wiki/yiye) (CHN), [JLU-SPH](https://2026.igem.wiki/jlu-sph) (CHN), [ZJUT-China](https://2026.igem.wiki/zjut-china) (CHN), [GCGS](https://2026.igem.wiki/gcgs) (CHN) — conventional-form projects (sandwich ELISA/nanobody, toehold switch panel, RPA+Cas12a panel, probiotic CRC screen, dual-input AND-gate therapy). Visit only if time allows; GCGS is arguably therapy rather than diagnostics and its Fur + RhlR two-input logic is the one interesting item.

---

## 4. Fashion & Cosmetics — the C and S buckets in detail

Sustainable materials and waste valorisation (closest to the professor's Taiwan-relevant niches):

- [TU Darmstadt (UNRAVEL)](https://2026.igem.wiki/tu-darmstadt) (DEU) — **C H** — thermophilic, anaerobic chassis to degrade blended PET/nylon/cotton textiles without separation; five enzymes engineered for thermostability; they built their own equipment to handle the organisms. Ask what the equipment is.
- [QingdaoAcademy (UPkeep)](https://2026.igem.wiki/qingdaoacademy) (CHN) — **C S** — *Ulva prolifera* green-tide biomass into ulvan oligosaccharides via a designer cellulosome, with hydrolysate feeding the enzyme production and cellulosome recovery for reuse; explicitly argues the revenue offsets bloom losses. Direct read-across to Taiwan's coastal blooms.
- [HUST-China (IRIS)](https://2026.igem.wiki/hust-china) (CHN) — fashion waste → bacterial cellulose → CNC structural-colour film.
- [Concordia-Shanghai (SCOPE)](https://2026.igem.wiki/concordia-shanghai) (CHN) — LCA-driven, plus the HALO accessibility build; also a modelling claim worth probing (alanine substitutions at BcsA's Glu370–Arg583 salt bridge to predict a c-di-GMP-independent synthase).
- [NENU-China (CottonStatic)](https://2026.igem.wiki/nenu-china) (CHN) — **C M** — CBM3a-linker-PaPilA fusion that anchors to cotton and self-assembles a humidity-independent conductive nanowire network; three DBTL cycles; starts from a quantified public misconception (83% believe cotton is antistatic).
- [Tsinglan (you NAILed it)](https://2026.igem.wiki/tsinglan) (CHN) — **C** — three-module biodegradable nail system: chromoprotein polish (mutated gfasPurple, thermostability verified), hydroxyapatite-alginate tips, mussel-foot + spider-silk bio-glue. Good example of a whole consumer product rather than one ingredient.
- [ZQT-Nanjing (EctoBloom)](https://2026.igem.wiki/zqt-nanjing) (CHN) — **C** — ectoine without high-salinity fermentation (LysC T352I mutation), wheat-straw hydrolysate feedstock, bacterial-cellulose mask substrate.
- [Cataverse-Union](https://2026.igem.wiki/cataverse-union) (CHN) — **C** — cultural-relic restoration: pigment synthases fused to a cellulose-binding module so biopigments deposit and stay bound on paper or silk. Heritage conservation as a synthetic-biology market is a genuinely new category.
- [Usherbrooke](https://2026.igem.wiki/usherbrooke) (CAN) — **C S** — γ-PGA as a hyaluronic-acid substitute in *Bacillus subtilis* var. natto, with supply-chain sovereignty (Asian production concentration, North American import dependence) as the stated driver. Same genus as ReLeaf; ask about their *B. subtilis* handling and promoter work.

Bio-production of cosmetic and fragrance ingredients (C, with M where modelling is real):

- [Tsinghua-T (GALATEA)](https://2026.igem.wiki/tsinghua-t) (CHN) — **M C** — spatial enzyme ordering inside an engineered LLPS condensate to suppress off-pathway demethylation, plus a software platform with an adaptive AI agent and literature-retrieval algorithm, and an SDG-aligned evaluation framework. Strongest M in the Fashion hall.
- [Westlake](https://2026.igem.wiki/westlake) (CHN) — **M H C** — AI turns stated preferences into a scent recipe, engineered yeast makes the terpenoid components, custom automated hardware blends it. A closed loop from user input to physical product; ask how the AI was trained and what the blending rig actually is.
- [Qingdao-China (Yeauty)](https://2026.igem.wiki/qingdao-china) (CHN) — **M C** — genome-scale metabolic modelling identified a precursor-balance bottleneck, answered with P2A co-expression; endotoxin-free HA in *Komagataella pastoris*. A clean case of a model changing a construct.
- [CAFA-LZU](https://2026.igem.wiki/cafa-lzu) (CHN) — two-colour light control of which fragrance is made; bio-art exhibitions.
- [China-HUBU-Wuhan](https://2026.igem.wiki/china-hubu-wuhan) (CHN) — **C** — *Candida tropicalis* on palm oil with an intracellular/in-vitro decoupled design: the hard macrolactonisation step is moved out of the cell to lipase catalysis to spare host burden. Good split-the-pathway idea.
- [MIT-MAHE (MAHEK)](https://2026.igem.wiki/mit-mahe) (IND) — **C** — cuminaldehyde by knocking out cymC to stall *Pseudomonas putida*'s native degradation pathway at the desired intermediate.
- [Squirrel-Shanghai](https://2026.igem.wiki/squirrel-shanghai) (CHN) — **C** — cis-abienol as an ambergris substitute via the isopentenol utilisation pathway; conservation-driven substitution.
- [JLU-NBBMS (TetraxSkin)](https://2026.igem.wiki/jlu-nbbms) (CHN) — **C** — Compound K from ginseng by-products, delivered on DNA tetrahedra; waste-stream plus nanocarrier.
- [PROFUTURE-CHINA (Furflouris)](https://2026.igem.wiki/profuture-china) (CHN) — **C** — pet grooming as the market; allantoin at 68.14 ± 4.06 mg/L with error bars, plus a PepG-EGF repair fusion and a vanillin fragrance pathway.
- [HongKong-UCCKE (Phoeniveil)](https://2026.igem.wiki/hongkong-uccke) (HKG) — **C** — coral mycosporine-like amino acids overexpressing transketolase for the S7P precursor, chitosan-encapsulated into a layered burn bandage.
- [SPC (BioScyde)](https://2026.igem.wiki/spc) (HKG) — **C H M S** — reef-safe scytonemin sunscreen; two software tools (a codon-repeat-eliminating DNA Design Suite, a protocol safety module), custom pigment-extraction hardware, and a technoeconomic entrepreneurial assessment. Unusually complete across all four buckets for a high-school team.

Living products, microbiome and human-practices-led design:

- [HKUST-GZ (BioWipe)](https://2026.igem.wiki/hkust-gz) (CHN) — engineered *B. subtilis*, biosafety switch, phased commercialisation; user interviews changed the form factor from a wipe to a finger sleeve.
- [IITDelhi (DermaSense)](https://2026.igem.wiki/iitdelhi) (IND) — **C M S** — living moisturiser in skin-commensal *Staphylococcus epidermidis* that doses itself under oxidative stress, with software pulling live global air-quality data to estimate damage and protection. Environment-responsive living product; the honest note is that proof of concept was only in *E. coli*.
- [GreatBay-SCIE (Expelliodor)](https://2026.igem.wiki/greatbay-scie) (CHN) — **C S** — three parallel de novo protein strategies against the odour precursor rather than killing skin flora; and the human-practices conclusion is a position, not a product claim: body odour is normal variation and managing it should stay a personal choice. Best stigma-handling in the slice.
- [Cornell (Klothos)](https://2026.igem.wiki/cornell) (USA) — **H C S** — gated probiotic releasing anti-fibrotic peptides, electrospun into an alginate nanofibre smart bandage on a coaxial electrospinner they built; explicit price-point positioning against the cosmeceutical market.
- [TecCEM (MONARCH)](https://2026.igem.wiki/teccem) (MEX) — **C M S** — in-silico multifunctional peptides, *Lactococcus lactis* GRAS chassis with a metabolic model built to handle its lactic-acid metabolism, and a business proposal shaped by multidisciplinary interviews.
- [Baltimore (KeraTINT)](https://2026.igem.wiki/baltimore) (USA) — **C** — keratin-binding peptide fused to seven different chromoproteins so the dye repairs while it colours; they wrote their own assays for multiple hair types.
- [Worldshaper-HZ (BlackNova)](https://2026.igem.wiki/worldshaper-hz) (CHN) — **C S** — polydopamine hair dye plus an adhesion peptide, packaged as a consumer kit; the second of two hair-dye teams in this hall, so compare with Baltimore.
- [SSES](https://2026.igem.wiki/sses) (CHN) — **C** — isovaleric-acid odour degradation needing all four of FadL, FadD, AidB and MccAB co-expressed, with a pTRIP temperature-dependent quorum-sensing kill switch that stays off at 37 °C fermentation and lyses the cells at ambient temperature. Containment design worth copying.

---

## 5. Questions to carry to specific booths

Ordered by how much they feed the three ReLeaf-adjacent reports.

1. **NU-Kazakhstan, IIT-Madras, IOANNINA, Hamburg** — what does the optical front end cost in parts, and how is the reading calibrated to concentration? ReLeaf's own OD600 channel sits on a reference-channel count-to-OD conversion, so comparable numbers from three independent low-cost readers are directly useful.
2. **WIST** — how were the acceptance gates written and frozen before the run, and what did they do when the OFF state capped the fold change? This is the same problem class as ReLeaf's frozen criteria and reported shortfalls.
3. **HKUST-GZ and SSES** — how did regulators or advisors react to a live-organism consumer product, and what convinced them the kill switch was enough? Both use density- or temperature-gated containment.
4. **CAFA-LZU** — how reproducible is light-colour-selected product identity across a batch, and what light hardware delivers it? Nearest external comparison to ReLeaf's green/red control.
5. **Usherbrooke** — practical *B. subtilis* (var. natto) promoter and knockout experience; same genus, different product.
6. **Tsinghua-T and Westlake** — what exactly does the "AI agent" do in the design loop, and which decisions did it actually change? Useful calibration for how ReLeaf should describe its own optimisation layer.
7. **Qingdao-China and Puebla** — ask for a case where the model contradicted the data and what they changed. Both have one.
8. **Concordia-Shanghai** — how was the LCA functional unit defined? ReLeaf will need the same discipline if it ever claims an energy or water advantage.
9. **BK-Denmark, SZPU-CHINA, UFABC-Brazil, HongKong-HS** — all four published a negative or partial result. Ask how they decided to report it and how judges responded; this is reusable evidence for ReLeaf's own "what we did not achieve" sections.
10. **QingdaoAcademy and TU Darmstadt** — feedstock economics of waste-derived processes: what does the hydrolysate actually cost once collection is counted?

---

## 6. Abstract-less teams in this slice — decide at the venue

Ten Diagnostics records carry a team name, country and village but no title, abstract or wiki link. They cannot be triaged from this file. Several of the names suggest diagnostics hardware or sensing, so an advisor passing through the Diagnostics hall should glance at each board and pick up anything matching the H bucket.

| Team | Country |
|---|---|
| Aptalxero | IND |
| DETEX | GHA |
| ExPrimary | USA |
| GaitMate | USA |
| Gallisa | CHE |
| MolVerse | IND |
| NeuroXense | ARG |
| SenseBio | SAU |
| SynFRET | BRA |
| XMars | USA |

Worth noting for the report's coverage statement: DETEX (Ghana) and SenseBio (Saudi Arabia) are the only entries in this slice from their regions, so a booth visit is the only way to include them.

---

## 7. Patterns worth stating in the post-trip report

- **The reader is becoming the project.** At least nine Diagnostics teams built a physical readout instrument, and the pattern has settled into one of two shapes: a 3D-printed enclosure that turns a smartphone camera into a fluorimeter (NU-Kazakhstan, IOANNINA), or a dedicated low-cost photodetector (IIT-Madras's SiPM, Hamburg's optical sensor, BIT's custom reader). Smartphone-as-detector is now the default assumption rather than an innovation.
- **Teams are designing around instrumentation they cannot afford.** SRE-China staging a one-pot reaction by temperature alone, ICT-Mumbai settling for X-gal blue, HongKong-HS going enzyme-free, ZZU shipping both a lab assay and a strip — all are choices made to delete equipment from the deployment site rather than to add capability.
- **Every serious Diagnostics team now ships software with the biology.** Charlotte-HS (three tools), DelNorte-SD (two), UMA Malaga (Diana), BIT (FluoroCheck), SPC (two), NU-Kazakhstan (ColoRisk). Design-tool-plus-analysis-tool has become part of the expected deliverable set.
- **Fashion & Cosmetics is where the cross-field mash-ups live.** Art academy optogenetics (CAFA-LZU), heritage conservation enzymology (Cataverse-Union), kingfisher-feather ethics answered with nanocrystal optics (HUST-China), environmental economists choosing the product (Concordia-Shanghai), supply-chain sovereignty as the project driver (Usherbrooke), disability-inclusive lab furniture shipped alongside the biology (Concordia-Shanghai again). This hall, not Diagnostics, is where new project categories are being invented.
- **Waste-to-cosmetics is a consolidated niche with obvious Taiwan analogues:** algal blooms (QingdaoAcademy), blended textile waste (TU Darmstadt, HUST-China), ginseng by-products (JLU-NBBMS), wheat straw (ZQT-Nanjing), palm oil (China-HUBU-Wuhan).
- **Containment is being designed, not bolted on.** UofGlasgow's lysis device doubling as signal release, SSES's temperature-plus-quorum-sensing suicide module, HKUST-GZ's xylose-and-density switch, GCGS's two-input Fur/RhlR requirement. All four make containment part of the circuit's logic.
- **A visible minority reports failure plainly** — BK-Denmark (no detectable activity), SZPU-CHINA (no HA-dependent activation, offered as a foundation not a detector), Puebla (construct lost dCas9; model rules out the obvious explanation), WIST (fold change capped by the OFF state), UFABC-Brazil (whole-cell only preliminary), IITDelhi (proof of concept in the wrong chassis). Worth naming in the report, since ReLeaf's own pages take the same approach and it helps to know the practice is spreading.
