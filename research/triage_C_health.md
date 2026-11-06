---
layout: doc
title: Therapeutics, oncology, infectious disease
eyebrow: Triage · slice C
section: Triage
description: 98 teams, read for transferable method rather than subject matter.
---

**Teams read:** 98 (Therapeutics 67, Oncology 18, Infectious Diseases 13). 5 have no abstract in the slice.
**Audience:** GEMS-Taiwan advisors Gabriel (G, wet lab), Chars (Ch, wet lab), Timmy (T, PI / dry lab).
**Honest framing:** almost nothing here is agriculturally relevant. The value is transferable method — secretion, containment, sensor circuits, peptide design, modelling discipline, and the handful of teams that built hardware.

## Overview

The chassis monoculture is striking: *E. coli* Nissle 1917 carries at least a dozen projects (Cataverse-GreatBay, CHINAGuangdongShimen, UNC-Chapel Hill, SUDA-ICPI-China, UC Davis, Worldshaper-SHMed, HFI, KCSCD, SYPHU-China, PuiChing-Macau, HUST-UEVE-UPSaclay, SCU-WestChina), differing only in payload. Two-input logic sensing is the other crowd — hypoxia + lactate (SUDA-ICPI-China), pH + putrescine (MSP-Maastricht), succinate-high/butyrate-low (Worldshaper-SHMed), HLA-A2 then VCAM-1 (TU-Eindhoven), AI-2 + tetrathionate (LZU-CHINA), fatty acid + oxidative stress (AFCM-Egypt) — so circuit architecture is cheap to learn here and worth comparing across booths rather than at one. Hardware is genuinely rare: only Aachen (automated two-stage VLP bioreactor with its own control software), McMaster-Canada (custom bioreactor plus microfluidic OMV isolation), NIS Almaty-Medeu (metal-oxide gas-sensor e-nose), PuiChing-Macau (delivery hardware and dosing software), PLKLFC (3D bioprinting) and SUIS-SFLS (enzyme on magnetic beads) built anything physical. Kill switches appear everywhere but are nearly all boilerplate arabinose or temperature switches (Stony Brook, UC Davis, ICJFLS, PLKLFC, HFI); SYPHU-China is the only team that designed containment without introducing a toxin at all. Secretion is the slice's unspoken bottleneck — YebF turns up twice independently (Waterloo, Stony Brook) and signal-peptide screening is an afterthought in several others (UCS-B) — which is exactly ReLeaf's weak spot. Finally, most abstracts are entirely future tense (Sheffield, GU Frankfurt, U Copenhagen, NTU-Singapore); the five that report something that failed (Gikal, Stony Brook, NCState, UI-ITB-Indonesia, Boston-BOSLab) are the ones worth the queue.

Priority list below is 15 teams. Two others score 3 in the table (XJTLU, and SUDA-ICPI-China which is in the list) — treat XJTLU as the alternate if a booth is mobbed.

## Priority targets

### Aachen — Adesonica (Infectious Diseases, DEU, overgrad)
- **Buckets:** C, H, M
- **Why it's worth the walk:** They built M.A.R.M.A.L.A.D.E., a two-compartment automated reactor — bacteria express TMV coat protein in the first part, virus-like particles assemble in the second — plus the control software for it. Separately they trained an ML model to predict the transcriptome from the methylome specifically to cut measurement cost, and packaged growth-rate prediction from transcriptomics as a Python library.
- **Relevance to ReLeaf/GEMS:** Technique to borrow, and the closest benchmark in the slice for our own reactor-plus-software stack.
- **Ask at the booth:** How is the handover between the expression stage and the assembly stage sensed and triggered — a timer, OD, or a product measurement? What did the control software actually control, and what was left to the operator? What was the training-set size for the methylome→transcriptome model, and what error made it not worth trusting?
- **Assign:** T

### Houston-TX — AKGut: Model-Guided Design of a Probiotic that Produces α-Ketoglutarate (Therapeutics, USA, overgrad)
- **Buckets:** M
- **Why it's worth the walk:** This is the only team in the slice where modelling demonstrably changed the build: flux balance analysis on iHM1533 named glutamate dehydrogenase (not α-KG dehydrogenase) as the main drain, put the production optimum near half-maximal oxygen, showed no knockout set couples production to growth, and caught a residue-numbering error that would have put the citrate synthase mutation one residue off. They also say the chromosomal knockouts are still in troubleshooting.
- **Relevance to ReLeaf/GEMS:** Benchmark — this is the standard our digital twin should be judged against, i.e. modelling that produces decisions and catches errors rather than a figure.
- **Ask at the booth:** Which FBA constraints did you have to set by hand before the oxygen optimum stopped moving? How did you notice the numbering error — was it a model output or a sequence check? Given no knockout couples production to growth, what does the α-KG addiction system look like on paper and why did you not build it?
- **Assign:** T

### SUSTech — ORCA: On-target RNA Correction of APOE4 (Therapeutics, CHN, undergrad)
- **Buckets:** M
- **Why it's worth the walk:** They quantify the trade-off instead of claiming a win: two candidate editors retained 61–70% target editing while cutting cumulative bystander editing in the measured APOE region by 84–88% against the parental editor. They also built SONAR plus a stated measurement pipeline to make reporter readouts reusable and interpretable, and ran protein and RNA foundation models in an explicit loop with wet-lab measurement.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — the measurement-pipeline-as-deliverable pattern is directly transplantable to our OD600 and calibration work.
- **Ask at the booth:** What does the SONAR pipeline normalise against, and how did you set the window for "the measured APOE region"? Which predictions from the foundation models were wrong, and did the wet-lab result change the model or just the shortlist? How many replicates sit behind the 84–88% range?
- **Assign:** T

### PuiChing-Macau — Tuning butyrate with engineered probiotics to prevent Alzheimer's (Therapeutics, MAC, high-school)
- **Buckets:** C, H, M
- **Why it's worth the walk:** The circuit is a closed loop with an explicit brake: a pNorVβ promoter senses nitric oxide, and butyrate biosynthesis runs under a negative feedback loop specifically to prevent overproduction. They also claim customised delivery hardware, risk-prediction software and a personalised dosage model — an unusual high-school combination, and the hardware/software claims are thin enough in the abstract to be worth probing.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — negative feedback inside the cell is the alternative to doing all regulation in our external controller.
- **Ask at the booth:** What is the feedback element in the butyrate loop, and how did you measure that it actually limited output rather than just lowering it? What does the dosage model take as input, and was it fitted to data or assumed? Can we see the delivery hardware — what does it cost and what does it actually actuate?
- **Assign:** T

### SUDA-ICPI-China — FLAME: An Engineered Bacterial Platform for Precision Colorectal Cancer Therapy (Oncology, CHN, undergrad)
- **Buckets:** C, M
- **Why it's worth the walk:** Three-input gating — hypoxia and lactate sensing combined with LuxI/LuxR quorum sensing — with reporter data showing the strongest response under combined low oxygen and lactate, so the AND behaviour was tested, not asserted. Modelling informed promoter selection and identified limits on selectivity and achievable lesion size. They compared untagged, TAT-fused and SsrA-tagged effectors and prioritised the SsrA version on safety grounds.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — degradation tagging as a safety dial, and modelling used to choose a promoter rather than to decorate one.
- **Ask at the booth:** What did the model say the selectivity ceiling was, and which promoter did it eliminate? How did the three tagged effector versions differ quantitatively in the non-tumour L929 cells? Does quorum sensing add anything the hypoxia/lactate pair did not already give you?
- **Assign:** T

### McMaster-Canada — Chariot: A Platform Technology for OMV-based Therapeutics (Therapeutics, CAN, undergrad)
- **Buckets:** C, H, M
- **Why it's worth the walk:** They attack the real bottleneck in vesicle production — yield and variability — with vesicle nucleating peptide tags to load cargo into outer membrane vesicles, and they built the kit around it: a custom bioreactor and a microfluidic OMV isolation device, plus two in silico tools for de novo cargo generation and VNp sequence optimisation.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — this is the closest thing in the slice to our problem of getting a protein out of the cell and across a membrane, with hardware attached.
- **Ask at the booth:** What yield improvement did the VNp tag give over untagged cargo, and how did you measure OMV concentration? What does the microfluidic isolation device cost to build, and what does it replace — ultracentrifugation? Did VNp tagging work for antimicrobial peptides as well as for antigens, or only one class?
- **Assign:** Ch

### Gikal — ZipTide: designing short peptides against zonulin-driven loss of the intestinal barrier (Therapeutics, TUR, high-school)
- **Buckets:** M, S
- **Why it's worth the walk:** The most disciplined peptide-design funnel in the slice, and the most honest: 25.6 billion 8-mers collapsed onto 2,220,075 compositions without discarding any, ranked by physicochemical distance to larazotide, 1,500 screened for toxicity/allergenicity/haemolysis, 20 docked, 3 synthesised. The success criterion was written before any data existed, the gliadin assay worked (zonulin up 4.8-fold, reversed by larazotide), and they report that neither tested candidate cleared the bar and the third arrived as an empty vial.
- **Relevance to ReLeaf/GEMS:** Benchmark — this is the template for how BoPep4 should have been selected and pre-registered.
- **Ask at the booth:** How did you collapse 8-mers onto compositions without losing position information, and what did that cost you at the docking stage? What exactly was the pre-written criterion, and who held it? Of the filters — toxicity, allergenicity, haemolysis — which killed the most candidates, and did any filter turn out to be useless?
- **Assign:** Ch

### HKU-HongKong — Omni-Patch (Therapeutics, HKG, undergrad)
- **Buckets:** M
- **Why it's worth the walk:** A de novo pipeline with named tools — RFdiffusion, LigandMPNN, molecular dynamics — aimed at a specific interface (MD-2/LPS in the TLR4 complex), producing lead αTi-14 that reduced cell-associated fluorescent LPS in macrophage-like cells. They state plainly that functional confirmation is still ongoing, and their mathematical model links molecular design to alginate release kinetics and downstream response.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — the design-to-release-kinetics chain is the same chain we need from BoPep4 through the membrane.
- **Ask at the booth:** How many RFdiffusion designs survived LigandMPNN and MD before you ordered anything, and what MD observable did you filter on? What does "reduced cell-associated fluorescent LPS" mean numerically, and why is that not yet functional confirmation? How did you parameterise the alginate release part of the model — measured or literature?
- **Assign:** Ch

### NCKU-Tainan — Capture: A Dual-Action Biosensor and Inhibitor for Pseudomonas aeruginosa (Infectious Diseases, TWN, undergrad)
- **Buckets:** C, H
- **Why it's worth the walk:** An AHL biosensor giving a visible fluorescent readout for low-cost screening, paired with a retron system producing ssDNA aptamers that bind AHL — using retrons to make aptamers in vivo is unusual in this slice. Also the other Taiwanese team in the health villages, so the booth doubles as a domestic contact. The abstract's inhibition claims (swarming, pyocyanin, biofilm) are stated without numbers.
- **Relevance to ReLeaf/GEMS:** Technique to borrow (fluorescent readout calibration) and new direction (retron-generated ssDNA as a tunable binder source); plus a Taiwan network contact.
- **Ask at the booth:** What is the detection floor of the AHL biosensor in molar terms, and against what standard curve? How did you quantify retron ssDNA yield per cell, and how did you confirm aptamer binding rather than inferring it from phenotype? Which of the three phenotypes dropped most, and by how much?
- **Assign:** Ch

### LethbridgeHS — Oat Shield: Sustainable cellulose bandages with integrated antimicrobial peptides (Therapeutics, CAN, high-school)
- **Buckets:** C, H
- **Why it's worth the walk:** The only team in the slice working on our organism's product: subtilin, the antimicrobial peptide from *Bacillus subtilis*, expressed heterologously in *E. coli* under an IPTG-inducible promoter with a hexahistidine tag. The material half — cellulose extracted from oat husk agricultural waste — is the one genuine agriculture/sustainable-materials crossover in the health villages.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — their subtilin expression and purification route is a direct comparator for our peptide work, and the ag-waste framing is a model for how to connect to Taiwanese agriculture.
- **Ask at the booth:** Why express subtilin in *E. coli* rather than in *B. subtilis*, and what yield did you get after the His-tag purification? Did the peptide survive incorporation into the cellulose matrix, and how did you test that? Which cellulose extraction method won, and on what criterion — fibre length, yield, or cost?
- **Assign:** Ch

### Stony Brook — Engineering Bacteria to Detect and Break Down Biofilms Secreted by *S. aureus* (Therapeutics, USA, undergrad)
- **Buckets:** C, M
- **Why it's worth the walk:** Three enzymes pushed out through a YebF carrier, and they report exactly which ones worked: secretion confirmed for Nuclease1 and SspA, eDNA degradation confirmed, SspA proteolytically active — and Dispersin B stayed membrane-embedded and untested. They also state that biofilm degradation itself remains undemonstrated. Two-signal detection (AI-2 early, nitric oxide late) with an arabinose-inducible mazE/mazF kill switch.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — a YebF secretion failure case with a named culprit is worth more to us than three successes.
- **Ask at the booth:** Why do you think Dispersin B stayed membrane-embedded when the other two cleared — size, glycosylation, fold? What fraction of each enzyme ended up extracellular, and how did you measure it? How fast does the mazEF switch clear the population after arabinose, and does it leak without it?
- **Assign:** G

### Waterloo — Biofilm Busters: Targeting Pathogenic Gut Biofilms Through Curli Inhibition (Infectious Diseases, CAN, undergrad)
- **Buckets:** C, M, S
- **Why it's worth the walk:** The second independent YebF secretion case in this slice — an N-terminal YebF carrier to secrete CsgC, a natural amyloid chaperone, so the mechanism inhibits curli assembly rather than killing bacteria. They plan a move to *Lactococcus lactis* with inducible expression and biological containment, and used bioinformatics to survey curli genes across gut taxa to predict which organisms would be hit.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — comparing their YebF experience against Stony Brook's gives two data points on the same carrier, and the off-target taxa survey is a model for asking which soil organisms our protectants touch.
- **Ask at the booth:** How did the YebF–CsgC fusion behave on yield compared with keeping CsgC intracellular? What made you choose *L. lactis* over staying in *E. coli*, and what containment is planned? What did the gut-taxa survey say you would affect that you had not expected?
- **Assign:** G

### SYPHU-China — LBP-Mototype: An Environment-Dependent Suicide Strategy for IBD Live Biotherapeutics (Therapeutics, CHN, undergrad)
- **Buckets:** C, M
- **Why it's worth the walk:** The only containment design here that does not introduce a toxin. Deleting acrB and pspA weakens bile efflux and membrane protection; inflammation-responsive PspA complementation conditionally restores protection while AcrB stays absent, so ambient bile stress is the killing agent and the genetic killing chain gets shorter. They also think about the awkward parts — protein carry-over buffering the signal, par⁻-associated inheritance variation producing graded survival.
- **Relevance to ReLeaf/GEMS:** New direction — our kill switch should probably be environment-dependent rather than toxin-based, since outside the bioreactor there is no bile but there are other absent nutrients.
- **Ask at the booth:** What is the measured survival ratio between the inflamed and non-inflamed condition, and how long does protein carry-over delay the kill? How did you pick acrB and pspA over other efflux/membrane genes? What is the escape frequency, and did the par⁻ inheritance variation show up experimentally or only in the model?
- **Assign:** G

### ICJFLS — ORA-GUARD: Engineered Oral Probiotics for Long-Term Bad Breath Solution (Therapeutics, CHN, high-school)
- **Buckets:** C, S
- **Why it's worth the walk:** Three of our weak spots in one booth: CRISPR-Cas9-mediated genome integration (not a plasmid) into *Streptococcus salivarius* K12, a codon-optimised multi-enzyme system secreting volatile-sulfur-degrading enzymes, and layered containment combining auxotrophy with a temperature-sensitive kill switch. "Efficiently secretes" and "precise and sustained" are claims with no numbers attached — worth pressing.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — genome integration plus secretion in a Gram-positive commensal is the nearest analogue to what we need in *B. subtilis*.
- **Ask at the booth:** What integration efficiency did you get in *S. salivarius*, and which locus? Which signal peptide did the secreted enzymes use, and did codon optimisation or the signal peptide move the yield more? How tight is the temperature switch, and does auxotrophy actually add anything measurable on top of it?
- **Assign:** G

### KULeuven — EMPOWER: Engineering Microbes to Promote Ovarian Wellbeing and Recovery (Therapeutics, BEL, overgrad)
- **Buckets:** C, M
- **Why it's worth the walk:** Before the therapy, they built the missing toolkit for a non-model anaerobe, *Phocaeicola vulgatus*: characterised promoters evaluated across four fluorescent reporters, optimised conjugation, and phenotypic characterisation of candidate chassis strains. Using four reporters rather than one is a measurement choice almost nobody else in this slice made.
- **Relevance to ReLeaf/GEMS:** Technique to borrow — a parts-characterisation protocol for an awkward chassis, and a reason to re-express our CcaSR characterisation in more than one reporter.
- **Ask at the booth:** How much did the promoter ranking change between the four reporters, and which reporter did you end up trusting? What made conjugation work in the end — donor strain, mating time, selection? Which candidate chassis strains did you reject, and on what phenotype?
- **Assign:** G

## Full triage table

| Team | Title | Buckets | Score 0–3 | One-line hook |
|---|---|---|---|---|
| Aachen | Adesonica | C, H, M | 3 | Two-stage automated VLP bioreactor with its own control software; ML predicts transcriptome from methylome to cut measurement cost |
| Boston-BOSLab | Epidermighty | M, S | 2 | 90 computational binder designs, 5 tested, binding still unconfirmed — and the abstract says so |
| Hopkins | Oralis | C | 1 | SpyTag/SpyCatcher VLP display on a floss-like device; room-temperature stability asserted, not shown |
| IISc-Bengaluru | MOSKATEER | C, H | 2 | dsRNA packaged by tandem MS2 coat repeats, delivered from an acetoin-baited sugar-matrix field trap |
| NCKU-Tainan | Capture | C, H | 3 | Taiwan team: AHL biosensor plus retron-made ssDNA aptamers against the quorum signal |
| Ohio State | SprayAway | M | 2 | Shannon entropy used to pick three ultraconserved HIV LTR target sites; EV surface engineering for CD4 tropism |
| PeptiForge-UDEM | — | — | ? | no abstract — check wiki |
| SUSTechOcean | Lactosylarchaeol adjuvant in *E. coli* | C, M | 2 | Light-controlled module strips host phospholipids while sparing the ether-linked product |
| UChicago | GENELOCK | C, M | 2 | Designed condensate protein (DNA-binding + IDR + oligomerisation), read out by ParB–parS plus OD and CFU |
| UiOslo-Norway | HePatch | M | 2 | Thermostable HBsAg variants claimed stable 28+ days at 37–45 °C; microneedle patch, no data in abstract |
| Vironics AI | — | — | ? | no abstract — check wiki |
| Waseda-Tokyo | SUNRISE | C | 2 | Protein injector delivers an adaptor that recruits host ClpXP to degrade resistance proteins |
| Waterloo | Biofilm Busters | C, M, S | 3 | YebF-carrier secretion of CsgC plus planned *L. lactis* containment and a gut-taxa off-target survey |
| Bist-China | PyrLac Glow | H | 1 | Lactate/pyruvate ratio by fluorescent probe as a cheap screen; no mechanism or data |
| BNU-China | CABOMB | C | 1 | Nanoscale CaCO₃ carrier plus MNAzyme effector; every claim forward-looking |
| Caltech | Cervixa | C, M | 2 | ODE rate-kinetic model of a homologous-recombination readout, pitched as reusable DNA logic |
| CSW-UD | BSMV virus-like particles for TNBC | C | 2 | Plant-virus rod VLP with cysteine-mutated inner channel for thiol-Michael doxorubicin conjugation |
| ECNU-China | PREVAIL | C | 1 | Hijacks population-wide SARS-CoV-2 memory T cells for antitumour response; concept only |
| HBUT-China | oHSV2-Neo-IL-2 | M, S | 2 | AI-designed IL-2 variant that keeps CD122/CD132 but loses CD25; named HOPES and SHIELD HP/safety frameworks |
| HIT-SLS | GLYCO-TAM | M, S | 2 | Seven DBTL cycles to land on MGAT5; LNP-mRNA reprogramming; states cell and animal models only |
| HKPOLYU | Engineered *Lactobacillus* secreting IL-37 | C, S | 2 | Publishes failed constructs and surface-modification protocols as a deliberate community deliverable |
| IZJU-China | X-BAT (*B. longum*, Gal8) | C | 1 | Gal8 surface display to force xenophagy and boost antigen presentation; design stage |
| JLU-FBH | CirCure | M | 2 | Epitope pipeline (MHC-I binding, immunogenicity, structure) compressed into one circRNA |
| NIS Almaty-Medeu | MiRVOX | H, M | 2 | Metal-oxide gas-sensor e-nose beside reverse-logic toehold switches; both labelled research-stage |
| Penn State | TRIDENT | C | 1 | Yeast exosomes coated with anti-TROP-2 nanobodies carrying miR-34α |
| PLKLFC | COLOPRINT | C, H, M | 2 | 3D-bioprinted alginate pills, hypoxia + formic-acid double criterion, arabinose kill switch |
| SEHS | FusionDrive | M | 2 | Reports EC50 1.155 nM and differential pSTAT5 between CD25⁺ and CD25⁻ cells — unusually numeric |
| SUDA-ICPI-China | FLAME | C, M | 3 | Hypoxia + lactate + quorum gating tested, modelling chose the promoter, SsrA tag used as a safety dial |
| Thessaloniki | AETh3R | M | 2 | Two peptide-PROTACs with VHL ligand; DOTAP-containing LNP tuned for lung biodistribution |
| UNC-Chapel Hill | CRYPTIC | C | 2 | Redirects tryptophan flux from the kynurenine to the indole pathway in EcN, plus KynU breakdown |
| Zhulu-China | RGD-ES/KS acid-responsive peptides | M, S | 2 | pH 6.0-triggered peptide barrier over five DBTL cycles; built PRISM, a locally deployed dual-use AI screening layer |
| Aarhus University | RiboLogic | C, M | 2 | miRNA-gated RNA logic domain upstream of a therapeutic mRNA; modularity claimed, not demonstrated |
| AFCM-Egypt | FROST | M | 2 | Validation organised as seven models, each an assumption turned into a prediction; survival and therapy on separate signals |
| AIS-China | C.L.E.A.R. | C, S | 2 | Methylating *E. coli* intermediate host to get plasmids into *C. acnes*; transformation still not achieved |
| BASIS-China | HEAL | C, H | 2 | Bile-acid-responsive containment linking growth to a signal scarce outside the gut, plus a food-weighing prototype |
| Beagle Bioworks | — | — | ? | no abstract — check wiki |
| Bielefeld-CeBiTec | α Synu-Clear | M | 2 | De novo binder to the human dopamine transporter plus a nanobody–LC3B degrader; design tools unnamed |
| BiHealthy | — | — | ? | no abstract — check wiki |
| Cataverse-GreatBay | Uric-acid-lowering oral probiotic | C | 1 | Uricase plus catalase in EcN with an engineered urate/xanthine transporter |
| CHINAGuangdongShimen | Re-CDI Alert | C, M | 2 | Heterologous PcrSR-Pcmh two-component sensor ported into EcN to detect p-cresol |
| CSU-CHINA | BRIDGE | M | 2 | Anti-BCAN synNotch refined by interface-guided mutagenesis against a structural model |
| CUHK-HongKong-SBS | Topical *L. plantarum* for psoriasis | C, S | 2 | Live biotherapeutic secreting an IL-23R-antagonist fusion peptide; explicit stigma-reduction campaign |
| DBHS-CA | FIV-UR | C, M | 2 | PhoR/PhoB phosphate limitation as the input that times glycosylation — nutrient level as a control layer |
| Epiphany-NYC | TheraNOva | C | 1 | NO-sensing promoter driving a butyrate enzyme and an anti-TNF siRNA inside vesicles |
| FSU | Lilieum | M, S | 2 | GROMACS partitioning simulation of DEHP in a membrane proxy; senses capture via membrane rigidity, then sheds pili |
| Gikal | ZipTide | M, S | 3 | Whole 8-mer space collapsed to 2.2M compositions, criterion written before data, candidates failed the bar |
| GU Frankfurt | HIDE | C | 1 | Local downregulation of donor HLA on the graft; no mechanism given in the abstract |
| Gymnasium Leiden | V.A.U.L.T | C | 2 | Eukaryotic major vault proteins made in *E. coli* with a protein-A Z-domain as an IgG docking site |
| HFI | Dual EcN for hyperlysinemia | C | 2 | SpyTag/SpyCatcher physically couples two strains into a "metabolic tunnel"; kill switch included |
| HKBU | FibroSwitch | C, M | 2 | Nrf2-responsive pARE promoter triggered by a herbal compound that is itself anti-inflammatory |
| HKU-HongKong | Omni-Patch | M | 3 | RFdiffusion/LigandMPNN/MD peptide pipeline tied to an alginate release-kinetics model; admits function unconfirmed |
| Houston-TX | AKGut | M | 3 | FBA chose the target, eliminated a design, and caught a residue-numbering error before cloning |
| HunanU | NariViva | C, M | 2 | Directly compares the circuit with and without negative feedback by Western blot and HPLC across pH |
| HUST-UEVE-UPSaclay | Pet Dental Guard | C | 2 | Engineered M13 phage delivering metronidazole alongside IL-10-producing EcN in a double-layer hydrogel |
| HZAU-China | PurrFit | C, S | 1 | MetaEdit on *B. thetaiotaomicron* plus an "AI agent" for feeding advice; AI module barely specified |
| ICJFLS | ORA-GUARD | C, S | 3 | CRISPR genome integration in *S. salivarius* K12, secreted multi-enzyme cassette, auxotrophy plus temperature kill switch |
| KCSCD | FELIX | C | 1 | Lipase envelope degradation plus RNAi EcN across three "fronts"; broad and unvalidated |
| KFUPM-Saudi | ARMOR | M, H | 2 | oxDNA simulation plus COMSOL transport model of a needle-free patch and a three-compartment delivery analysis |
| KULeuven | EMPOWER | C, M | 3 | Promoter library characterised with four fluorescent reporters and optimised conjugation in a non-model anaerobe |
| LethbridgeHS | Oat Shield | C, H | 3 | Subtilin from *B. subtilis* expressed in *E. coli*; bandage cellulose extracted from oat-husk waste |
| LHWHS Missouri | siRNA cocktail screening | H, M | 1 | "Proprietary" single-cell-addressable plate platform asserted with no method, data, or validation |
| LINKS-Union | S.H.I.E.L.D | C | 2 | MtuI intein self-cleaves below pH 6.5 to release LL-37; ALP/CaGP mineral layer slows the release |
| Lund | Gut-based approach to androgen excess in PMOS | C | 1 | Gut-responsive switch driving androgen-metabolising enzymes; proof-of-concept stage only |
| LUT-CHINA | Four-layer dressing for diabetic foot ulcers | C | 2 | Two herbal bioactives biosynthesised in *E. coli*, lobetyolin HPLC-validated, built into a four-layer dressing |
| LZU GANSU | DENTAL SHIELD | C | 1 | *L. lactis* that reports hidden lesions and treats them; abstract gives no mechanism at all |
| LZU-CHINA | Intestinal barrier vs perioperative *Salmonella* | C, M | 2 | AI-2 quorum sensing plus tetrathionate inflammation signal as a dual switch for AMP expression |
| MaiAnTiem | — | — | ? | no abstract — check wiki |
| McMaster-Canada | Chariot | C, H, M | 3 | Vesicle nucleating peptide tags for OMV loading, with a custom bioreactor and microfluidic isolation device |
| Michigan | MagNav | C, H | 2 | Magnetotactic AMB-1 steered by external magnets and gated by fine-tuned RNA thermometers |
| MSP-Maastricht | Vivora | C | 2 | Two-input pH and putrescine detection in *L. jensenii*, reusing a previous iGEM team's protocols |
| NCState | AMPack | M, S | 2 | Reports that the selection antibiotic confounded the growth comparison, with p-values — honest negative framing |
| NTU-Singapore | Efficient RNA writers | M | 1 | Promises trans-splicing design rules; no construct or result in the abstract |
| Patras UPAT | EPIONE | M | 2 | 2×2 construct matrix of linker chemistry against reporter orientation; in vitro maturation with PC2, 7B2, CPE |
| PekingHSC | HEPHA-RNA | M | 2 | Translation enhancer recruiting the 60S subunit; >1.5-fold protein with no mRNA increase across two blots |
| PuiChing-Macau | Tuning butyrate to prevent Alzheimer's | C, H, M | 3 | NO biosensor plus negative-feedback butyrate circuit, with delivery hardware and a dosing model |
| SCU-WestChina | PerioGuard | C, M | 2 | CsgA–amelogenin secretion under a HucR circuit, plus an AI-predicted nucleoside adsorptive coating |
| Sheffield | DRAVEX | C | 1 | RVG–Lamp2b exosomes for BBB transport; entirely future tense |
| SJTU-BioX-Shanghai | Dual-Armor | C | 2 | Two chassis coordinating through naringenin signalling inside a freeze-dried multilayer dressing |
| SNIoE-India | SmogSense | C, M | 2 | PM2.5-driven NF-κB sensing with IL-10 feedback in human macrophages; self-limiting by design |
| Stanford University | Kele Patch | M | 2 | RADAR mRNA sensor reads cell transcriptional state; RADAR-Scout offered as a reusable platform |
| Stony Brook | Detect and degrade MRSA biofilms | C, M | 3 | Two of three YebF-secreted enzymes confirmed, Dispersin B reported stuck in the membrane, arabinose mazEF switch |
| SUIS-SFLS | TyroFix | C, H | 2 | Tyrosinase immobilised on magnetic beads for reuse; DOPA-modified mussel adhesive protein |
| SUSTech | ORCA | M | 3 | 61–70% on-target editing with 84–88% less bystander editing, plus a named measurement pipeline |
| SUSTech-MED | FORGE | C | 1 | *L. plantarum* making SFN and NAC plus ammonia-to-BCAA conversion, intranasal; claims outrun the evidence |
| SYPHU-China | LBP-Mototype | C, M | 3 | Containment with no introduced toxin: acrB/pspA deletions make ambient bile the killing agent |
| SZA-Union | Enzymatic strategy against oral biofilm | C | 1 | α-1,3- and α-1,6-glucanases in *E. coli* assessed by HPLC, TLC, SEM and staining |
| Thessaly | ATHENA | C, M | 2 | Conjugative plasmid disarms UPEC in place rather than killing it; NOCTUA software suite as a side deliverable |
| TU-Eindhoven | RESTART | C, M | 2 | Two-receptor synNotch cascade as a sequential AND gate on HLA-A2 then VCAM-1 |
| U Copenhagen | Lutealine | C | 1 | Hormone-cycle-responsive ADHD dosing; no construct or mechanism described |
| UAlberta | gleyeco | C, M | 2 | Engineered lectins optimised by in silico mutagenesis and binding simulation, delivered from a hydrogel contact lens |
| UC Davis | INDIGO | C | 2 | TF-antigen-binding oligopeptides for localisation plus an RNA-thermometer kill switch keyed to body temperature |
| UCAS-China | PARCEL | C, M | 2 | ELP phase separation builds Pum2-captured mRNA micelles; Sortase A conjugates the targeting antibody |
| UCS-B | Living Factory (L-asparaginase) | M | 2 | Region-specific mutagenesis at tetramer interface and substrate entry, with a signal-peptide screen for secretion |
| UI-ITB-Indonesia | BELL10 | M | 2 | Reports 126.70 ± 8.73 pg/mL IL-10, 59 nm vesicles, and that prolonged treatment killed the cells |
| ULP-CA | SulFlux | M | 1 | Sulfotransferase remodelled to accept lithocholic acid; folding and activity not yet established |
| UManitoba | H.A.L.T. - UTI | C, M | 2 | Surface display verified with GFP, adhesins and binders purified, *L. crispatus* in hydrogel in simulated vaginal fluid |
| Worldshaper-SHMed | AdipoSense | C, M | 2 | Succinate-high/butyrate-low AND-NOT logic demonstrated in vitro, with a plant-derived NAPE gene as output |
| XJTLU | FOLLICoffee | C, H, M | 3 | OxyR–PkatG H₂O₂ sensing with surface-displayed alginate lyase, aiming to link peroxide dose quantitatively to release |
