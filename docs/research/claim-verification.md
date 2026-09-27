# Appendix A: Claim-by-claim verification of the README

> Machine-generated research digest produced alongside the project brief. Each entry cites the sources the reviewing agent found. Treat it as a starting point for your own reading, not as vetted medical advice.


Each README claim was checked under two lenses: **evidence** (best human data, magnitude, replication) and **safety** (who could be harmed if the engine told them to add this).

| ID | Claim | Evidence lens | Safety lens |
|---|---|---|---|
| C1 | Adding vitamin C (citrus) to plant foods chemically reduces ferric (Fe3+) iron to ferrous (Fe2+) iron, increasing absorption and overriding […] | partially_supported (high) | partially_supported (high) |
| C2 | Vitamin C reduces ferric iron - presented as an immutable biochemical law suitable for a hard graph edge. | partially_supported (high) | partially_supported (high) |
| C3 | Co-ingesting black pepper (piperine) and fat with turmeric increases curcumin bioavailability by up to 2,000%. | overstated (high) | overstated (high) |
| C4 | In a person with high fasting insulin, Ceylon cinnamon + magnesium + acetic acid 'structurally activate' GLUT4 glucose transporters in […] | overstated (high) | overstated (high) |
| C5 | Elevated creatine kinase and hs-CRP together flag severe tissue damage and systemic inflammation. | overstated (high) | overstated (high) |
| C6 | Vitamin C, copper and proline are the precise co-factors for collagen synthesis and supplying them supports 'structural repair' after […] | overstated (high) | overstated (high) |
| C7 | The gut microbiome contains redundant metabolic pathways such that when a primary strain is depleted, other surviving bacteria can be fed […] | partially_supported (high) | overstated (high) |
| C8 | Urolithin A and short-chain fatty acids are microbially synthesised 'critical recovery compounds'. | partially_supported (high) | partially_supported (high) |
| C9 | Fitness enthusiasts as a cohort have complete micronutrient and bioavailability blindness despite precise macro tracking. | overstated (medium) | overstated (medium) |
| C10 | Gym-goers routinely mega-dose competing supplements (implying supplement-supplement absorption competition is common and consequential). | overstated (high) | overstated (medium) |
| C11 | Combining clashing food matrices causes 'anabolic waste' (i.e. lost muscle-building potential from nutrient interactions). | unsupported (high) | unsupported (high) |
| C12 | Heavy protein and sweetener intake causes broad-spectrum gut dysbiosis in this cohort. | overstated (high) | overstated (high) |
| C13 | A single night of poor sleep can completely alter metabolic and gut-microbial state. | overstated (high) | overstated (high) |
| C14 | Human biology is chaotic, non-linear and non-replicable, unpredictable moment to moment. | overstated (high) | overstated (high) |
| C15 | Blood biomarkers can prove whether a dietary recommendation influenced the body. | overstated (high) | overstated (high) |
| C16 | Eating a recommended meal alters internal small-molecule metabolomics in a way measurable by blood panels (hs-CRP, fasting insulin, […] | overstated (high) | overstated (high) |
| C17 | Sequential blood tests can be used by ML to learn exactly how a specific individual reacts to micro-additive nutritional changes. | overstated (high) | overstated (high) |
| C18 | Blood anomalies can be mapped directly to actionable dietary solutions. | overstated (high) | overstated (high) |
| C19 | The laws of chemistry and taxonomic microbiology relevant to nutrition are rigid and immutable, i.e. context-free enough to be graph edges. | overstated (high) | overstated (high) |
| C20 | Ingredients compete for enterocyte transporters (nutrient-nutrient absorption competition at the gut wall). | partially_supported (high) | partially_supported (high) |
| C21 | Adding companion ingredients can multiply performance, absorption and recovery. | overstated (high) | overstated (high) |
| C22 | Semantic embedding of subjective state (e.g. 'sore') can be matched to biological recovery pathways. | partially_supported (medium) | overstated (high) |
| C23 | Generic clinical/fitness advice ('balanced diet, regular exercise') is fundamentally true but lacks specificity and actionability. | partially_supported (high) | partially_supported (high) |
| C24 | Standard biological databases are heavily siloed but can be joined via universal identifiers; […] | partially_supported (high) | partially_supported (high) |
| C25 | ArcadeDB combines a native graph engine, an LSM-powered vector search engine and a document store under a single ACID transaction boundary, […] | partially_supported (high) | partially_supported (high) |
| C26 | The project's domain is metabolomics and nutrigenomics, and blood panels can deliver 'metabolomics & nutrigenomics' diagnostics. | overstated (high) | overstated (high) |
| C27 | Medicine interactions and allergies can be made uniquely traceable per user from medical research and open data. | partially_supported (high) | overstated (high) |
| C28 | The system's outputs carry no liability; validity is established only by observed effectiveness, data quality and individual response. | unsupported (high) | overstated (high) |


## C1. Adding vitamin C (citrus) to plant foods chemically reduces ferric (Fe3+) iron to ferrous (Fe2+) iron, increasing absorption and overriding the inhibitory effect of plant phytates.

**README says:** "Adding a squeeze of citrus (Vitamin C) to plant-based greens to chemically reduce ferric iron into highly absorbable ferrous iron, overriding native plant phytate inhibitors."

**Evidence verdict:** partially_supported (confidence high). Grade: Single-meal absorption effect: multiple independent human crossover radioisotope trials, replicated across labs (Gothenburg, Johannesburg, Seattle/Kansas) and decades, cumulative n > 800 (Hallberg […]

**Honest version:** Ascorbic acid eaten in the same meal reliably raises non-heme iron absorption from plant foods in a dose-dependent way (roughly 2-3x at 15-30 mg, 3-4x at 50-100 mg, up to ~6-10x at 250-1000 mg, from a low baseline of ~1-4% absorption), and it partially counteracts phytate and polyphenol inhibition rather than "overriding" it: ~30 mg overcame 10-58 mg phytate-P in a bread meal, and a molar ratio of ~2:1 ascorbate:iron (about 20 mg per 3 mg Fe) is needed for low/medium-inhibitor meals and >4:1 for high-inhibitor meals. The mechanism is reduction of Fe3+ to Fe2+ plus formation of a soluble iron-ascorbate chelate that survives the duodenal pH shift (Fe2+ then enters via DMT1, with ascorbate-fed […]

**Key evidence:** FOR (single meal, human radioisotope): Cook & Monsen 1977 (63 men, semisynthetic meal): absorption ratio with/without ascorbic acid 1.65 at 25 mg rising to 9.57 at 1000 mg, proportional to dose; effect much smaller when meal contained meat; a morning dose did not affect noon/evening meals. Hallberg, Brune & Rossander 1986 (299 subjects): biggest enhancement in meals with high phytate/tannin content; native food vitamin C and crystalline ascorbic acid equally effective; ~50 mg per main meal recommended for optimum effect. Ballot 1987 (234 Indian women, rice meal): baseline absorption 2.5%; 100 mL orange juice (28 mg AA) 13.9% (5.6x); 33 mg AA in water alone 5.9% vs 9.7% when 750 mg citric acid added; adding 4 g citric acid to orange juice raised 16.6% to 22.6%; guava/papaya 12.6-29.3%; correlation with fruit AA content rs 0.738; grape/apple/peach no effect. Gillooly 1983 (Indian women): 15 mg AA raised rice-meal absorption 3.1% to 8.1%; 1 g citric acid 2.8% to 8.5%; spinach absorption 1.4%, beetroot greens 2.4%, broccoli 26%, cabbage 32%; tannic acid cut broccoli 29.7% to 1.5%; […]

**Magnitude:** Single-meal absorption (relative): 15 mg AA ~2.6x (3.1 to 8.1%); 25 mg ~1.65x; 28 mg as orange juice ~5.6x (2.5 to 13.9%); 30 mg fully reverses 10-58 mg phytate-P inhibition; 50-100 mg ~3-4x; 1000 mg ~9.6x. Absolute terms: for a 4 mg-iron plant meal, going from 2.5% to 13.9% absorption is 0.10 mg to 0.56 mg iron absorbed, i.e., +0.46 mg per meal. Phytate inhibition to be overcome: -18% at 2 mg phytate-P, -64% at 25 mg, -82% at 250 mg. Required […]

**Safety caveats:** (1) Iron overload is the primary population risk: HFE hereditary hemochromatosis (C282Y homozygous ~1 in 150-300 of Northern European ancestry; majority undiagnosed in midlife per UK Biobank), transfusional overload (thalassemia, sickle cell, MDS), and anyone on iron chelation. In HH hepcidin is deficient, so the physiological brake that makes vitamin C's whole-diet effect small in normal people is absent; enhancers act unopposed, and ascorbate additionally promotes cellular uptake of non-transferrin-bound iron and redox toxicity when iron is in excess (Lane & Richardson 2014; Omena 2021). NIDDK: avoid vitamin C-containing supplements and iron supplements; LPI: high-dose vitamin C regimens may worsen overload. A single lemon squeeze (2-4 mg) is not a supplement and per NIDDK phlebotomy […]

**What this means for the engine:** 1) Re-type this edge from a binary "companion pair unlock" to a dose-dependent, meal-scoped, status-gated rule. Weight = f(mg ascorbate in meal, mg non-heme Fe in meal, inhibitor load class, presence of meat, user iron status). Practical thresholds from the literature: require AA:Fe molar ratio >= 2:1 (about 6.3 mg AA per mg Fe) for […]

**Sources:**
- [Hallberg L, Brune M, Rossander L. Iron absorption in man: ascorbic acid and dose-dependent […]](https://doi.org/10.1093/ajcn/49.1.140)
- [Siegenberg D et al. Ascorbic acid prevents the dose-dependent inhibitory effects of polyphenols and […]](https://doi.org/10.1093/ajcn/53.2.537)
- [Hallberg L, Brune M, Rossander L. Effect of ascorbic acid on iron absorption from different types […]](https://europepmc.org/article/MED/3700141)
- [Cook JD, Monsen ER. Vitamin C, the common cold, and iron absorption. Am J Clin Nutr 1977;30:235-41 […]](https://doi.org/10.1093/ajcn/30.2.235)
- [Ballot D et al. The effects of fruit juices and fruits on the absorption of iron from a rice meal. […]](https://doi.org/10.1079/bjn19870041)
- [Gillooly M et al. The effects of organic acids, phytates and polyphenols on the absorption of iron […]](https://doi.org/10.1079/bjn19830042)

## C2. Vitamin C reduces ferric iron - presented as an immutable biochemical law suitable for a hard graph edge.

**README says:** "Immutable Biochemical Laws (e.g., Vitamin C reduces Ferric Iron)"

**Evidence verdict:** partially_supported (confidence high). Grade: Mixed by sub-claim. Chemistry (Fe3+ reduction, chelation): established in-vitro/mechanistic chemistry, not contested. Dcytb mechanism: animal + structural biology (mouse cDNA and Xenopus expression, […]

**Honest version:** Two different claims are bundled here and they deserve different graph treatment. (1) CHEMISTRY, true and effectively immutable: ascorbate donates electrons to Fe3+, producing Fe2+ and dehydroascorbate, and additionally chelates iron at gastric pH into complexes that stay soluble at duodenal pH (Conrad & Schade 1968; Hallberg 1989 review names both mechanisms; Teucher 2004). A brush-border enzyme, Dcytb, uses ascorbate as the electron donor to reduce luminal Fe3+ (McKie 2001; crystal structure Ganasen 2018). (2) PHYSIOLOGY, true but conditional and quantitatively bounded: co-ingested ascorbic acid increases NON-HEME iron absorption from THAT meal in a dose-dependent way (25 mg ≈ 1.65x, 1000 […]

**Key evidence:** FOR (acute, single meal): Cook & Monsen 1977 AJCN, 63 men, radioiron: absorption ratio with/without ascorbic acid rose linearly from 1.65 (25 mg) to 9.57 (1,000 mg) on a semisynthetic meal; 'substantially less when the test meal contained meat'; a large breakfast dose 'did not affect iron absorption from the noon or evening meal'. Hallberg, Brune & Rossander 1986, 299 subjects: enhancement varied markedly by meal, largest in high-phytate/tannin meals; crystalline and food-native ascorbic acid equivalent; '~50 mg in each main meal is desirable for optimum effect'. Hallberg 1989 AJCN: phytate-P 2 mg inhibited absorption 18%, 25 mg 64%, 250 mg 82%; ascorbic acid 'significantly counteracted' the inhibition. Siegenberg 1991 AJCN, 199 subjects: 30 mg ascorbic acid overcame phytate-P of 10-58 mg; ≥50 mg required for meals with >100 mg tannic acid. Gillooly 1983 Br J Nutr (Indian women, radioiron): 15 mg ascorbic acid raised absorption 3.1% -> 8.1%; 1 g citric acid 2.8% -> 8.5%; spinach absorption 1.4% vs broccoli 26%, cabbage 32%; polyphenol content inversely correlated with absorption […]

**Magnitude:** Acute single-meal non-heme iron absorption: 25 mg AA ≈ 1.65x; 50 mg ≈ 2-3x; 100 mg ≈ 3-4x; 250-500 mg ≈ 5-7x; 1,000 mg ≈ 9.6x (semisynthetic meal, no meat); 15 mg raised absorption from 3.1% to 8.1% in a vegetable meal. Absolute context: baseline non-heme absorption is roughly 2-20% (spinach 1.4%, wheat roll ~22% reference, broccoli/cabbage 26-32%); mixed diets 14-18% and vegetarian diets 5-12% overall bioavailability. Whole-diet: 51-247 mg/d -> […]

**Safety caveats:** WHO IS HARMED BY AN "ADD" RECOMMENDATION THAT RAISES IRON ABSORPTION: (1) HFE hemochromatosis (diagnosed or, more dangerously, undiagnosed): ~1 in 150 people of northern-European ancestry are C282Y homozygotes; men are the penetrant sex (28.4% develop iron-overload disease; 84% have raised ferritin by mid-50s). The README's target demographic ("gym rats", disproportionately young men who already take vitamin C, iron-fortified products and red meat) overlaps this group. AASLD 1C: vitamin C supplements and iron supplements should be avoided; pharmacologic vitamin C can saturate transferrin, raise free-radical activity, and in advanced disease with arrhythmia/cardiomyopathy carries risk of sudden death; McLaran 1982 fatal cardiomyopathy after 12 months of high-dose ascorbic acid in an […]

**What this means for the engine:** 1. Do not model this as one boolean 'hard edge'. Split into (a) a chemistry/reaction node 'ascorbate + Fe3+ -> dehydroascorbate + Fe2+' (immutable, ChEBI/KEGG-mappable, but not actionable by itself) and (b) a physiological edge 'ascorbic acid ENHANCES non-heme iron absorption' carrying typed attributes: dose_mg_in_meal, molar_ratio_AA_to_Fe, […]

**Sources:**
- [Cook JD, Monsen ER. Vitamin C, the common cold, and iron absorption. Am J Clin Nutr 1977 (PMID […]](https://pubmed.ncbi.nlm.nih.gov/835510/)
- [Hallberg L, Brune M, Rossander L. Effect of ascorbic acid on iron absorption from different types […]](https://pubmed.ncbi.nlm.nih.gov/3700141/)
- [Hallberg L, Brune M, Rossander L. Iron absorption in man: ascorbic acid and dose-dependent […]](https://pubmed.ncbi.nlm.nih.gov/2911999/)
- [Hallberg L, Brune M, Rossander L. The role of vitamin C in iron absorption. Int J Vitam Nutr Res […]](https://pubmed.ncbi.nlm.nih.gov/2507689/)
- [Siegenberg D et al. Ascorbic acid prevents the dose-dependent inhibitory effects of polyphenols and […]](https://pubmed.ncbi.nlm.nih.gov/1989423/)
- [Gillooly M et al. The effects of organic acids, phytates and polyphenols on the absorption of iron […]](https://doi.org/10.1079/bjn19830042)

## C3. Co-ingesting black pepper (piperine) and fat with turmeric increases curcumin bioavailability by up to 2,000%.

**README says:** "Pairing black pepper (piperine) and fat with turmeric to boost curcumin bioavailability by up to 2,000%."

**Evidence verdict:** overstated (confidence high). Grade: Piperine component: single human crossover PK study (n=10, 1998, co-authored by the manufacturer of the piperine product), never replicated at that magnitude; subsequent human PK comparisons (n=8-16, […]

**Honest version:** In one small, industry-linked 1998 crossover study (10 healthy men), taking 20 mg of purified piperine with a 2 g curcumin supplement raised the area-under-curve of total (conjugated + free) serum curcumin about 20-fold ("2000%") over a 1-2 h window. That 20-fold is relative to a baseline that was essentially undetectable (0.006 +/- 0.005 ug/mL at 1 h), so absolute levels remained trace, and free/unconjugated curcumin has still never been reliably measured in humans even with piperine. Later head-to-head human pharmacokinetic comparisons show curcumin+piperine products absorbing roughly the same as plain curcumin (~1.1x) and being outperformed 6-46x by lipid/dispersion formulations. The […]

**Key evidence:** FOR (source of the figure): Shoba et al., Planta Med 1998;64:353-6 (PMID 9619120). Rats: 2 g/kg curcumin +/- 20 mg/kg piperine -> bioavailability +154%. Humans: 2 g curcumin alone -> serum levels "undetectable or very low" (0.006 +/- 0.005 ug/mL at 1 h per Prasad 2014 quoting the paper); with 20 mg piperine -> higher levels at 0.25-1 h, "increase in bioavailability was 2000%". Tabanelli 2021 (Pharmaceutics) describes it as 10 healthy adult males, randomized crossover, ~20-fold AUC increase. Co-author M. Majeed founded Sabinsa (1988), which markets BioPerine (piperine) and Curcumin C3 Complex (Sabinsa about-us page); a Majeed/Badmaev US patent (5,536,506) covers using piperine to raise nutrient bioavailability. The "2000%" then propagated via reviews such as Hewlings & Kalman 2017 (Foods), which restates it without qualification. Mechanism (real): piperine inhibits intestinal/hepatic glucuronidation (UGT), SULT, CYP3A4 and P-gp; Volak 2008 (Drug Metab Dispos) in vitro: piperine is a relatively selective CYP3A4 inhibitor (IC50 5.5 uM); rat study (Biopharm Drug Dispos 2017) shows only […]

**Magnitude:** Primary study (Shoba 1998, n=10): total serum curcumin AUC ~20x (reported "+2000%") after 2 g curcumin + 20 mg piperine vs 2 g alone; baseline 0.006 +/- 0.005 ug/mL at 1 h (i.e. near/below detection); rat arm +154%. Independent human comparisons: curcumin-lecithin-piperine ~1.1x plain curcumin (derived from Antony 2008: 6.93/6.3); 95% curcuminoids + 1% piperine Cmax 10.94 ng/mL vs 663.6 ng/mL with 10% piperine (Malhotra 2025, n=4-5 per arm); 3 x […]

**Safety caveats:** POPULATIONS WHO COULD BE HARMED BY AN "ADD PEPPER + TURMERIC + FAT" RECOMMENDATION: (a) Anyone on CYP3A4, P-gp or UGT substrate drugs with narrow therapeutic index, because piperine at seasoning doses (15-20 mg, ~0.2-0.5 g pepper) is a proven in-vivo inhibitor: antiepileptics (phenytoin, carbamazepine - documented in epilepsy patients), theophylline, propranolol/beta-blockers, midazolam/benzodiazepines, nevirapine/NNRTIs, and by mechanism tacrolimus/cyclosporine, digoxin, some statins and calcium-channel blockers. Velpandian 2001 used pepper in soup, so this is a food-dose hazard, not just a supplement hazard; risk rises with daily repeated exposure (Volak's 2-day null result vs Bano/Rezaee/Kasibhatta multi-day positives). (b) Transplant recipients on tacrolimus: documented AKI with […]

**What this means for the engine:** (1) Do not hard-code "+2000%" as an edge weight. Encode the piperine->curcumin relationship as: effect on TOTAL curcuminoid AUC, single-study, n=10, manufacturer-linked, measured against a near-zero baseline, non-replicated; expected practical increment from later comparisons ~1.1x-2x at supplement doses; unknown at spice doses. The graph should […]

**Sources:**
- [Shoba G et al. Influence of piperine on the pharmacokinetics of curcumin in animals and human […]](https://pubmed.ncbi.nlm.nih.gov/9619120/)
- [Prasad S et al. Recent developments in delivery, bioavailability, absorption and metabolism of […]](https://doi.org/10.4143/crt.2014.46.1.2)
- [Tabanelli R et al. Improving Curcumin Bioavailability: Current Strategies and Future Perspectives. […]](https://doi.org/10.3390/pharmaceutics13101715)
- [Sabinsa Corporation - About Us (founded 1988 by Dr Muhammed Majeed; BioPerine and Curcumin C3 […]](https://www.sabinsa.com/about-us)
- [Hewlings SJ, Kalman DS. Curcumin: A Review of Its Effects on Human Health. Foods 2017 (restates the […]](https://doi.org/10.3390/foods6100092)
- [Volak LP et al. Effect of a herbal extract containing curcumin and piperine on midazolam, […]](https://doi.org/10.1111/j.1365-2125.2012.04364.x)

## C4. In a person with high fasting insulin, Ceylon cinnamon + magnesium + acetic acid 'structurally activate' GLUT4 glucose transporters in muscle tissue, and this is an appropriate response to that biomarker.

**README says:** "High Fasting Insulin: The engine traverses paths to recommend Ceylon Cinnamon + Magnesium + Acetic Acid to structurally activate GLUT4 glucose transporters in muscle tissue."

**Evidence verdict:** overstated (confidence high). Grade: Mixed by component and by sub-claim. GLUT4 "activation" by any of the three: in-vitro (C2C12/L6 myotubes, 3T3-L1 adipocytes) and rodent only; "structural activation" itself = mechanistic […]

**Honest version:** Each of the three ingredients has some human evidence for modest, inconsistent improvement in glycaemic markers, but none is shown to lower fasting insulin reliably, the GLUT4 link is in-vitro/rodent only, "structural activation" is not a real mechanism (GLUT4 acts by translocation, driven by insulin/Akt or contraction/AMPK signalling), and the triple combination has never been tested. Honest statement: (1) Cinnamon (almost all RCTs used cassia, 1-6 g/day, 6-16 weeks) lowers fasting glucose ~11 mg/dL and HOMA-IR ~0.6 in small, heterogeneous (I2 ~84%), mostly high/unclear-risk-of-bias trials; the fasting-insulin effect is small and unstable (WMD -2.0 uIU/mL with CI touching zero in the 2023 […]

**Key evidence:** MECHANISM. GLUT4 mediates glucose entry into muscle by translocating from intracellular vesicles to the plasma membrane/T-tubules in response to insulin (PI3K/Akt) or contraction (AMPK, Ca2+, Rac1); chronic GLUT4 expression is upregulated most potently by exercise training via AMPK/CaMKII-HDAC-MEF2 (Richter & Hargreaves 2013, Physiol Rev; Klip 2019, JBC). Richter 2021 notes that exercise raises muscle glucose uptake up to 100-fold but measured GLUT4 translocation only ~2-fold, and that a change in GLUT4 "intrinsic activity" is an unproven hypothesis even for exercise; no source describes any nutrient "structurally activating" GLUT4. Cinnamon-GLUT4: cinnamon extract increased GLUT4 translocation in C2C12 myotubes and 3T3-L1 adipocytes via LKB1-AMPK (Shen 2014; hydro-alcoholic extract in C2C12, 2012); in type-2 diabetic model rats cinnamon extract improved oral glucose tolerance but NOT insulin sensitivity on an insulin tolerance test (Shen 2014). Acetic acid-GLUT4: acetic acid phosphorylated AMPK and increased GLUT4 and myoglobin expression and glucose uptake in L6 myotubes and in […]

**Magnitude:** Cinnamon (pooled RCTs, mostly cassia): FPG -10.9 mg/dL (95% CI -16.2 to -5.7); fasting insulin -2.0 uIU/mL (-3.96 to -0.07) in umbrella meta, SMD -0.17 (NS) in 24-RCT meta, SMD -0.26 (-0.50 to -0.02) in 49-study GRADE meta; HOMA-IR -0.61 (-0.91 to -0.31) to -0.71 (-1.39 to -0.04), I2 ~84%; HbA1c -0.10% (-0.17 to -0.03). Ceylon-specific: 6 g acute = no effect on postprandial glucose/insulin (n=10); 1 g/day x 12 wk = FBS -8.6 mg/dL (0.6 to 16.6), […]

**Safety caveats:** The "add-only" framing does not remove harm: adding is dosing, and each of these three has a ceiling, contraindicated populations and drug interactions. CINNAMON: (1) Species/coumarin: "cinnamon" in a typical kitchen or supplement is Cassia (C. cassia/burmannii; Wang 2013: US products are mostly C. burmannii). Cassia contains ~3,000 mg/kg coumarin (up to 10,000 mg/kg); TDI is 0.1 mg/kg bw/day, reached at ~2 g Cassia/day for a 60 kg adult and ~0.5 g for a 15 kg child (BfR). Supplement-style doses used in the positive trials (1-6 g/day) exceed the TDI unless the product is verified C. verum. A susceptible human subgroup develops reversible hepatotoxicity (raised enzymes to jaundice) at coumarin exposures near therapeutic doses (Abraham 2010; BfR). Case reports of cinnamon-supplement liver […]

**What this means for the engine:** 1) Separate mechanism edges from outcome edges and tag each with evidence tier and organism: "cinnamon extract -> AMPK -> GLUT4 translocation" is an in-vitro C2C12/3T3-L1 edge; "cinnamon -> lower fasting glucose" is a human-RCT edge with CI and I2; never let an in-vitro edge inherit the weight of a human outcome edge. 2) Delete "structurally […]

**Sources:**
- [Leach & Kumar 2012, Cinnamon for diabetes mellitus (Cochrane Review)](https://pubmed.ncbi.nlm.nih.gov/22972104/)
- [Zarezadeh 2023, umbrella meta-analysis of cinnamon on glycemic control in T2D/PCOS](https://pubmed.ncbi.nlm.nih.gov/37316893/)
- [Moridpour 2024, updated dose-response meta-analysis of cinnamon in T2DM (24 RCTs)](https://pubmed.ncbi.nlm.nih.gov/37818728/)
- [Jafari 2025, GRADE-assessed meta-analysis of cinnamon on cardiovascular risk factors (49 studies)](https://pubmed.ncbi.nlm.nih.gov/40611215/)
- [Deyno 2019, cinnamon in T2DM and prediabetes: meta-analysis and meta-regression](https://pubmed.ncbi.nlm.nih.gov/31425768/)
- [Kutbi 2022, cinnamon in metabolic diseases: dose-response meta-analysis](https://pubmed.ncbi.nlm.nih.gov/33739219/)

## C5. Elevated creatine kinase and hs-CRP together flag severe tissue damage and systemic inflammation.

**README says:** "Elevated Creatine Kinase (CK) / hs-CRP: Flags severe tissue damage and systemic inflammation"

**Evidence verdict:** overstated (confidence high). Grade: Mixed. (1) CK as a marker of skeletal-muscle membrane disruption: human experimental studies (n=10 to 499) plus narrative/systematic reviews - solid at the group level, weak for individual severity […]

**Honest version:** Serum creatine kinase (CK) is a marker that skeletal-muscle (or cardiac) fibre membranes have recently leaked; high-sensitivity CRP is a nonspecific hepatic acute-phase marker. Neither, alone or together, grades "severity" of tissue damage. In a training population CK rises after essentially every hard or unaccustomed session (peak 24-96 h, baseline again by ~7-10 days), varies >100-fold between healthy people doing the identical workout (236-25,244 U/L after 24 eccentric curls), and routinely exceeds published rhabdomyolysis cut-offs (51 of 203 healthy volunteers >10,000 U/L after one eccentric bout) with zero kidney impairment. "Severe" is a clinical syndrome (weakness, swelling, myalgia, […]

**Key evidence:** CK MAGNITUDE AND VARIABILITY IN HEALTHY HUMANS. Clarkson 2006 (n=203, 50 maximal eccentric elbow-flexor contractions): CK +6,420% over baseline at day 4; 111/203 >2,000 U/L and 51/203 >10,000 U/L; no significant change in any renal measure, no myoglobinuria, nobody treated. Kenney 2012 (n=499 military recruits, 14 days): median CK 157 -> 567 IU/L by day 7, range 34-35,056 IU/L, zero cases of clinical exertional rhabdomyolysis; authors conclude >50x ULN is the more specific threshold and that African-American recruits have higher CK. Nosaka & Clarkson 1996 (n=10, identical protocol): peak CK 236-25,244 IU/L; but within-study peak CK did correlate with force loss (r=0.73-0.79) and MRI signal change (r=0.90-0.94). Kim & Lee 2015 (n=119): high CK responders had larger strength loss and soreness than low responders; %body fat higher in high responders. Paulsen 2005 (n=11, 300 eccentric actions): force -47%; CK peaked day 4, CRP day 2; both correlated with acute force loss at only r=0.65. Fridén & Lieber 2001 (rabbit, n=26): CK explained ~8% of torque variance (animal). Net: CK tracks […]

**Magnitude:** CK after one unaccustomed eccentric bout in healthy adults: +6,420% at day 4 (n=203); 55% of subjects >2,000 U/L, 25% >10,000 U/L, renal function unchanged. Inter-individual range for the same workout: 236-25,244 IU/L (n=10) and 34-35,056 IU/L (n=499). Resting biological variation: CVI 14.5%, CVG 31.5%. True population ULN 2-5x the manufacturer's; 49% of Black adults exceed the kit ULN at rest. Athlete ULN 1,083 U/L (men), up to 1,492 U/L in […]

**Safety caveats:** 1) Missed medical diagnoses are the dominant harm, not the food: a CK/hs-CRP flag that pins a "Structural Repair" vector and outputs food pairings can delay care for exertional rhabdomyolysis (risk higher in sickle cell trait HR 1.54, statin users HR 2.89, antipsychotic users HR 3.02, young men, Black service members, novices/CrossFit-style high-volume sessions), statin myopathy (CK >10x ULN is a stop-drug event), hypothyroidism (57% of overt cases have raised CK), and hs-CRP >10 mg/L from infection, autoimmune disease or malignancy. 2) The README's "liability: there is none" stance is incompatible with a system that interprets clinical labs. 3) Hemochromatosis/iron overload: AASLD says avoid vitamin C supplements (1C); the same engine already recommends citrus with iron-rich greens - for […]

**What this means for the engine:** 1. Rename the state. "Elevated CK + hs-CRP" should map to "recent high muscle-damaging or endurance load (last 1-3 days)" or "possible illness/injury - not a nutrition state", never to "severe tissue damage". 2. Make CK uninterpretable without a training-log timestamp: every CK value must be joined to hours-since-last-hard-session and session type […]

**Sources:**
- [Clarkson PM et al. 2006. Serum creatine kinase levels and renal function measures in exertional […]](https://pubmed.ncbi.nlm.nih.gov/16679975/)
- [Kenney K et al. 2012. Serum creatine kinase after exercise: drawing the line between physiological […]](https://pubmed.ncbi.nlm.nih.gov/22334169/)
- [Nosaka K, Clarkson PM. 1996. Variability in serum creatine kinase response after eccentric exercise […]](https://pubmed.ncbi.nlm.nih.gov/8833714/)
- [Kim J, Lee J. 2015. The relationship of creatine kinase variability with body composition and […]](https://pubmed.ncbi.nlm.nih.gov/26244131/)
- [Paulsen G et al. 2005. Delayed leukocytosis and cytokine response to high-force eccentric exercise. […]](https://pubmed.ncbi.nlm.nih.gov/16286856/)
- [Paulsen G et al. 2012. Leucocytes, cytokines and satellite cells: what role do they play in muscle […]](https://pubmed.ncbi.nlm.nih.gov/22876722/)

## C6. Vitamin C, copper and proline are the precise co-factors for collagen synthesis and supplying them supports 'structural repair' after tissue damage.

**README says:** "surfacing precise collagen-synthesis co-factors (Vitamin C + Copper + Proline)"

**Evidence verdict:** overstated (confidence high). Grade: Mechanism (vitamin C for prolyl/lysyl hydroxylases; copper for lysyl oxidase): established biochemistry + human deficiency states (strong). Proline as a 'cofactor': incorrect categorisation; proline […]

**Honest version:** Vitamin C is a genuine co-substrate for the prolyl- and lysyl-hydroxylases that stabilise procollagen (alongside Fe2+, 2-oxoglutarate and O2, which the README omits), and copper is the cofactor of lysyl oxidase, which cross-links secreted collagen/elastin. Deficiency of either demonstrably weakens connective tissue (scurvy; Menkes/zinc-induced copper depletion). Proline, however, is a substrate, not a cofactor; it is non-essential, and animal wound-model reviews report that extra dietary proline does not increase collagen deposition, whereas arginine does (human wound-catheter RCT, n=36, hydroxyproline ~2.4x). Glycine (33% of collagen residues) and lysine are at least as relevant as […]

**Key evidence:** FOR (mechanism): Gorres & Raines 2010 (Crit Rev Biochem Mol Biol)  -  prolyl 4-hydroxylase is an Fe2+/2-oxoglutarate-dependent dioxygenase requiring ascorbate; Hyp stabilises the triple helix. Rucker 1998 (AJCN)  -  lysyl oxidase is a cuproenzyme; dietary copper controls LOX functional activity post-translationally without changing LOX protein/mRNA. Linus Pauling Institute  -  vitamin C is cofactor for 3 prolyl-4-hydroxylase, 3 prolyl-3-hydroxylase and 3 lysyl-hydroxylase isoenzymes; scurvy = poor wound closure, bleeding; prevented by as little as 10 mg/day; plasma >=50 umol/L saturates muscle tissue. Levine 1996 (PNAS, n=7 depletion-repletion)  -  first dose beyond the steep part of the plasma curve is 200 mg/day; complete plasma saturation at 1000 mg/day; single doses >=500 mg are largely excreted; oxalate/urate excretion rises at 1000 mg/day. EFSA 2009 (EFSA Journal 7(9):1226 and 1211, verified via Crossref) authorised only 'normal collagen formation' and 'maintenance of normal connective tissues' claims, i.e. adequacy claims, not repair claims.
FOR (human surrogate): Shaw et al […]

**Magnitude:** Vitamin C + gelatin/collagen on serum PINP: ~2x (n=8, 15 g gelatin + 48 mg C); ~+20% non-significant (n=10). Muscle connective-tissue FSR after 30 g collagen: 0.068 vs 0.058 %/h placebo, NS p=0.09 (n=45). Tendon adaptation over 14-15 wk RT: Achilles CSA +11.0% vs +4.7% (n=40, Gelita) vs patellar tendon no between-group difference, stiffness +17.3% vs +20.9% (n=39, independent). RFD recovery with 20 g HC + 50 mg C: recovered to baseline vs […]

**Safety caveats:** POPULATIONS AT RISK IF THE ENGINE SAYS "ADD": (1) Hemochromatosis/iron overload (incl. thalassemia): vitamin C increases non-heme iron absorption and counteracts phytate inhibition in single meals (Hallberg 1989); MSKCC lists hemochromatosis as a do-not-take condition; Herbert 1999 Ann Intern Med. Effect from a whole diet is much smaller than single-meal studies (Cook & Reddy 2001, 51-247 mg/day range), so food-dose risk is modest but the engine's own citrus-with-iron companion pair compounds it. (2) Recurrent stone formers, CKD, dialysis, renal transplant, post-Roux-en-Y gastric bypass: supplemental vitamin C raises urinary oxalate; cohort risk ~1.2-1.9x in men; case reports of acute oxalate nephropathy with high-dose vitamin C in transplant recipients and post-RYGB patients (Shen 2023, […]

**What this means for the engine:** (a) Fix the node set: replace 'Vitamin C + Copper + Proline' with typed edges: COFACTOR edges {ascorbate, Fe2+, 2-oxoglutarate, O2} -> prolyl-4-hydroxylase/lysyl-hydroxylase; {Cu} -> lysyl oxidase; SUBSTRATE edges {glycine 33%, proline+hydroxyproline 23%, lysine} -> procollagen; PRECURSOR edge {arginine -> ornithine -> proline} (only amino acid […]

**Sources:**
- [Shaw et al. 2017, Vitamin C-enriched gelatin supplementation before intermittent activity augments […]](https://pubmed.ncbi.nlm.nih.gov/27852613/)
- [Lis & Baar 2019, Effects of different vitamin C-enriched collagen derivatives on collagen synthesis […]](https://pubmed.ncbi.nlm.nih.gov/30859848/)
- [Lis et al. 2022, Collagen and vitamin C supplementation increases lower limb rate of force […]](https://pubmed.ncbi.nlm.nih.gov/34808597/)
- [Aussieker et al. 2023, Collagen protein ingestion during recovery from exercise does not increase […]](https://pubmed.ncbi.nlm.nih.gov/37202878/)
- [Balshaw et al. 2023, Effect of specific bioactive collagen peptides on tendon remodeling during 15 […]](https://pubmed.ncbi.nlm.nih.gov/37436929/)
- [Jerger et al. 2022, Specific collagen peptide supplementation with resistance training on Achilles […]](https://pubmed.ncbi.nlm.nih.gov/35403756/)

## C7. The gut microbiome contains redundant metabolic pathways such that when a primary strain is depleted, other surviving bacteria can be fed specific prebiotic fibres or polyphenols to synthesise the same recovery compounds.

**README says:** "Scans the user's microbiome profile to find redundant metabolic pathways. If a primary strain is depleted, it recommends adding specific prebiotic fibres or polyphenols to feed surviving bacteria capable of synthesizing critical recovery compounds"

**Evidence verdict:** partially_supported (confidence high). Grade: SPLIT. Sub-claim 1 (redundancy exists): STRONG  -  large-cohort human metagenomics (HMP, n=242, 18 body sites), ultra-deep human metaproteomics, and a 4,912-metagenome/28-cohort computational […]

**Honest version:** Two claims are welded together here, and they have opposite evidence grades.

SUB-CLAIM 1  -  "the gut microbiome contains redundant metabolic pathways": SUPPORTED, and well supported. Taxonomically divergent communities converge on similar encoded metabolic repertoires; this is one of the most replicated findings in human microbiome genomics.

SUB-CLAIM 2  -  "if a primary strain is depleted, feed specific prebiotic fibres or polyphenols to surviving bacteria so they synthesise the same recovery compounds (e.g. Urolithin A or SCFAs)": UNSUPPORTED for the named exemplars, and directly contradicted by the best available human trials. Redundancy is a property of the *aggregate* metabolic […]

**Key evidence:** FOR REDUNDANCY (mechanism + aggregate):
1. HMP 2012 (Nature, n=242 healthy adults): "Metagenomic carriage of metabolic pathways was stable among individuals despite variation in community structure." Landmark, replicated. PMID 22699609.
2. Tian et al. 2023 (Nat Commun), ultra-deep metaproteomics: high PROTEOME-level functional redundancy and high nestedness in taxa-to-function networks  -  i.e. redundancy exists in expressed proteins, not just gene presence. Critically, gut inflammation and xenobiotic exposure SIGNIFICANTLY DIMINISHED redundancy with NO significant change in taxonomic diversity. PMID 37301875.
3. Microbiome 2025, 4,912 gut metagenomes / 28 disease cohorts: formally identifies "functional redundancy clusters"  -  groups of species that can independently execute a given pathway. This validates the README's graph concept. But: network is polycentric in health, shifts to MONOCENTRIC in NASH, and "FR keystone species exert disproportionate influence on the system's resilience." PMID 41345980.
4. Vieira-Silva 2016 (Nat Microbiol): half of gut species are metabolic […]

**Magnitude:** WHAT FIBRE ACTUALLY DELIVERS (So et al. 2018, AJCN meta-analysis, 64 RCTs, n=2,099 healthy adults)  -  this is the realistic ceiling:
- Bifidobacterium spp.: SMD +0.64 (95% CI 0.42 to 0.86), p<0.00001  -  moderate, robust.
- Lactobacillus spp.: SMD +0.22 (95% CI 0.03 to 0.41), p=0.02  -  small.
- Faecal butyrate: SMD +0.24 (95% CI 0.00 to 0.47), p=0.05  -  borderline, CI touches zero.
- Alpha diversity: NO effect. Other prespecified taxa: NO […]

**Safety caveats:** The additive-only framing does not make this safe; an "add" can pharmacologically subtract drug exposure. Concrete risks if the engine acts on this claim: (a) OATP inhibition by catechin/flavonoid-rich additions  -  green tea at ordinary beverage strength cuts nadolol, fexofenadine and raloxifene exposure by 40-99%; a user on nadolol for hypertension or angina, or on levothyroxine/statins (overlapping transporter substrates), can lose therapeutic effect with no symptom the engine would see. (b) Third-trimester pregnancy: polyphenol-rich additions (cocoa, grape/orange juice, herbal teas) are associated with fetal ductus arteriosus constriction and pulmonary pressure elevation, reversible on restriction; cocoa reproduced indomethacin-like constriction in pregnant rats. Any […]

**What this means for the engine:** This claim is salvageable but only if the graph stops treating "redundant pathway" as a binary and starts treating redundancy breadth as a first-class, queryable property.

1. ADD A REDUNDANCY-BREADTH ATTRIBUTE TO EVERY FUNCTION NODE. Count independent taxa/genomes encoding the pathway from AGORA/VMH (already cited in the README) and KEGG […]

**Sources:**
- [Structure, function and diversity of the healthy human microbiome (Human Microbiome Project […]](https://pubmed.ncbi.nlm.nih.gov/22699609/)
- [Revealing proteome-level functional redundancy in the human gut microbiome using ultra-deep […]](https://doi.org/10.1038/s41467-023-39149-2)
- [Deciphering the personalized functional redundancy hierarchy in the gut microbiome (Microbiome […]](https://doi.org/10.1186/s40168-025-02273-w)
- [Species-function relationships shape ecological properties of the human gut microbiome (Nat […]](https://pubmed.ncbi.nlm.nih.gov/27573110/)
- [Diversity of human colonic butyrate-producing bacteria revealed by analysis of the […]](https://pubmed.ncbi.nlm.nih.gov/19807780/)
- [The effect of jaboticaba peel and seed powder intake for three weeks on urolithin metabotype and […]](https://doi.org/10.1016/j.foodres.2026.118594)

## C8. Urolithin A and short-chain fatty acids are microbially synthesised 'critical recovery compounds'.

**README says:** "critical recovery compounds (like Urolithin A or short-chain fatty acids)"

**Evidence verdict:** partially_supported (confidence high). Grade: MIXED. Microbial-synthesis sub-claim: strong (established microbiology + mechanistic, well-replicated). UA muscle benefit: RCT-in-humans but small, primary-endpoint-negative in the pivotal trial, […]

**Honest version:** Two distinct sub-claims are bundled together. (1) "Microbially synthesised" is TRUE and well-established for both compounds: urolithin A (UA) is a gut-bacterial catabolite of dietary ellagitannins/ellagic acid (pomegranate, walnuts, berries)  -  humans cannot make it, and even the dietary precursors do not yield UA without the right microbes; short-chain fatty acids (SCFAs: acetate, propionate, butyrate) are bacterial fermentation products of dietary fibre/resistant starch. (2) "Critical recovery compounds" is OVERSTATED for human outcomes. For UA, human RCT evidence for muscle function is real but modest, inconsistent, low-certainty, and produced almost entirely by the compound's […]

**Key evidence:** UA microbial origin & metabotypes: Iglesias-Aguirre 2023 J Agric Food Chem (DOI 10.1021/acs.jafc.2c08889) identified the cooperative bacterial consortium (Gordonibacter spp., Ellagibacter isourolithinifaciens) converting ellagic acid to urolithins; García-Villalba 2022 Mol Nutr Food Res (10.1002/mnfr.202101019) describes three metabotypes UM-A (produces UA), UM-B, UM-0 (non-producers)  -  a meaningful minority cannot make UA from precursors, and UM-B/UM-0 shares rise with age/dysbiosis. UA human trials (all Amazentis/Mitopure-sponsored): Andreux 2019 Nat Metab (10.1038/s42255-019-0073-4) first-in-human safety + muscle mitochondrial gene signature, no functional outcome; Singh 2022 Cell Rep Med (10.1016/j.xcrm.2022.100633, NCT03464500) middle-aged adults, 4 mo, ~12% strength gain, improved VO2 peak, reduced plasma acylcarnitines/CRP; Liu 2022 JAMA Netw Open (10.1001/jamanetworkopen.2021.44279) older adults n=66, 1000 mg/d 4 mo  -  both PRIMARY endpoints (6MWT, max ATP) non-significant, only secondary muscle-endurance and biomarker (acylcarnitine/ceramide/CRP) endpoints improved. […]

**Magnitude:** UA: single industry RCT ~12% muscle-strength improvement (Singh 2022); pooled 6-min-walk +17.0 m across 5 RCTs but NOT significant (95% CI crosses 0; p=0.135; low GRADE); pivotal older-adult RCT (n=66) failed both pre-specified primary endpoints; consistent secondary-endpoint effects were on plasma mitochondrial biomarkers (acylcarnitines, ceramides) and CRP. SCFA for exercise recovery: no quantifiable human effect size  -  zero direct […]

**Safety caveats:** THE HEADLINE: the README's central premise  -  that an additive-only, "never say don't eat X" engine carries no liability because it only ever adds food  -  is falsified by a 2026 case series. Eight people formed urolithin A renal calculi, up to 1356 mg, some obstructing the ureter, from daily walnut/blueberry/almond "health smoothies." None took supplements. The exposure that caused the stones is precisely the output this engine is designed to generate: "add walnuts," "add berries," "add pomegranate," repeated daily. Additive framing is not a safety property. It is a rhetorical one.

Worse, the engine's stratification logic points the wrong way. The README proposes scanning the microbiome and, where a user CAN produce UA, feeding ellagitannins to that pathway. The ~40% of people who are […]

**What this means for the engine:** Keep UA and SCFAs in the graph as microbial metabolite nodes, but (a) do NOT label them "critical recovery compounds" as immutable biochemical law  -  that is a marketing-adjacent framing, not established human outcome science; downgrade to "candidate metabolites with modest/limited human evidence." (b) Gate any UA recommendation on the user's […]

**Sources:**
- [Dao 2026  -  Effects of Urolithin A supplementation on muscle health outcomes in humans from RCTs […]](https://doi.org/10.3389/fnut.2026.1834344)
- [Liu 2022  -  Urolithin A Supplementation on Muscle Endurance and Mitochondrial Health in Older […]](https://doi.org/10.1001/jamanetworkopen.2021.44279)
- [Singh 2022  -  Urolithin A improves muscle strength/exercise performance in middle-aged adults […]](https://doi.org/10.1016/j.xcrm.2022.100633)
- [Andreux 2019  -  Urolithin A first-in-human safety & mitochondrial signature (Nature Metabolism; […]](https://doi.org/10.1038/s42255-019-0073-4)
- [Iglesias-Aguirre 2023  -  Gut bacteria (Gordonibacter, Ellagibacter) involved in ellagic acid […]](https://doi.org/10.1021/acs.jafc.2c08889)
- [García-Villalba 2022  -  Urolithins: metabolism, bioactivity, gut microbiota & metabotypes UM-A/B/0 […]](https://doi.org/10.1002/mnfr.202101019)

## C9. Fitness enthusiasts as a cohort have complete micronutrient and bioavailability blindness despite precise macro tracking.

**README says:** "This cohort possesses exceptional macro-discipline (counting protein, fats, and carbs down to the decimal point) but suffers from complete micronutrient and bioavailability blindness."

**Evidence verdict:** overstated (confidence medium). Grade: Observational (cross-sectional dietary surveys and supplement-use questionnaires, n=24 to 1,335) plus one systematic review of bodybuilder dietary intake (18 studies, n=385, rated poor quality and […]

**Honest version:** Competitive physique athletes and a minority of serious gym-goers track energy and macronutrients closely, but almost none quantify micronutrient intake, and the consumer apps they use (MyFitnessPal etc.) are validated only for energy/macros, not micronutrients. Small, mostly old dietary surveys of competitive bodybuilders show >50% under-consume several micronutrients from food (vitamin D, calcium, magnesium, zinc, iron in women), especially during cutting phases and on monotonous diets. However, the cohort is not "blind": 30-60% of gym supplement users buy multivitamins, 11-80% of UK natural bodybuilders take vitamin D, and some megadose to ~1000% RDA / above the UL. The real gap is (a) […]

**Key evidence:** FOR the kernel (micronutrient intake is under-quantified and often inadequate): (1) Ismaeel 2018, n=41 competitive bodybuilders (30M/11F), IIFYM vs strict dieters: "over half of individuals from all groups consumed less than the recommended amounts of several of the micronutrients"; no male IIFYM-vs-strict difference; female IIFYM had higher vitamin E, K, C. Directly tests macro-trackers and finds micronutrient shortfalls regardless of tracking style. (2) Kleiner 1994, n=24 drug-tested USA Championship bodybuilders: females 0% vitamin D RDA, 52% calcium, 76% zinc, below ESADDI for copper/chromium; males 46% vitamin D RDA; 81% of females had contest-related amenorrhea. (3) Helms 2014 review: deficiencies in vitamin D, Ca, Zn, Mg, Fe reported in dieting bodybuilders but "these studies were all published nearly 2 decades ago" and likely reflect food-group elimination and monotony; recommends low-dose multivitamin during prep. (4) Spendlove 2015 systematic review (18 studies, 385 participants, 62 women, mostly 1980s-90s, "poor" quality): supplement contribution often unreported; when […]

**Magnitude:** Food-only micronutrient shortfall in competitive bodybuilders: >50% below recommendations for several micronutrients (Ismaeel 2018, n=41); female elite bodybuilders 0% of vitamin D RDA, 52% calcium, 76% zinc; males 46% vitamin D RDA (Kleiner 1994, n=24). Overshoot when supplements counted: ~1000% RDA, above UL for some micronutrients (Spendlove 2015). Micronutrient supplement uptake: multivitamin 31-60% across gym/bodybuilder samples […]

**Safety caveats:** The additive framing does not make recommendations safe; an absorption enhancer or a stacked micronutrient is pharmacologically a dose increase, and this cohort is already the group most likely to be above ULs from supplements. Specific harm pathways for the README's own example additions: (A) Citrus/vitamin C to increase nonheme iron absorption: harmful for HFE C282Y homozygotes (0.44% of non-Hispanic whites; young Northern-European-ancestry males, over-represented in Western gyms, are exactly the undiagnosed group; 88% of undiagnosed male homozygotes already have ferritin >300 µg/L). Ascorbate plus iron overload amplifies free-radical damage (Halliwell 1982) and high-dose ascorbate has been implicated in iron-loading case reports; at food dose (one lemon squeeze, ~15-30 mg) the per-meal […]

**What this means for the engine:** (1) Reframe the wedge from "micronutrient blindness" to "unquantified micronutrient intake + unsupervised supplementation": the evidence supports a tooling gap (apps are macro-only, micro-invalid) and a supervision gap, not an awareness vacuum. (2) The highest-value first feature is not companion-pairing but micronutrient adequacy accounting: […]

**Sources:**
- [Ismaeel A, Weems S, Willoughby DS. A Comparison of the Nutrient Intakes of Macronutrient-Based […]](https://doi.org/10.1123/ijsnem.2017-0323)
- [Chappell AJ, Simper T, Barker ME. Nutritional strategies of high level natural bodybuilders during […]](https://doi.org/10.1186/s12970-018-0209-z)
- [Chappell AJ, Simper T, Helms E. Nutritional strategies of British professional and amateur natural […]](https://doi.org/10.1186/s12970-019-0302-y)
- [Kleiner SM et al. Nutritional status of nationally ranked elite bodybuilders. Int J Sport Nutr 1994 […]](https://pubmed.ncbi.nlm.nih.gov/8167655/)
- [Spendlove J et al. Dietary Intake of Competitive Bodybuilders. Sports Med 2015 (PMID 25926019)](https://doi.org/10.1007/s40279-015-0329-4)
- [Lenzi JL et al. Dietary Strategies of Modern Bodybuilders During Different Phases of the […]](https://doi.org/10.1519/JSC.0000000000003169)

## C10. Gym-goers routinely mega-dose competing supplements (implying supplement-supplement absorption competition is common and consequential).

**README says:** "They routinely mega-dose competing supplements"

**Evidence verdict:** overstated (confidence high). Grade: Population half: observational, cross-sectional convenience-sample self-report surveys (n=63 to 2,576 per study; methodological quality rated 43 +/- 16% of available points across 159 studies in the […]

**Honest version:** Gym-goers are heavy, largely self-prescribed, multi-product supplement users (30-85% use in gym surveys; pooled ~60% of athletes; typical stack = protein + creatine/amino acids + multivitamin/mineral + pre-workout; median 3 products in elite athletes, mean 1.59 in Lisbon gym-goers; 55-61% self-prescribed via internet/peers). A minority mega-dose specific nutrients: among supplement-using athletes, 16-34% exceed the UL for niacin, ~10% of women for vitamin B6, 8-17% of women for preformed vitamin A; ~8% of US adults exceed the zinc UL (rising from 5% to 8% because of supplements); 38% of young Danish gym users exceed 400 mg/day caffeine. All other micronutrient UL exceedances are <=4%. […]

**Key evidence:** PREVALENCE/STACKING (for): Knapik 2016 SR/MA of 159 studies: any-supplement pooled prevalence 60% (95% CI 55-64) in athletes; non-elite men 48% (27-70), women 42% (22-66) vs elite 69%/71%; MVM in non-elite 33-39%; vitamin C 32%; protein 27%; iron 17%; calcium 12%; zinc-only 7% (5-10). Gym surveys: Long Island NY 2004: 84.7% used, MVM 45%, protein 42.3%, vitamin C 34.7%, vitamin E 23.4% taken >=5x/week, ephedra 28% weekly; Belo Horizonte 2010 (n=1,102): 36.8%, 55% self-prescribed; Beirut 2012 (n=512): 36.3%; Palermo 2011 (n=800): 30.1%, whey mixed with creatine+amino acids 48.3% of users, 34% relied on gym instructors, 0% consulted nutritionists; Sao Luis 2015 (n=723): 64.7%; Riyadh 2017 (n=299): 37.8%; Sharjah 2018 (n=320): 43.8%, 60.7% internet-driven self-prescription, 12.8% consulted dietitians; Riyadh 2018 (n=445): 44.5%; Mainz 2018 (n=492): 57% last-4-weeks, pre-workout boosters 25.8% lifetime; Portugal 2020 (n=459): 43.8%, MVM 38.3% of users; Naples bodybuilders 2021 (n=107): 81.3% supplements, 35.5% hormones; CrossFit 2022 (n=2,576): 82.2% >=1 supplement; Lisbon 2024 (n=303): […]

**Magnitude:** Use prevalence: 30-85% across gym surveys (n=63-2,576); pooled athletes 60% (55-64); non-elite 42-48%; MVM 33-39%; zinc-only supplements 7%; protein 27% (men 36%). Stacking: median 3 products (elite athletes), mean 1.59 (gym-goers), 18.4 ingredients per pre-workout. Mega-dosing: UL exceedance among supplement-using athletes: niacin 16-34%, B6 9-11% (women), vitamin A 8-17% (women), all others <=4%; US adults >UL: zinc 8%, niacin 10%, vitamin A […]

**Safety caveats:** Assume the engine tells a real gym-goer to ADD something on top of an existing, largely undisclosed stack. (1) Additive-only framing is not risk-free: the documented harm mode in this cohort is summation across products, so any "add" that carries caffeine, niacin, B6, zinc, magnesium, vitamin A or iron can push a user over a UL the engine cannot see unless it ingests the supplement inventory. Concrete thresholds: caffeine 200 mg single/400 mg day (EFSA); niacin 35 mg (flushing; niacin-containing energy products linked to acute hepatitis and liver failure); B6 12 mg (EFSA 2023; neuropathy reference point 50 mg/day; US UL 100 mg); zinc 40 mg (copper deficiency at ≥50 mg for weeks; ZMA alone is 30 mg); supplemental magnesium 350 mg (diarrhea; hypermagnesemia in impaired kidney function); […]

**What this means for the engine:** 1) Reframe the wedge: the defensible, computable problem in gym-goers is nutrient AGGREGATION across stacked products (whey + creatine + MVM + ZMA + pre-workout + fortified bars/gainers), not absorption competition. Build a per-nutrient daily-sum from Grocy inventory/label data, compare to UL (EFSA/IOM/Nordic tables), and flag the nutrients that […]

**Sources:**
- [Knapik et al. 2016 - Prevalence of Dietary Supplement Use by Athletes: Systematic Review and […]](https://doi.org/10.1007/s40279-015-0387-7)
- [Morrison, Gizis & Shorter 2004 - Prevalent use of dietary supplements among people who exercise at […]](https://doi.org/10.1123/ijsnem.14.4.481)
- [Goston & Correia 2010 - Intake of nutritional supplements among people exercising in gyms and […]](https://doi.org/10.1016/j.nut.2009.06.021)
- [El Khoury & Antoine-Jonville 2012 - Intake of Nutritional Supplements among People Exercising in […]](https://doi.org/10.1155/2012/703490)
- [Bianco et al. 2011 - Protein supplementation in strength and conditioning adepts, Palermo (JISSN)](https://doi.org/10.1186/1550-2783-8-25)
- [Ruano & Teixeira 2020 - Prevalence of dietary supplement use by gym members in Portugal (JISSN)](https://doi.org/10.1186/s12970-020-00342-z)

## C11. Combining clashing food matrices causes 'anabolic waste' (i.e. lost muscle-building potential from nutrient interactions).

**README says:** "combine clashing food matrices that cause "anabolic waste,""

**Evidence verdict:** unsupported (confidence high). Grade: Claim as stated: marketing claim / mechanistic speculation (no primary source; zero hits for "anabolic waste" in biomedical titles). Counter-evidence: multiple independent human RCTs using […]

**Honest version:** There is no recognised physiological phenomenon called "anabolic waste" and no human evidence that combining ordinary foods ("clashing matrices") reduces the muscle-building response to a meal. Stable-isotope studies in humans show that co-ingesting carbohydrate or fat with protein, or eating protein inside a whole-food matrix (whole egg, whole milk, cheese, salmon, mycoprotein, beef), produces muscle protein synthesis (MPS) rates that are equal to, or in some cases higher than, isolated protein; the classic "food combining" (dissociated) diet gave no advantage in a 6-week inpatient RCT; and very large protein doses (100 g) are not oxidised away but extend the anabolic response for over 12 […]

**Key evidence:** TERM CHECK: Europe PMC title search for "anabolic waste" = 0 hits; full-text search = 2 hits, both unrelated (bone-marrow organoid review; chemoresistant cancer cell lines). No fitness-nutrition source in the peer-reviewed literature uses the term.

DIRECT TESTS OF "FOOD COMBINING": Golay 2000 (Int J Obes; n=54 obese inpatients, 6 wk, isocaloric 1100 kcal/d, dissociated vs balanced): weight loss 6.2+/-0.6 vs 7.5+/-0.4 kg (NS); "total lean body mass was identically spared in both groups"; fasting glucose, insulin, lipids fell equally. No funding listed.

CARBOHYDRATE + PROTEIN (the most common "clash" in gym folklore): Koopman 2007 (AJP Endo; n=10, crossover, 0/0.15/0.6 g/kg/h CHO with 0.3 g/kg/h protein hydrolysate, 6 h post-exercise): mixed-muscle FSR 0.10/0.10/0.11 %/h, no difference; insulin 12x higher with CHO made no difference. Staples 2011 (MSSE; n=9, 25 g whey +/- 50 g maltodextrin): no difference in MPS or breakdown despite 17.5-fold glucose and 5-fold insulin AUC. Gorissen 2014 (JCEM; n=24 young + 25 older, 20 g intrinsically labelled protein +/- 60 g CHO): CHO delayed […]

**Magnitude:** Effect of co-ingesting carbohydrate with protein on MPS: 0 (three RCTs, n=9-49; FSR differences within 0.001-0.008 %/h, all NS). Effect of fat/whole-food matrix vs isolate on MPS: 0 to positive (whole egg > egg white, P=0.04, n=10; whole milk threonine uptake 2.8x fat-free; salmon, cheese, mycoprotein, minced/steak beef all NS vs comparator, n=9-24). Food-combining diet vs balanced diet at matched calories: weight loss 6.2 vs 7.5 kg (NS), lean […]

**Safety caveats:** The additive framing does not make recommendations safe: several of the engine's canonical "adds" are pharmacologically active at culinary doses, and "add more protein/leucine/minerals to avoid waste" has hard contraindications. (1) CKD (~10% of adults, largely undiagnosed): KDOQI 2020 (PMID 32829751) recommends 0.55-0.60 g/kg/d protein for metabolically stable CKD 3-5 (0.6-0.8 g/kg/d in diabetic CKD; NEJM review PMID 29091561); an engine pushing toward 1.6-2 g/kg/d or 100 g boluses directly conflicts. Same population is at risk from "add" potassium-rich foods when on ACE inhibitors/ARBs/MRAs (KDIGO 2020, PMID 31706619) and from magnesium supplements/antacids (hypermagnesemia: PMID 39392591; LPI: UL 350 mg/d supplemental Mg; renal impairment increases risk). Healthy adults: high protein […]

**What this means for the engine:** Remove "anabolic waste" and any "matrix clash -> lost anabolism" edge type, score term or Anabolic Synergy Index penalty; there is no human evidence to parameterise it and its sign is wrong (whole-food combinations are neutral-to-positive). Replace with evidence-backed per-meal features: (a) protein dose relative to body mass (~0.3-0.4 g/kg or […]

**Sources:**
- [Golay et al. 2000 - Similar weight loss with low-energy food combining or balanced diets (Int J […]](https://doi.org/10.1038/sj.ijo.0801185)
- [Koopman et al. 2007 - Coingestion of carbohydrate with protein does not further augment […]](https://doi.org/10.1152/ajpendo.00135.2007)
- [Staples et al. 2011 - Carbohydrate does not augment exercise-induced protein accretion versus […]](https://doi.org/10.1249/mss.0b013e31820751cb)
- [Gorissen et al. 2014 - Carbohydrate coingestion delays dietary protein digestion and absorption but […]](https://doi.org/10.1210/jc.2013-3970)
- [van Vliet et al. 2017 - Whole eggs promote greater postexercise muscle protein synthesis than […]](https://doi.org/10.3945/ajcn.117.159855)
- [ClinicalTrials.gov NCT03117127 - sponsor record for whole egg vs egg white trial (University of […]](https://clinicaltrials.gov/study/NCT03117127)

## C12. Heavy protein and sweetener intake causes broad-spectrum gut dysbiosis in this cohort.

**README says:** "or experience broad-spectrum gut dysbiosis due to heavy protein/sweetener loads."

**Evidence verdict:** overstated (confidence high). Grade: Mixed and weaker than the claim implies. Best available: small short human RCTs (n=17-120, 2-10 weeks) plus observational athlete cohorts; one RCT (Suez 2022) adds gnotobiotic-mouse transplant for […]

**Honest version:** Resistance-trained, high-protein, high-sweetener eaters show measurable gut microbial DIFFERENCES from sedentary controls, but not "broad-spectrum dysbiosis," and causation is not established for either exposure.

PROTEIN: (a) Protein dose itself does not change microbiota composition. Beaumont 2017 (RCT, n=38, 3 wk isocaloric casein vs soy vs maltodextrin) found "HPDs did not alter the microbiota composition"  -  what changed was bacterial METABOLISM, shifted toward amino-acid degradation, with profiles differing by protein source. Fecal-water cytotoxicity unchanged; no inflammation induced. (b) In the gym cohort specifically, Jang 2019 found bodybuilders vs runners vs sedentary "did not […]

**Key evidence:** SUPPORTING (partial):
- Moreno-Pérez 2018, Nutrients, PMID 29534465  -  randomized double-blind PILOT, n=24 cross-country runners (12 protein [whey isolate + beef hydrolysate] vs 12 maltodextrin), 10 wk. Bacteroidetes up; Roseburia, Blautia, Bifidobacterium longum down. All functional markers null (fecal pH, water, ammonia, SCFA; plasma/urine malondialdehyde). Authors hedge: protein "may have a negative impact… Further research is needed." No COI declared.
- Jang 2019, J Int Soc Sports Nutr, PMID 31053143  -  OBSERVATIONAL: bodybuilders vs distance runners vs sedentary men. Alpha and beta diversity did NOT differ by athlete type. Bifidobacterium/Parasutterella lowest and Faecalibacterium/Sutterella/Clostridium/Haemophilus/Eisenbergiella highest in bodybuilders; SCFA producers (Blautia wexlerae, Eubacterium hallii) and probiotic taxa lowest in bodybuilders. Protein intake vs OTU count r = -0.53, p<0.05. Confounded: bodybuilders were high-protein AND low-fiber.
- Russell 2011, AJCN, PMID 21389180  -  controlled crossover feeding, 17 obese men, 4 wk/arm. Both high-protein arms raised […]

**Magnitude:** Effect sizes are small, mostly reported as taxon-level significance without magnitudes, and the primary functional endpoints are frequently ZERO.

- Jang 2019: the only correlation coefficient in the on-cohort literature  -  daily protein intake vs OTU count r = -0.53, p<0.05. In a small observational sample with fiber co-varying, this is weak. Alpha/beta diversity difference between bodybuilders, runners and sedentary controls: NOT significant […]

**Safety caveats:** The additive-only framing does not make recommendations safe, and this claim is where that breaks most clearly. Specific exposures:
1. CKD stage 3-5 / dialysis  -  highest-stakes population. The protein-fermentation axis is genuinely clinical here: p-cresyl sulfate and indoxyl sulfate are gut-derived, protein-precursor (tyrosine/phenylalanine, tryptophan) uraemic toxins whose accumulation is linked to renal progression and cardiovascular outcomes across 59 studies. The danger is not the protein advice, it is what an additive engine reaches for as the remedy: the README's own additive library (nuts, seeds, cocoa, leafy greens, bananas, dairy) is potassium- and phosphorus-dense. Hyperkalaemia is an acute arrhythmic risk. A lifter with undiagnosed CKD is a realistic user  -  creatine […]

**What this means for the engine:** 1. DELETE "dysbiosis" as a modeled entity. It has no consensus functional definition and therefore no measurable threshold; a node or scalar named "dysbiosis" is unfalsifiable and will silently accumulate error through the recalibration loop. Replace with quantities that can actually be read: fiber intake (g/d), fermentable-substrate-to-protein […]

**Sources:**
- [Effect of a Protein Supplement on the Gut Microbiota of Endurance Athletes: A Randomized, […]](https://pubmed.ncbi.nlm.nih.gov/29534465/)
- [The combination of sport and sport-specific diet is associated with characteristics of gut […]](https://pubmed.ncbi.nlm.nih.gov/31053143/)
- [High-protein, reduced-carbohydrate weight-loss diets promote metabolite profiles likely to be […]](https://pubmed.ncbi.nlm.nih.gov/21389180/)
- [Quantity and source of dietary protein influence metabolite production by gut microbiota and rectal […]](https://pubmed.ncbi.nlm.nih.gov/28903954/)
- [Exercise and associated dietary extremes impact on gut microbial diversity (Clarke 2014, Gut; PMID […]](https://pubmed.ncbi.nlm.nih.gov/25021423/)
- [The microbiome of professional athletes differs from that of more sedentary subjects in composition […]](https://pubmed.ncbi.nlm.nih.gov/28360096/)

## C13. A single night of poor sleep can completely alter metabolic and gut-microbial state.

**README says:** "a single night of poor sleep can completely alter metabolic and gut microbial realities."

**Evidence verdict:** overstated (confidence high). Grade: Metabolic half: small randomized crossover trials in humans (n=9-28 per study, gold-standard clamp/IVGTT/OGTT endpoints), replicated across >=6 independent labs, plus two meta-analyses of RCTs (Zhu […]

**Honest version:** A single night of short sleep (about 4 h, or one night of total wakefulness) produces a measurable but modest and transient metabolic shift in healthy adults: whole-body insulin sensitivity falls roughly 15-25% (clamp glucose-infusion rate -25%, HOMA-IR +16%), next-day post-glucose-load glucose rises roughly 10-20%, a minority of circulating metabolites change (e.g., 27 of 171 measured; specific acylcarnitines +22-32%), and adipose/muscle tissue shows altered clock-gene methylation and expression. These effects are consistent in direction across independent labs and reverse within 1-2 nights of normal sleep. The claim's second half has no human support: there is no single-night human […]

**Key evidence:** SINGLE-NIGHT HUMAN METABOLIC STUDIES (all randomized crossover, in-lab unless noted): Donga 2010 (n=9, 4 h sleep one night, hyperinsulinemic clamp): glucose infusion rate -25% (P=0.001); glucose disposal 32.5 vs 40.7 umol/kg LBM/min (-20%, P=0.009); endogenous glucose production during clamp 4.4 vs 3.6 (+22%, P=0.017, hepatic IR); clamp NEFA 68 vs 57 umol/L; fasting glucose/insulin/NEFA UNCHANGED. Cedernaes 2016 JSR (n=16 men, 4.25 h one night): HOMA-IR +16% (P=0.025). Cedernaes 2015 JCEM (n=15 men, one night total sleep deprivation): 2-h post-OGTT glucose 7.77 vs 6.59 mmol/L (+18%); adipose CRY1 promoter methylation +4%, PER1 enhancers +15%/+9%; muscle BMAL1 mRNA -18%, CRY1 -22%; cortisol lower. Cedernaes 2018 Sci Adv (same design, n=15 pairs): 148 differentially methylated regions in adipose (FDR<0.05), tissue-specific transcript/protein changes, inflammatory transcript signatures in both tissues; funders stated to have no role. van den Berg 2016 (n=9 healthy + 7 T1D, 4 h vs 8 h): plasma acylcarnitines C14:1 +32%, C18:1 +22%, C18:2 +27%. Davies 2014 PNAS (n=12, 24 h wakefulness, […]

**Magnitude:** Single night, healthy adults: insulin sensitivity -15% to -25% (clamp GIR -25%, n=9; HOMA-IR +16%, n=16); 2-h post-load glucose +18% after total sleep deprivation (n=15); OGTT glucose AUC +9.5% after 3 h sleep (n=11, insulin AUC unchanged); specific acylcarnitines +22-32%; 27/171 metabolites (16%) increased and 78/109 rhythms preserved during 24 h wake (n=12); 25/263 lipids (10%) trended (n=20); 148 adipose DMRs; clock-gene methylation +4-15%, […]

**Safety caveats:** This claim is not inert, because the README wires it directly to an intervention. Section 5 states that for "High Fasting Insulin" the engine recommends Ceylon Cinnamon + Magnesium + Acetic Acid. A single night of poor sleep lowers insulin sensitivity and raises fasting insulin. So by the engine's own logic, C13 is the trigger that fires that supplement stack  -  on a transient, self-resolving physiological state. That is the concrete harm pathway, and it is specific to this claim rather than generic.

WHO GETS HURT
1. Insulin, sulfonylurea and meglitinide users. Acetic acid is pharmacologically active on glucose (-9.40 mg/dL fasting, -14.59 mg/dL postprandial, meta-analytic). Stacked on a fixed prandial insulin dose or a sulfonylurea during a night of disturbed sleep, this is a […]

**What this means for the engine:** Model 'poor sleep' as a modest, day-scale, self-resolving metabolic modifier, not a state reset: after a reported short night, apply a prior of roughly -20% insulin sensitivity and +10-20% post-meal glucose excursion for that day, decaying to baseline after 1-2 normal nights (Broussard 2016; Chennaoui 2014). Actionable, replicated levers under […]

**Sources:**
- [Donga 2010 - A single night of partial sleep deprivation induces insulin resistance in multiple […]](https://pubmed.ncbi.nlm.nih.gov/20371664/)
- [Cedernaes 2016 - A single night of partial sleep loss impairs fasting insulin sensitivity (J Sleep […]](https://pubmed.ncbi.nlm.nih.gov/26361380/)
- [Cedernaes 2015 - Acute sleep loss induces tissue-specific epigenetic and transcriptional […]](https://pubmed.ncbi.nlm.nih.gov/26168277/)
- [Cedernaes 2018 - Acute sleep loss results in tissue-specific alterations in genome-wide DNA […]](https://pmc.ncbi.nlm.nih.gov/articles/PMC6105229/)
- [van den Berg 2016 - A single night of sleep curtailment increases plasma acylcarnitines (Arch […]](https://pubmed.ncbi.nlm.nih.gov/26393786/)
- [Davies 2014 - Effect of sleep deprivation on the human metabolome (PNAS)](https://pubmed.ncbi.nlm.nih.gov/25002497/)

## C14. Human biology is chaotic, non-linear and non-replicable, unpredictable moment to moment.

**README says:** "Human biology is a chaotic, non-linear, and non-replicable system - unpredictable moment to moment"

**Evidence verdict:** overstated (confidence high). Grade: Against the claim: (1) Human observational biological-variation studies with rigorous repeated sampling (EuBIVAS: n=91, 10 weekly samples, BIVAC grade A; Macy 1997 CRP; Ricos/Westgard compilation) - […]

**Honest version:** Human physiology is a nonlinear, multi-scale, homeostatically regulated system, not a chaotic or non-replicable one. Core regulated variables are highly reproducible within a person (within-subject biological CV: sodium 0.6%, HbA1c 1.2%, fasting glucose ~5%, cholesterol ~6%), while some markers the README relies on are noisy day to day (hs-CRP CVI 42%, fasting insulin ~21%, HOMA-IR 27%, CK 15-23%, postprandial glucose to duplicate meals ICC 0.17-0.74). Physiological time series such as heart rate show fractal, long-range-correlated ("1/f") dynamics, but the best-studied case (heart rate variability) shows no good evidence of deterministic chaos; most of the "chaotic-looking" fluctuation is […]

**Key evidence:** CHAOS/NONLINEARITY: Goldberger et al. 2002 PNAS: healthy heartbeat shows long-range power-law (fractal, multifractal) correlations, breaking down in heart failure/aging - this is nonlinear and complex, but structured and statistically predictable. Kanters et al. 1994 (n=10 healthy adults, surrogate-data testing): "no evidence for low-dimensional chaos in the time series of RR intervals"; correlation dimension of real and surrogate data differed only slightly; nonlinear determinism present but prediction error grows slower than a chaotic system would. Wessel et al. 2009 (Chaos): respiratory modulation explains heart-rate fluctuation with coefficient of determination 96%; recommends replacing "is the heart rate chaotic?" with "is it 'chaotic' due to respiration?". Glass 2009 (Chaos, editorial introducing the controversy issue) confirms no consensus that normal heart rate is chaotic. No study located demonstrates deterministic chaos (positive Lyapunov exponent with surrogate control) in any human physiological output. WITHIN-PERSON REPLICABILITY OF BLOOD MARKERS: Ricos/Westgard 2014 BV […]

**Magnitude:** Replicability by measurand (within-subject CV, i.e., week-to-week noise in the same healthy person): sodium 0.6%; HbA1c 1.2%; QUICKI 4.1%; fasting glucose 5.0-5.6%; cholesterol ~6%; testosterone ~9%; CK 14.5% (EuBIVAS) to 22.8% (older data); cortisol 15%; triglyceride ~20%; fasting insulin ~21%; HOMA-IR 26.7%; iron 26.5%; CRP 42.2%. Corresponding two-sided p<0.05 reference change values (RCV = 2.77 x sqrt(CVA^2 + CVI^2), assuming CVA 3-5%): […]

**Safety caveats:** This claim is not a food additive, but it is the epistemic premise of the whole engine and the README pairs it with 'liability. there is none.' That pairing is where the harm lies. (1) If the engine encodes 'biology is unpredictable/non-replicable', it has no principled basis for deterministic hard-stop rules - yet the hazards are the most deterministic part of biology. Every README exemplar has a replicable contraindication: 'squeeze lemon on greens' (ascorbate + non-heme iron) is beneficial in deficiency and contraindicated at supplement doses in iron-loaded hemochromatosis patients (AASLD 2011: avoid vitamin C supplements; food doses acceptable - the engine must distinguish food from supplement dose). 'Add black pepper' (piperine) inhibits CYP3A4/P-gp and glucuronidation; users on […]

**What this means for the engine:** 1) The claim is self-undermining: if biology were truly non-replicable and unpredictable moment to moment, the README's own blood-panel validation loop and "Dynamic Biological Twin" could not learn anything. The real situation is more useful and more demanding: biology is reproducible enough to learn from, but each measurand has a known noise […]

**Sources:**
- [Glass L. Introduction to controversial topics in nonlinear science: is the normal heart rate […]](https://doi.org/10.1063/1.3156832)
- [Wessel N et al. Is the normal heart rate 'chaotic' due to respiration? Chaos 2009](https://doi.org/10.1063/1.3133128)
- [Kanters JK et al. Lack of evidence for low-dimensional chaos in heart rate variability. J […]](https://doi.org/10.1111/j.1540-8167.1994.tb01300.x)
- [Goldberger AL et al. Fractal dynamics in physiology: alterations with disease and aging. PNAS 2002](https://pmc.ncbi.nlm.nih.gov/articles/PMC128562/)
- [Lipsitz LA, Goldberger AL. Loss of 'complexity' and aging. JAMA 1992](https://doi.org/10.1001/jama.1992.03480130122036)
- [Westgard QC: Desirable Biological Variation Database specifications (Ricos et al. 2014 update)](https://www.westgard.com/biodatabase1.htm)

## C15. Blood biomarkers can prove whether a dietary recommendation influenced the body.

**README says:** "Blood biomarkers serve as the ultimate validation layer to prove whether a dietary recommendation successfully influenced the body."

**Evidence verdict:** overstated (confidence high). Grade: Mixed by sub-claim. "Diet moves blood biomarkers at group level": meta-analyses of RCTs (high). "Biomarker/phenotype-guided personalised advice outperforms generic advice on blood markers": RCTs and […]

**Honest version:** Blood biomarkers can objectively confirm two narrower things: (1) that a person actually consumed/absorbed a nutrient, when a validated intake or status marker exists for it (plasma ascorbate, serum ferritin/sTfR, 25(OH)D, RBC folate, erythrocyte omega-3 index, alkylresorcinols, urinary Na/K/N), and (2) at the group level across RCTs, that dietary patterns shift risk markers by modest amounts (e.g., Mediterranean diet lowers hs-CRP by roughly 1 mg/L). They cannot, from one baseline and one follow-up panel, "prove" that a specific additive food-pairing recommendation caused a change in one individual, because the within-person biological noise of the markers the README names (hs-CRP […]

**Key evidence:** AGAINST (as stated). (a) Noise vs signal for the README's named markers: EuBIVAS serial sampling in 91 healthy adults over 10 weeks (Carobene 2019, Clin Chem) gives CRP within-subject CV 42% and between-subject CV 76% (values as quoted by a 2025 BMC Prim Care paper citing EuBIVAS); the EuBIVAS authors state analytical goals for CRP should not even be derived from biological-variation data except for CVD risk use, because participants kept having mild inflammatory episodes (7% of 25,290 results excluded). Ockene 2001 (n=113, 5 hs-CRP draws over 1 year): only 63% of consecutive pairs fell in the same quartile. Rudez 2009 (40 healthy adults, 520 samples): CRP had by far the largest within-subject variation of the inflammatory/haemostatic panel. HOMA-IR within-subject CV 26.7% (95% CI 25.5-28.3) in 90 non-diabetic EuBIVAS subjects, "driven largely by variability in plasma insulin"; authors conclude single measurements are of limited value (Carobene 2025). CK: reference change value about +140%/-60% from biweekly sampling in 17 healthy subjects (Wu 2009); post-exercise CK peaks 2-6 days […]

**Magnitude:** Within-person noise: hs-CRP CVI ~42%, CVG 76% (n=91, 10 weekly draws) implying a reference change value >100% for a single pair of results; HOMA-IR CVI 26.7% (n=90); CK RCV +140%/-60% (n=17) and post-exercise rises up to 33x baseline peaking 2-6 days after training. Diet effects at group level: Mediterranean pattern hs-CRP -0.98 mg/L (I2 91%); +8 g/d fibre CRP -0.37 mg/L; exercise training CRP ES 0.26. Biomarker-guided personalised nutrition vs […]

**Safety caveats:** The additive framing does not make the loop safe, for two reasons: (a) the "add" recommendations are themselves contraindicated in identifiable groups, and (b) a validation loop that cannot see a signal at food doses will pressure escalation to supplement doses, where the harms live. Specific populations and interactions:
- Hereditary hemochromatosis (C282Y homozygosity ~1 in 225 people of Northern European ancestry; 1 in 15 carry one copy; men and post-menopausal women express iron overload; NIDDK): NIDDK advises avoiding vitamin C supplements and iron supplements because vitamin C increases iron absorption. The engine's flagship "citrus on greens to reduce ferric to ferrous iron" is precisely the mechanism these patients are told to avoid; food-dose lemon is low risk, but the engine has […]

**What this means for the engine:** 1. Rename the layer: it is a monitoring/feedback layer with explicit uncertainty, not a "validation layer that proves". 2. Require a personal baseline of at least 2-3 draws (weekly, same time, fasted, >=72 h after hard training, no acute illness) before any recommendation is scored; store per-analyte within-subject CV and compute lognormal […]

**Sources:**
- [Bermingham KM et al. 2024. Effects of a personalized nutrition program on cardiometabolic health: a […]](https://pubmed.ncbi.nlm.nih.gov/38714898/)
- [Berry SE et al. 2020. Human postprandial responses to food and potential for precision nutrition […]](https://pubmed.ncbi.nlm.nih.gov/32528151/)
- [Celis-Morales C et al. 2017. Effect of personalized nutrition on health-related behaviour change: […]](https://pubmed.ncbi.nlm.nih.gov/27524815/)
- [Celis-Morales C et al. 2017. Can genetic-based advice help you lose weight? Food4Me. Am J Clin Nutr](https://pubmed.ncbi.nlm.nih.gov/28381478/)
- [Duc TQ et al. 2026. Effects of personalized nutrition on cardiometabolic biomarkers in adults with […]](https://pubmed.ncbi.nlm.nih.gov/42106813/)
- [Cross V et al. 2025. Do personalized nutrition interventions improve dietary intake and risk […]](https://pubmed.ncbi.nlm.nih.gov/39420556/)

## C16. Eating a recommended meal alters internal small-molecule metabolomics in a way measurable by blood panels (hs-CRP, fasting insulin, creatine kinase).

**README says:** "User Eats Meal Matrix ... -->|Alters internal small-molecule metabolomics| Blood_Panels ... (hs-CRP, Fasting Insulin, Creatine Kinase)"

**Evidence verdict:** overstated (confidence high). Grade: Mixed by sub-claim. (1) Meal alters plasma metabolome: human controlled crossover/challenge trials (n=15-36) plus a large postprandial cohort (n=1,002) - strong, replicated. (2) Food-intake […]

**Honest version:** A meal does measurably change the plasma small-molecule metabolome within 0.5-6 h (well replicated in controlled human crossover/challenge studies), and a few food-specific metabolites (e.g., proline betaine for citrus) can confirm that a food was eaten. But hs-CRP, fasting insulin and creatine kinase are not metabolomic readouts (they are a protein, a peptide hormone and an enzyme on a routine chemistry panel), and none of them responds to a single meal in a way that can be attributed to that meal: CRP does not change after a single meal in ~79% of controlled studies (half-life ~19 h, peaks ~48 h after a stimulus); fasting insulin has ~26% day-to-day within-person variation plus ~24% […]

**Key evidence:** FOR the metabolome half: Pellis 2012 (Metabolomics): standardized 500 mL shake, 6-h time course, 106 of 145 plasma metabolites, 31 of 79 proteins and 5 of 7 clinical-chemistry parameters changed; a 5-week anti-inflammatory supplement mix in 36 overweight subjects altered 31 of 231 postprandial parameters that were NOT detectable in the fasting state. Karimpour 2016 (Anal Chim Acta): GC-MS/LC-MS/NMR after a challenge meal showed amino acids and sugars up, fatty acids and ketones down at 0.5 h; the individual response was stable when retested 1.5 years later and largely independent of background diet. Krug 2012 (FASEB J): 15 healthy men, 4-day challenge protocol, 275 metabolic traits at up to 56 time points; challenges exposed inter-individual metabotypes invisible at fasting baseline. Berry 2020 PREDICT 1 (Nat Med; n=1,002 UK + 100 US validation; authors include Zoe Global Ltd employees alongside Wellcome/MRC/BHF/NIH funding): population CV of postprandial responses to identical meals was 103% (triglyceride), 68% (glucose), 59% (insulin); meal macronutrients explained only 3.6% of […]

**Magnitude:** Acute metabolome: ~73% of quantified plasma metabolites (106/145) change within 6 h of a standardized meal; changes at 0.5 h are reproducible within-person 1.5 years apart. Inter-individual postprandial CV to identical meals: TG 103%, glucose 68%, insulin 59% (n=1,002); meal composition explains 3.6-15.4% of variance. hs-CRP: single meal - no change in 79% of 29 studies; the largest reported single-meal effect is -6% (n=8), versus within-person […]

**Safety caveats:** Who is harmed by the "add" recommendations the README ties to these biomarkers: (1) HFE hemochromatosis (about 1 in 227 non-Hispanic whites, mostly undiagnosed, 88% of undiagnosed male homozygotes already have ferritin >300): the flagship "vitamin C + iron" pairing is the wrong direction; high-dose vitamin C worsens iron overload; add-only stacking ("add citrus to every iron meal") converts a food-dose nudge into a chronic absorption-enhancing regimen; same for thalassemia/transfusional iron overload. (2) Wilson disease and high-dose zinc users: the "elevated CK/hs-CRP -> add copper" rule is contraindicated in Wilson disease, which is harmed at normal dietary copper; copper has no human RCT support for collagen/recovery anyway. (3) Kidney stone formers and CKD: vitamin C supplements >=1 […]

**What this means for the engine:** Split the "Objective Validation Loop" into two loops with different physics. FAST LOOP (hours): the only meal-scale signals with human evidence are postprandial glucose (CGM), postprandial TG/insulin (venous, impractical) or targeted food-intake biomarkers (urinary proline betaine for citrus, etc.); PREDICT 1 shows even standardized meals with […]

**Sources:**
- [Berry SE et al. 2020. Human postprandial responses to food and potential for precision nutrition […]](https://pubmed.ncbi.nlm.nih.gov/32528151/)
- [Pellis L et al. 2012. Plasma metabolomics and proteomics profiling after a postprandial challenge […]](https://doi.org/10.1007/s11306-011-0320-5)
- [Karimpour M et al. 2016. Postprandial metabolomics: pilot MS and NMR study of the plasma metabolome […]](https://doi.org/10.1016/j.aca.2015.12.009)
- [Krug S et al. 2012. The dynamic range of the human metabolome revealed by challenges. FASEB J](https://doi.org/10.1096/fj.11-198093)
- [Garcia-Perez I et al. 2017. Objective assessment of dietary patterns by use of metabolic […]](https://doi.org/10.1016/S2213-8587(16)30419-3)
- [Heinzmann SS et al. 2010. Proline betaine as a marker of citrus consumption. Am J Clin Nutr](https://doi.org/10.3945/ajcn.2010.29672)

## C17. Sequential blood tests can be used by ML to learn exactly how a specific individual reacts to micro-additive nutritional changes.

**README says:** "sequential blood tests form a Dynamic Biological Twin inside ArcadeDB, allowing the machine learning layers to learn exactly how a specific human body dynamically reacts to micro-additive nutritional changes."

**Evidence verdict:** overstated (confidence high). Grade: Mixed. (1) Group-level ML-personalized nutrition: human RCTs, n=200-350, 6-18 weeks/months, mostly company-affiliated (ZOE, DayTwo, Twin Health) - moderate quality, small effects. (2) […]

**Honest version:** Serial blood panels can track an individual's biomarker trajectory, and ML models trained on large cohorts can modestly predict some acute nutritional responses from a person's baseline blood/microbiome/anthropometric features (postprandial glucose r~0.62-0.77, postprandial triglyceride r~0.47). Trials that act on such predictions produce small group-level gains over generic advice (e.g., TG -0.13 mmol/L; HbA1c between-group difference -0.08%), and adding blood phenotype to dietary advice added nothing in the one large RCT that tested it (Food4Me). No published human study has shown an ML system learning an individual's response to small dietary additions from sequential blood draws. The […]

**Key evidence:** FOR (what is real): (a) Large inter-individual variability in postprandial responses to identical meals: PREDICT 1 (Berry 2020, Nat Med, n=1,002 UK + 100 US validation; population CV 103% for TG, 68% glucose, 59% insulin); ML predicted glycemic response r=0.77, TG r=0.47; person-specific factors (microbiome) explained 7.1% of TG variance vs 3.6% for meal macronutrients; genetics 9.5% (glucose), 0.8% (TG). Funded by Wellcome/MRC/BHF/NIH; authors linked to ZOE. (b) Zeevi 2015 (Cell, n=800, 46,898 meals, CGM; validated in n=100; small blinded 2-week crossover intervention lowered PPGR) - full text not retrievable here; abstract gives no coefficients. Independent replication: Mendes-Soares 2019 (JAMA Netw Open, n=327 US, NIDDK-funded): personalized model R=0.62 vs R=0.40 carbohydrate-only, R=0.34 calories-only. (c) RCTs acting on ML predictions: Ben-Yacov 2021 (Diabetes Care, n=225 prediabetes, 6 mo): personalized vs Mediterranean - time >140 mg/dL -1.3 vs -0.3 h/day; HbA1c -0.16% vs -0.08% (between-group -0.08%, P=0.007); OGTT no different. Rein 2022 (BMC Med, n=23 pilot crossover, […]

**Magnitude:** Predictive accuracy of cohort-trained ML for individual acute responses: glucose r=0.62-0.77 (i.e., 38-59% of variance), TG r=0.47 (22% of variance); baselines r=0.34-0.40. Within-person repeatability of the target signal: duplicate-meal CGM ICC 0.17-0.28; GI test intra-individual CV 20%. Clinical gains of acting on personalization (group level, best case): HbA1c between-arm difference -0.08% (prediabetes, 6 mo); time >140 mg/dL -1.0 h/day; TG […]

**Safety caveats:** A) Feedback-loop harm from noise-chasing: with CRP and CK noise this large, a per-user learner will attribute random dips to whichever additive was active and escalate it; the additive framing does not prevent harm because adding is dosing. B) Iron-absorption enhancers (citrus, vitamin C, heme pairing): HFE C282Y homozygosity is 1 in 156 in UK Biobank European-ancestry participants and only 21.7 percent of homozygous men and 9.8 percent of women were diagnosed (Pilling 2019, BMJ, PMID 30651232); LPI states high-dose vitamin C regimens may worsen iron overload in hemochromatosis. Ferritin is an acute-phase reactant and rises after exercise, so an inflammation-driven "low iron status" call from a single panel is unreliable; transferrin saturation and, where indicated, HFE genotype must gate […]

**What this means for the engine:** Replace "Dynamic Biological Twin that learns exactly" with "longitudinal biomarker record with explicit uncertainty." Concrete design rules the evidence supports: (a) Store per-analyte CVI/CVA and compute reference change values; do not update any graph weight from a delta smaller than the RCV, and never from a single follow-up draw. (b) Require […]

**Sources:**
- [Berry SE et al. 2020. Human postprandial responses to food and potential for precision nutrition. […]](https://doi.org/10.1038/s41591-020-0934-0)
- [Zeevi D et al. 2015. Personalized Nutrition by Prediction of Glycemic Responses. Cell](https://doi.org/10.1016/j.cell.2015.11.001)
- [Mendes-Soares H et al. 2019. Assessment of a Personalized Approach to Predicting Postprandial […]](https://doi.org/10.1001/jamanetworkopen.2018.8102)
- [Ben-Yacov O et al. 2021. Personalized Postprandial Glucose Response-Targeting Diet Versus […]](https://doi.org/10.2337/dc21-0162)
- [Rein M et al. 2022. Personalized diets by prediction of glycemic responses in newly diagnosed T2DM: […]](https://doi.org/10.1186/s12916-022-02254-y)
- [Popp CJ et al. 2022. Personalized Diet vs Low-fat Diet on Weight Loss: RCT. JAMA Netw Open](https://doi.org/10.1001/jamanetworkopen.2022.33760)

## C18. Blood anomalies can be mapped directly to actionable dietary solutions.

**README says:** "The database maps actionable solutions directly to objective blood anomalies using an Anabolic Synergy Index (ASI) solver"

**Evidence verdict:** overstated (confidence high). Grade: Mixed by component. General principle (blood phenotype -> personalized diet improves outcomes): human RCTs, mostly null or small (Food4Me n=1269; DIETFITS n=609; METHOD n=347; Popp n=204) with one […]

**Honest version:** A blood value can be mapped to a dietary action with good human evidence only when the biomarker is a status/deficiency marker for the nutrient being supplied (ferritin/TSAT -> iron; serum Mg -> magnesium; 25(OH)D -> vitamin D), and the effect is largest in people who are actually deficient. For the functional markers the README names (fasting insulin, hs-CRP, creatine kinase), (a) the markers are so noisy within one person (HOMA-IR CVI 26.7%; CRP CVI 42%, reference change value 118%; CK RCV +140%/-60%; athlete CK upper limit 2-6x the sedentary limit) that a single 'anomaly' usually cannot be distinguished from normal fluctuation, (b) the specific mappings proposed (Ceylon cinnamon + […]

**Key evidence:** AGAINST direct mapping of functional markers: (1) Food4Me RCT (Celis-Morales 2017, IJE; 1269 completers, 7 countries, 6 months): personalized advice beat generic advice on diet quality (HEI +1.27; saturated fat -1.14 %E; salt -0.65 g; red meat -5.5 g/d) but 'there was no evidence that including phenotypic [anthropometry + blood biomarkers] and phenotypic plus genotypic information enhanced the effectiveness'. (2) DIETFITS (Gardner 2018, JAMA; n=609, 12 months): insulin secretion at 30 min (INS-30) did not modify low-fat vs low-carb weight loss (interaction P=.47); genotype pattern P=.20. (3) Zoe METHOD (Bermingham 2024, Nat Med; n=347, 18 weeks; funded by Zoe Ltd, co-founders are authors, funder contributed to design/analysis/writing): personalized program using postprandial glucose/TG responses + microbiome reduced TG by 0.13 mmol/L; LDL NS; 'blood pressure, insulin, glucose, C-peptide ... did not differ between groups'; CRP did not differ. (4) Popp 2022 (JAMA Netw Open; n=204, NIH/AHA funded, DayTwo algorithm, Segal consultant): personalized PPGR diet weight loss -3.26% vs -4.31% […]

**Magnitude:** Biomarker-guided diet vs generic advice: Food4Me diet-quality HEI +1.27 points, phenotype/genotype add-on = 0 incremental benefit; DIETFITS weight difference 0.7 kg (CI -0.2 to 1.6), INS-30 interaction P=.47; METHOD TG -0.13 mmol/L, insulin/glucose/CRP = no difference; Popp weight -3.26% vs -4.31% (NS); Ben-Yacov HbA1c between-group ~0.08% (CI 0.02-0.14) and ~1 h/day less time >140 mg/dL; PERSON primary outcome null. Deficiency-repletion […]

**Safety caveats:** The additive framing does not make recommendations safe; "add X" is a dose decision made for a specific person, and every example in the README has a population for whom the add is harmful. (1) Cinnamon: most retail cinnamon and all sampled US cinnamon supplements are cassia, not Ceylon; coumarin is hepatotoxic in a susceptible human subgroup, TDI 0.1 mg/kg bw, reached with ~1 g/day of high-coumarin cassia; contraindicated or dose-limited in liver disease, with hepatotoxic drugs (case: cinnamon + statin hepatitis in a 73-year-old), and NCCIH states larger-than-food amounts are unsafe in pregnancy. Drug metabolism: cinnamon oil/cinnamic acid activate PXR (induces CYP3A4/CYP2B6/P-gp: risk of sub-therapeutic tacrolimus, cyclosporine, DOACs, oral contraceptives, some antiretrovirals) and […]

**What this means for the engine:** 1. Split the biomarker graph into two edge classes with different authority: (a) STATUS markers with validated repletion actions (ferritin/TSAT -> iron; serum/RBC Mg -> Mg; 25(OH)D -> D; B12/MMA -> B12; folate) where human RCT/meta-analysis effect sizes exist and are largest in deficient users; (b) FUNCTIONAL markers (fasting insulin/HOMA-IR, […]

**Sources:**
- [Cinnamon for diabetes mellitus (Cochrane Database Syst Rev 2012; Leach & Kumar)](https://doi.org/10.1002/14651858.CD007170.pub2)
- [Umbrella meta-analysis of cinnamon on glycemic control in T2D/PCOS (Zarezadeh 2023, Diabetol Metab […]](https://doi.org/10.1186/s13098-023-01057-2)
- [Cinnamon and glycemic control in T2DM: updated dose-response meta-analysis (Moridpour 2024, […]](https://doi.org/10.1002/ptr.8026)
- [Cinnamon supplementation on metabolic biomarkers in T2D: systematic review and meta-analysis (de […]](https://doi.org/10.1093/nutrit/nuae058)
- [Efficacy and safety of 'true' cinnamon (Cinnamomum zeylanicum) in diabetes: systematic review […]](https://doi.org/10.1111/j.1464-5491.2012.03718.x)
- [Ceylon cinnamon for diabetes: randomized double-blind placebo-controlled trial (Ranasinghe 2025, […]](https://doi.org/10.1016/j.dsx.2025.103357)

## C19. The laws of chemistry and taxonomic microbiology relevant to nutrition are rigid and immutable, i.e. context-free enough to be graph edges.

**README says:** "Traverses the rigid, immutable laws of chemistry and taxonomic microbiology (e.g., how an ingredient transforms into a prebiotic, feeds a microbe, alters a hormone, or competes for an enterocyte transporter)."

**Evidence verdict:** overstated (confidence high). Grade: Claim as stated: mechanistic speculation, supported only by in-vitro chemistry and single-meal fasting isotope studies. Counter-evidence: human RCT (n=440), controlled human stable-isotope absorption […]

**Honest version:** Only the lowest layer of the stack is immutable: reaction chemistry (ascorbate reduces Fe3+ to Fe2+; piperine inhibits UGT glucuronidation; ellagic acid is chemically convertible to urolithin A; DMT1 transports divalent cations). Everything the engine actually needs to recommend on, i.e. how much gets absorbed, whether a microbial conversion happens in THIS person, and whether a hormone or biomarker moves, is a conditional function of dose, meal matrix, acute vs chronic exposure, host regulatory state (hepcidin/iron stores/inflammation), host genotype (e.g. FUT2), and which strains the individual carries (urolithin/equol metabotypes). The README's own flagship examples fail as context-free […]

**Key evidence:** FLAGSHIP EDGE 1 - vitamin C -> iron absorption (README: 'Immutable Biochemical Laws (e.g., Vitamin C reduces Ferric Iron)'). (a) Cook & Reddy 2001, AJCN, n=12, iron absorption from a COMPLETE diet measured with labeled rolls at every meal for 5 days across three dietary periods spanning 51-247 mg/d vitamin C: no significant difference in mean iron absorption between periods; abstract explicitly contrasts the 'pronounced enhancing effect' in single fasting meals with 'negligible effect on iron balance of long-term supplementation'. Regression across pooled periods: phosphate negatively correlated (P=0.0005), ascorbate positively (P=0.0069), animal tissue positively (P=0.0285), i.e. the vitamin C edge is one term in a multivariate meal-matrix function, not a law. (b) Li et al. 2020, JAMA Netw Open, open-label single-centre equivalence RCT, n=440 adults with iron-deficiency anemia, 100 mg iron q8h with or without 200 mg vitamin C for 3 months: hemoglobin rise at 2 weeks 2.00 vs 1.84 g/dL (difference 0.16 g/dL, 95% CI -0.03 to 0.35), ferritin rise at 8 weeks 35.75 vs 34.48 ng/mL […]

**Magnitude:** Vitamin C on iron: single-meal enhancement is real and large in the classic isotope literature, but the whole-diet effect at 51-247 mg/d was not significant (n=12), and in a 440-patient RCT the incremental effect was 0.16 g/dL hemoglobin (95% CI -0.03 to 0.35) and 1.27 ng/mL ferritin (95% CI -0.70 to 3.24), i.e. indistinguishable from zero at 100 mg iron q8h. Hepcidin gating: fractional absorption falls 35-45% the day after a >=60 mg dose; 6x […]

**Safety caveats:** Populations for whom a purely "ADD" recommendation from context-free edges causes harm: (a) HFE hemochromatosis and other iron-loading states (thalassemia, transfusion-dependent, alcoholic liver disease; C282Y homozygosity is common in Northern-European ancestry per GeneReviews, exact prevalence not re-verified here): the vitamin C-with-iron edge is a harm edge; Milman 2021 instructs the opposite (tea/coffee/milk with meals, juice between). Note that high ferritin from red meat plus supplements is not rare in the target "gym rat" cohort, and ferritin is also an acute-phase reactant the engine could misread when hs-CRP is high. (b) Anyone on narrow-therapeutic-index or CYP3A4/P-gp/UGT-cleared drugs: phenytoin (documented AUC rise with 20 mg piperine), carbamazepine, […]

**What this means for the engine:** 1. Split the graph into two explicitly labelled layers: a CHEMISTRY layer (ChEBI/KEGG/Reactome reaction stoichiometry, transporter substrate lists; effectively immutable, evidence grade 'mechanistic') and a PHYSIOLOGY layer (absorption fraction, microbial conversion, biomarker response; conditional). Never let a chemistry-layer edge feed the ASI […]

**Sources:**
- [Cook JD, Reddy MB. Effect of ascorbic acid intake on nonheme-iron absorption from a complete diet. […]](https://pubmed.ncbi.nlm.nih.gov/11124756/)
- [Li N et al. The Efficacy and Safety of Vitamin C for Iron Supplementation in Adult Patients With […]](https://pubmed.ncbi.nlm.nih.gov/33136134/)
- [Moretti D et al. Oral iron supplements increase hepcidin and decrease iron absorption from daily or […]](https://pubmed.ncbi.nlm.nih.gov/26289639/)
- [Hallberg L et al. Calcium: effect of different amounts on nonheme- and heme-iron absorption in […]](https://pubmed.ncbi.nlm.nih.gov/1984335/)
- [Lonnerdal B. Calcium and iron absorption - mechanisms and public health relevance. Int J Vitam Nutr […]](https://pubmed.ncbi.nlm.nih.gov/21462112/)
- [Shoba G et al. Influence of piperine on the pharmacokinetics of curcumin in animals and human […]](https://pubmed.ncbi.nlm.nih.gov/9619120/)

## C20. Ingredients compete for enterocyte transporters (nutrient-nutrient absorption competition at the gut wall).

**README says:** "or competes for an enterocyte transporter"

**Evidence verdict:** partially_supported (confidence high). Grade: Human RCT/crossover isotope-absorption studies (dual radioisotope, stable isotope, whole-body counting; n=8-126 per study) plus one systematic review/dose-response meta-analysis (Ca-Fe; Abioye 2021) […]

**Honest version:** Some nutrients measurably inhibit each other's absorption in humans, and for a few pairs the site is plausibly a shared enterocyte uptake step: manganese vs iron (DMT1) is the best-supported case; zinc vs iron, calcium vs iron, and lutein vs beta-carotene are real in-human effects whose exact transporter attribution is either unproven or contradicted. The effect is strongly conditional: large (roughly 35-60% reduction) only for supplement-level doses taken in aqueous solution on an empty stomach at high molar ratios; small or absent at food-level doses inside a mixed meal (Zn-Fe: nil in a hamburger meal, milk, formula; Ca-Fe: pooled short-term absorption reduction only 5.6 absolute […]

**Key evidence:** FOR (direct competitive inhibition in humans): Rossander-Hultén 1991 (AJCN, dual radioisotope 55Fe/59Fe, paired design): adding 2.99 mg Mn to 0.01 mg Fe reduced fractional Fe absorption as much as raising the Fe dose 300-fold to 3 mg, in both water and a hamburger meal  -  classic kinetic signature of competition for a shared pathway; Illing 2012 (JBC, human DMT1 in Xenopus oocytes) independently shows Mn2+ and Co2+ competitively inhibit 55Fe2+ transport, so Mn-Fe is the one pair where human data and transporter data line up. ZINC-IRON: Sandström 1985 (J Nutr, 65Zn whole-body counting): Fe:Zn 25:1 in water cut Zn absorption from 59% to 34%; 1:1 and 2.5:1 had no effect; with a meal no inhibition at any ratio (25/23/22%); histidine ligand rescued to 47%. Rossander-Hultén 1991: 15 mg Zn/3 mg Fe reduced Fe absorption 56% in water solution but not in a hamburger meal. Olivares 2012 (Biometals, review of INTA Chile radioisotope studies): inhibition threshold Zn:Fe >=5.9:1 at 0.5 mg Fe but 1:1 at 10 mg Fe (fasting solution); no interaction in hamburger meal, premature formula, human milk […]

**Magnitude:** Fasting aqueous solution, supplement-level doses: Zn absorption -42% relative (59%->34%) at Fe:Zn 25:1 (Sandström); Fe absorption -56% at Zn:Fe 5:1 (Rossander-Hultén); Zn absorption 44%->23-26% with 100-400 mg Fe (Troost); Zn absorption 47%->20.5% with 60 mg Fe prenatal (O'Brien); Mn inhibited Fe equivalent to a 300-fold Fe dose increase. Calcium: -50-60% nonheme Fe in single meals at 165-600 mg Ca (Hallberg); -49% and -62% for Ca […]

**Safety caveats:** 1) Hemochromatosis / iron overload (HFE C282Y homozygotes, thalassaemia, transfusional overload, alcoholic liver disease): the README's flagship companion pair (citrus/vitamin C on greens, explicitly to convert Fe3+ to absorbable Fe2+) is the reverse of standard HH dietary advice (fruit and juice between meals, tea/coffee with meals, no iron or vitamin C supplements). At food doses the population signal is weak (citrus did not move ferritin in a 2232-person cohort), but the engine is optimising specifically for absorption, and any iron- or vitamin-C-supplement "add" is contraindicated. The engine must gate iron-enhancing edges on TSAT/ferritin/HFE status, which its own blood-panel loop can supply. 2) Piperine/black pepper: this is a pharmacokinetic intervention on every co-ingested […]

**What this means for the engine:** (a) Do not encode transporter competition as an "immutable biochemical law" hard edge in the graph layer; encode it as a conditional edge with parameters: nutrient pair, molar/weight ratio threshold, absolute dose, food matrix (fasting solution vs mixed meal vs dairy/formula), and time-scale (acute absorption vs long-term status). Concrete […]

**Sources:**
- [Rossander-Hultén L et al. 1991. Competitive inhibition of iron absorption by manganese and zinc in […]](https://doi.org/10.1093/ajcn/54.1.152)
- [Sandström B et al. 1985. Oral iron, dietary ligands and zinc absorption. J Nutr 115:411-4](https://doi.org/10.1093/jn/115.3.411)
- [Olivares M et al. 2012. Acute inhibition of iron bioavailability by zinc: studies in humans. […]](https://doi.org/10.1007/s10534-012-9524-z)
- [Troost FJ et al. 2003. Iron supplements inhibit zinc but not copper absorption in vivo in ileostomy […]](https://doi.org/10.1093/ajcn/78.5.1018)
- [O'Brien KO et al. 2000. Prenatal iron supplements impair zinc absorption in pregnant Peruvian […]](https://doi.org/10.1093/jn/130.9.2251)
- [Esamai F et al. 2014. Zinc absorption from micronutrient powder is low but is not affected by iron […]](https://doi.org/10.3390/nu6125636)

## C21. Adding companion ingredients can multiply performance, absorption and recovery.

**README says:** "It focuses entirely on what the user can add to their current meal matrix to multiply performance, absorption, and recovery."

**Evidence verdict:** overstated (confidence high). Grade: Mixed by sub-claim. ABSORPTION (iron, carotenoids): human single-meal isotope/postprandial crossover studies, replicated across labs (n=7-299 per study) = strong for acute absorption; but […]

**Honest version:** Adding specific companion ingredients can raise the ACUTE ABSORPTION of a small number of specific nutrients severalfold in single-meal human studies: co-consumed fat raises carotenoid absorption ~2.6-15x (essentially zero absorption from fat-free salad), and >=25-50 mg vitamin C raises non-heme iron absorption ~1.6-4x from an inhibitor-rich meal (up to ~9.6x at 1,000 mg in a semisynthetic meal), with the effect shrinking when meat is present. Those acute fold-changes largely disappear when measured over whole diets or as clinical status: vitamin C had no significant effect on iron absorption from complete 5-day diets, no effect on iron status after 5 weeks at 1,500 mg/d, and adding it to […]

**Key evidence:** FOR (acute absorption is genuinely multiplied): (1) Cook & Monsen 1977, 63 men, radioiron, semisynthetic meal: absorption ratio with/without ascorbic acid 1.65x at 25 mg to 9.57x at 1,000 mg; relative gain substantially smaller with meat. (2) Hallberg et al 1986, 299 subjects: enhancement largest in phytate/tannin-rich meals; ~50 mg vitamin C per main meal recommended for optimum effect; food-native and crystalline ascorbate equivalent. (3) Siegenberg 1991, 199 subjects: 30 mg ascorbic acid overcame maize-bran phytate inhibition; >=50 mg needed to overcome >100 mg tannic acid. (4) Hallberg & Hulthen 2000 algorithm: basal absorption 22.1% from inhibitor-free wheat roll multiplied by dose-effect terms for phytate, polyphenols, ascorbic acid, meat, calcium etc.; r2=0.987 against 24 measured meals. (5) Unlu 2005 (NIH-funded), n=11 crossover: 150 g avocado raised TRL-AUC 4.4x (lycopene) and 2.6x (beta-carotene) from salsa; 7.2x (alpha-carotene), 15.3x (beta-carotene), 5.1x (lutein) from salad; 75 g avocado or 24 g avocado oil equivalent. (6) Brown 2004, n=7: essentially no […]

**Magnitude:** Acute absorption (real multipliers): iron x1.65 (25 mg vit C) to x9.57 (1,000 mg) in semisynthetic meal; ~x2-4 at the 30-50 mg doses that overcome phytate/tannin; carotenoids x2.6-15.3 with 12-24 g fat vs none; near-zero absorption with fat-free dressing. Whole-diet iron absorption: no significant change across 51-247 mg/d vitamin C. Iron status: ferritin +1.2 ug/L (5 wk, 1,500 mg/d), NS. Clinical iron therapy: Hb +0.14-0.16 g/dL (95% CI […]

**Safety caveats:** Who is harmed by an ADD recommendation: (a) Undiagnosed HFE hemochromatosis (0.44% of non-Hispanic whites, most undiagnosed and already iron-loaded): routine "squeeze citrus on greens/iron foods" pushes bioavailable iron the wrong way; the engine's own ferritin/CRP loop must distinguish iron overload from inflammation before recommending iron enhancers. (b) Anyone on CYP3A4, P-gp, CYP2E1 or narrow-therapeutic-index drugs (carbamazepine, phenytoin, theophylline, propranolol, fexofenadine, diclofenac, cyclosporine, tacrolimus, digoxin, many statins, DOACs such as apixaban/rivaroxaban which are P-gp/CYP3A4 substrates): 20 mg piperine, achievable with a few hundred milligrams of black pepper if pepper is ~5-9% piperine (that percentage was not independently verified in this session), raises […]

**What this means for the engine:** (1) Separate endpoint layers on every edge: acute absorption (isotope/plasma AUC) vs nutrient status vs functional outcome (performance, recovery). Fold-changes must never propagate across layers; vitamin C-iron is the canonical case where x2-4 acute absorption collapses to +0.14 g/dL Hb. (2) Replace the 'Anabolic Synergy Index' notion of […]

**Sources:**
- [Cook & Monsen 1977 - Vitamin C, the common cold, and iron absorption (Am J Clin Nutr)](https://doi.org/10.1093/ajcn/30.2.235)
- [Hallberg, Brune, Rossander 1986 - Effect of ascorbic acid on iron absorption from different types […]](https://pubmed.ncbi.nlm.nih.gov/3700141/)
- [Siegenberg et al 1991 - Ascorbic acid prevents the dose-dependent inhibitory effects of polyphenols […]](https://doi.org/10.1093/ajcn/53.2.537)
- [Hallberg & Hulthén 2000 - Prediction of dietary iron absorption: an algorithm (Am J Clin Nutr)](https://doi.org/10.1093/ajcn/71.5.1147)
- [Cook & Reddy 2001 - Effect of ascorbic acid intake on nonheme-iron absorption from a complete diet […]](https://doi.org/10.1093/ajcn/73.1.93)
- [Hunt et al 1994 - Effect of ascorbic acid on apparent iron absorption by women with low iron stores […]](https://doi.org/10.1093/ajcn/59.6.1381)

## C22. Semantic embedding of subjective state (e.g. 'sore') can be matched to biological recovery pathways.

**README says:** "Encodes messy inputs into semantic 'State' coordinates - Matches 'Sore' to 'Recovery Pathways'"

**Evidence verdict:** partially_supported (confidence medium). Grade: Mixed by sub-claim. Embedding/entity-linking step: computational benchmarks only (no human outcome). Soreness-tracks-biology step: human experimental studies (N=110; N=286), one narrative methods […]

**Honest version:** The technically defensible version: "Biomedical entity-linking embeddings can map lay free-text like 'sore' to controlled-vocabulary concepts (UMLS/HPO/SNOMED: myalgia, delayed-onset muscle soreness) with ~92-96% top-1 accuracy on formal text but only ~66-71% top-1 on lay/social-media language; those concept IDs can then be joined by graph traversal to curated pathway/compound nodes in existing knowledge graphs (PrimeKG, MeNu GUIDE) to anchor a query." What the README's phrasing overstates: (1) that self-reported soreness identifies a specific biological "recovery pathway" - DOMS pathophysiology is explicitly described as unknown/multifactorial (Hotfiel 2018), and perceived soreness […]

**Key evidence:** FOR (technical feasibility of the embedding step): Liu et al. 2021 (NAACL; arXiv 2010.11784) self-aligned biomedical entity-linking encoder, unsupervised top-1 accuracy: NCBI-disease 92.0%, BC5CDR-disease 93.5%, BC5CDR-chemical 96.5%, MedMentions 50.8% (top-5 74.4%), but on patient/social-media language AskAPatient 70.5% (top-5 88.9%) and COMETA 65.9% (top-5 77.9%); authors attribute the drop to informal terminology. Wei et al. 2024 (Clin Microbiol Infect, PMID 37949111): a commercial LLM converting free-text symptom narratives to structured labels reached sensitivity 0.853-1.000 and specificity 0.947-1.000 for common symptoms, but sensitivity 0.200-1.000 for less common symptoms; few-shot prompting improved both. Zeinali et al. 2024 (PMID 38789092): domain-adapted transformer detecting symptoms in 1,112 annotated oncology notes: internal micro-F1 0.933, external validation F1 0.831; physical symptoms detected better than psychological. Graph-side feasibility: PrimeKG (Chandak et al. 2023, Sci Data, PMID 36732524) links 17,080 diseases via 4,050,249 edges across phenotypes, […]

**Magnitude:** Entity linking of lay text to ontology: 66-71% top-1 / 78-89% top-5 accuracy (vs 92-96% on formal text) - i.e., roughly 1 in 3 lay inputs mis-anchored at top-1. LLM symptom labelling: sensitivity 0.85-1.00 common symptoms, 0.20-1.00 uncommon. Soreness vs objective damage: r < 0.32 (N=110), palpation soreness r ~ 0; MVC loss after identical exercise ranges 18% to 58% across responder clusters (N=286). Subjective wellness vs training load: r = […]

**Safety caveats:** The "additive-only" framing does not remove risk; an addition is a dose change, and repeated additions stack. Population-specific harms if the engine tells someone to "add" a recovery food or supplement for "sore": (1) Athletes on any CYP3A4 or P-gp substrate (statins, calcium-channel blockers, some antihistamines, antiepileptics, theophylline, immunosuppressants, some antiretrovirals)  -  black pepper/piperine at 20 mg/day raises drug exposure. (2) Transplant recipients on tacrolimus  -  turmeric case of nephrotoxicity. (3) HLA-B*35:01 carriers and anyone taking concentrated turmeric/curcumin products  -  hepatocellular liver injury, 1 death in the DILIN series; piperine co-formulation increases exposure. (4) Kidney-stone formers and CKD  -  turmeric raises urinary oxalate; magnesium […]

**What this means for the engine:** 1) Rename and scope the vector layer as what it is: a fuzzy entity linker from lay text to ontology IDs (HPO/SNOMED/MeSH), returning top-k candidates with confidence; below a threshold (~0.7 cosine or non-dominant top-1) ask a one-line clarifier (body region, hours since session, pain 0-10, swelling/weakness/dark urine yes-no) rather than guess. […]

**Sources:**
- [Delayed-onset muscle soreness does not reflect the magnitude of eccentric exercise-induced muscle […]](https://pubmed.ncbi.nlm.nih.gov/12453160/)
- [Monitoring the athlete training response: subjective self-reported measures trump commonly used […]](https://pubmed.ncbi.nlm.nih.gov/26423706/)
- [Measurement tools used in the study of eccentric contraction-induced injury (Warren, Lowe & […]](https://pubmed.ncbi.nlm.nih.gov/10028132/)
- [Susceptibility to exercise-induced muscle damage: a cluster analysis with a large sample (Damas et […]](https://pubmed.ncbi.nlm.nih.gov/27116346/)
- [Advances in Delayed-Onset Muscle Soreness (DOMS): Part I: Pathogenesis and Diagnostics (Hotfiel et […]](https://pubmed.ncbi.nlm.nih.gov/30537791/)
- [Recovery and Performance in Sport: Consensus Statement (Kellmann et al. 2018)](https://pubmed.ncbi.nlm.nih.gov/29345524/)

## C23. Generic clinical/fitness advice ('balanced diet, regular exercise') is fundamentally true but lacks specificity and actionability.

**README says:** "While fundamentally true, this advice lacks personal specificity and actionability."

**Evidence verdict:** partially_supported (confidence high). Grade: Half A ("fundamentally true"): meta-analyses of large prospective cohorts (>30M participants for physical activity; 3.3M for diet quality) plus meta-analysis of RCTs with hard CVD endpoints (USPSTF […]

**Honest version:** "Balanced diet, regular exercise" is not merely "fundamentally true"; it is among the best-supported causal claims in preventive medicine, and even when delivered as generic guideline advice it measurably changes behavior and hard outcomes (NNT 12 to move one sedentary adult to recommended activity at 12 months; RR 0.80 for CVD events with multisession counseling). Its real weakness is adherence, not truth or actionability. Adding specificity does help, but the replicated gains come from BEHAVIORAL specificity (advice anchored to what the person currently eats, concrete goals, if-then plans, self-monitoring, repeated re-tailoring), worth roughly d = 0.1-0.35 over generic advice. BIOLOGICAL […]

**Key evidence:** FOR "fundamentally true": (1) Garcia 2023 BJSM dose-response meta-analysis, 94 cohorts, >30M participants: all-cause mortality RR 0.69 (0.65-0.73) at 8.75 mMET-h/wk (= the generic 150 min/wk recommendation); 15.7% of premature deaths averted if all inactive adults reached that level. (2) Ekelund 2019 BMJ, accelerometer-measured, n=36,383: HR 0.27 (0.23-0.32) most vs least active quartile. (3) Morze/Schwingshackl 2020, 113 reports, 3,277,684 participants: highest vs lowest diet quality RR 0.80 all-cause mortality, 0.80 CVD, 0.81 T2D. (4) Sotos-Prieto 2017 NEJM: a 20-percentile improvement in diet score associated with 8-17% lower total mortality. AGAINST "lacks actionability" (generic advice does act): (5) Orrow 2012 BMJ, 15 RCTs, n=8,745: primary-care PA promotion OR 1.42 (1.17-1.73), SMD 0.25, NNT 12 at 12 months. (6) Rees 2013 Cochrane, 44 RCTs, n=18,175: dietary advice vs none lowered total cholesterol 0.15 mmol/L, LDL 0.16, SBP 2.61 mmHg, DBP 1.45. (7) O'Connor 2020 USPSTF evidence report, 94 RCTs, N=52,174: guideline-content counseling reduced CVD events RR 0.80 (0.73-0.87). […]

**Magnitude:** Generic advice content, if followed: ~31% lower all-cause mortality at 150 min/wk MVPA (RR 0.69); ~20% lower all-cause mortality for high vs low diet quality (RR 0.80); 20% relative reduction in CVD events with counseling (absolute 4.4% to 3.6% in PREDIMED). Generic advice as delivered: OR 1.42 / SMD 0.25 for PA at 12 mo (NNT 12); total cholesterol -0.15 mmol/L; SBP -2.6 mmHg. Personalization premium over generic (behavioral tailoring): r=0.074 […]

**Safety caveats:** The additive framing ('keep eating your meal, just ADD') does not make recommendations safe by construction, for four structural reasons: (1) additions stack on existing intake  -  gym-user supplement stacks already push folic acid, vitamins A, B6 and C past ULs (Bailey 2012), so 'add' without a cumulative ledger can breach ULs/TDIs; (2) the README's core 'unlock keys' are absorption/metabolism enhancers (vitamin C, piperine, fat), which change the kinetics of whatever else the person is taking  -  iron, CYP3A4/P-gp substrate drugs  -  not just the target nutrient; (3) 'add' has no dose ceiling unless the engine models dose; (4) 'keep eating your meal' presumes the base meal is benign (a 4 g cassia-cinnamon smoothie is not). Populations at concrete risk from the README's own examples: […]

**What this means for the engine:** 1. Reframe the problem statement: the gap is adherence and behavioral specificity, not biological specificity. The evidence-backed levers are (i) personalizing to what the user already eats (Food4Me Level 1 was the whole effect), (ii) implementation intentions of the form "when I cook X, I add Y" (d=0.65), (iii) self-monitoring with feedback […]

**Sources:**
- [Garcia L et al. 2023. Non-occupational physical activity and risk of cardiovascular disease, cancer […]](https://doi.org/10.1136/bjsports-2022-105669)
- [Ekelund U et al. 2019. Dose-response associations between accelerometry measured physical activity […]](https://doi.org/10.1136/bmj.l4570)
- [Morze J, Danielewicz A, Hoffmann G, Schwingshackl L. 2020. Diet quality (HEI, AHEI, DASH) and […]](https://doi.org/10.1016/j.jand.2020.08.076)
- [Sotos-Prieto M et al. 2017. Association of Changes in Diet Quality with Total and Cause-Specific […]](https://doi.org/10.1056/NEJMoa1613502)
- [O'Connor EA et al. 2020. Behavioral Counseling to Promote a Healthy Diet and Physical Activity for […]](https://doi.org/10.1001/jama.2020.17108)
- [US Preventive Services Task Force 2020. Behavioral Counseling Interventions ... Adults With […]](https://doi.org/10.1001/jama.2020.21749)

## C24. Standard biological databases are heavily siloed but can be joined via universal identifiers; FooDB/ChEBI/KEGG/Reactome/UniProt/HMDB/VMH/MeSH cover food->compound->enzyme->pathway->protein->hormone/microbe/behaviour.

**README says:** "Because standard biological databases are heavily siloed, the engine acts as an overarching semantic layout, weaving fragmented global standards together via their universal identifiers"

**Evidence verdict:** partially_supported (confidence high). Grade: Not a human-outcome claim; the "human RCT/meta-analysis" lens does not apply. Assessed against primary database documentation, peer-reviewed database papers (Nucleic Acids Research, Nature […]

**Honest version:** Biological databases are genuinely fragmented: the same metabolite carries different, often conflicting identifiers across KEGG, ChEBI, HMDB, BiGG, MetaCyc, Reactome, SEED and SwissLipids (measured pairwise inconsistency up to 83.1%, most pairs <50% overlap, name-to-ID ambiguity up to 29%), and food vocabularies are siloed too. They CAN be joined, but not by any single "universal identifier": joining relies on curated cross-reference tables (ChEBI, HMDB, VMH each list KEGG/PubChem/HMDB/ChEBI IDs on 90-97% of their entries), on structure-hash hubs (InChIKey via UniChem, which covers FooDB/HMDB/ChEBI/PubChem but excludes KEGG), and on reconciliation namespaces (MetaNetX/MNXref) that still […]

**Key evidence:** SILOING (supports the premise): Pham et al. 2019 (Metabolites 9:28; PMID 30736318) mapped metabolite names/IDs across 11 databases (BiGG, ChEBI, enviPath, HMDB, KEGG, LIPID MAPS, MetaCyc, Reactome, SABIO-RK, SEED, SwissLipids): maximum inconsistency 83.1% (ChEBI IDs -> BiGG), "less than 50% overlap in most pairwise comparisons", best pair 67.7% (MetaCyc -> SEED via MNXref), name ambiguity up to 29.43% (Reactome), "nearly 100% of IDs are linked to more than 1 name" in ChEBI/HMDB/MetaCyc/SwissLipids/LIPID MAPS, and conclusion that "manual verification of the mappings appears to be the only solution". Bernard et al. 2014 (Brief Bioinform, PMID 23172809) and Moretti et al. 2016/2021 (NAR, PMIDs 26527720, 33156326) exist specifically because of this; MNXref 4.0 reconciles 13 sources into 1,045,319 metabolite and 37,103 reaction entries, with an average of only 1.23 source identifiers per reconciled metabolite (i.e., most metabolite records live in a single source) versus 4.3 per entry for the shared core used by genome-scale models. MNXref documentation states "the protonation state […]

**Magnitude:** Cross-database identifier inconsistency: up to 83.1% (ChEBI->BiGG), most pairs <50% consistent, best 67.7%; name ambiguity up to 29.43% (Pham 2019, 11 databases, 5,102-1,218,750 names per database). MNXref 4.0: 1,045,319 metabolites, 37,103 reactions, 13 sources, mean 1.23 source IDs per metabolite entry (4.3 for model-core metabolites), ~99.7% one-to-one reaction mapping for a well-annotated model (2,368/2,376, E. coli iAF1260). VMH […]

**Safety caveats:** The additive framing does not remove risk; an 'add' is a dose change, and every README example has a defined harmed population that none of the eight listed databases can identify. Epilepsy/phenytoin, theophylline, propranolol, and by extension narrow-index CYP3A4/P-gp substrates (tacrolimus, cyclosporine, some statins, apixaban/rivaroxaban): 'add black pepper' at supplement-equivalent piperine (20 mg ~ several grams of pepper or a 'bioperine' capsule) raises drug exposure; culinary pinches are probably below effect threshold but the engine cannot know which the user will do. Turmeric + piperine 'stacks' are the exact product class in DILIN liver-failure cases, with HLA-B*35:01 carriers at ~8x allele enrichment; culinary turmeric at 10 g/d showed no tacrolimus effect in one patient, so […]

**What this means for the engine:** Concrete design consequences: (a) Do not model identity on "universal identifiers"; build a canonicalisation layer: MNXref namespace (already reconciles ChEBI, HMDB, KEGG, MetaCyc, BiGG, SEED, SwissLipids, LIPID MAPS, Reactome, Rhea, SABIO-RK, enviPath, VMH) plus UniChem/InChIKey first-block matching for FooDB->HMDB/ChEBI/PubChem, plus explicit […]

**Sources:**
- [Pham N et al. 2019. Consistency, Inconsistency, and Ambiguity of Metabolite Names in Biochemical […]](https://doi.org/10.3390/metabo9020028)
- [Moretti S et al. 2021. MetaNetX/MNXref: unified namespace for metabolites and biochemical reactions […]](https://doi.org/10.1093/nar/gkaa992)
- [Moretti S et al. 2016. MetaNetX/MNXref - reconciliation of metabolites and biochemical reactions to […]](https://doi.org/10.1093/nar/gkv1117)
- [Bernard T et al. 2014. Reconciliation of metabolites and biochemical reactions for metabolic […]](https://doi.org/10.1093/bib/bbs058)
- [MetaNetX MNXref 4.5 documentation (sources, protonation and stereo handling)](https://www.metanetx.org/mnxdoc/mnxref.html)
- [Noronha A et al. 2019. The Virtual Metabolic Human database: integrating human and gut microbiome […]](https://doi.org/10.1093/nar/gky992)

## C25. ArcadeDB combines a native graph engine, an LSM-powered vector search engine and a document store under a single ACID transaction boundary, with index-free adjacency traversal unaffected by storing dense JSON on nodes.

**README says:** "ArcadeDB, a multi-model database that combines a native Graph Engine, an LSM-powered Vector Search Engine, and a Document Store under a single ACID transaction boundary ... without sacrificing index-free graph traversal speeds."

**Evidence verdict:** partially_supported (confidence high). Grade: Not a biomedical claim; the human-evidence hierarchy does not apply. Nearest analogue: manufacturer/mechanistic claim, partially verified against primary source. Architecture facts (graph storage […]

**Honest version:** ArcadeDB (Apache-2.0, Java, single-vendor project led by Luca Garulli) is genuinely one storage engine that stores graph vertices/edges, schema-less JSON documents and vector embeddings in the same page files under one transaction manager with a WAL and MVCC page versioning; a vertex IS a document (25-byte header holding out/in edge-list RIDs followed by inline properties), and edges are traversed by direct RID pointer-chasing through linked edge segments with no index lookup, so "native graph + document store + index-free adjacency" is accurate. The vector side is accurate but newer and less settled than the wording implies: since 25.11.1 the dense index type LSM_VECTOR is an LSM-style […]

**Key evidence:** FOR (verified in source/docs): (1) GitHub README: "fully transactional DBMS with support for ACID transactions ... native graph engine (no joins but links between records)"; models listed: Graph, Document, Key/Value, Search Engine, Time Series, Vector Embedding; latest release 26.9.1 (3 Sep 2026). (2) ImmutableVertex.java: record = 1-byte type + out-edge RID (int+long) + in-edge RID (int+long) = 25-byte fixed prefix, then properties; edge head RIDs are parsed first and properties are lazily loaded. (3) EdgeLinkedList.java: edges stored newest-first in chained EdgeSegment chunks; each hop loads the chunk via database.lookupByRID(chunkRID) - direct page/offset load, no index; geometric chunk growth (64,128,... doubling); super-node promotion to striped lists >4,096 edges (26.9.1 notes). (4) docs/concepts/multi-model: "all models share the same storage layer, the same transaction manager, and the same query infrastructure ... A single ACID transaction can create a document, connect it as a vertex in a graph, and index its embedding for vector similarity - atomically." (5) […]

**Magnitude:** No quantitative evidence exists, from vendor or third parties, for the specific claim that traversal speed is unchanged when dense JSON sits on vertices; the only vendor statement on the topic (#4027) is qualitative and negative ("cache misses and I/O"). Order-of-magnitude reasoning from verified constants: default page 64 KB; vertex header 25 bytes; a FooDB-style abstract/recipe JSON of 5-30 KB per vertex means ~2-12 vertices per page instead […]

**Safety caveats:** The database claim itself harms no one; the harm pathway is what the schema fails to represent. As described, the README architecture has vertices for biochemistry, microbes, foods and user state, an 'Anabolic Synergy Index' that sums positive weights, and an output restricted to 'ADD'. Nothing in that design is a blocking edge. ArcadeDB does not prevent negative edges (CONTRAINDICATED_FOR, INTERACTS_WITH, EXCEEDS_UL_FOR) between user-condition/medication nodes and food/compound nodes; the product philosophy does. Concrete populations harmed by the README's own three canonical 'adds': (1) Citrus on greens (ascorbate -> ferrous iron): hereditary hemochromatosis (~1/225 Northern European ancestry homozygous C282Y, 1/15 carriers; NIDDK), thalassemia and transfusion-dependent iron overload; […]

**What this means for the engine:** (1) ArcadeDB is a defensible choice for the stated need (graph of nutrient/enzyme/microbe relations + JSON ingredient/recipe metadata + embeddings of free-text user state, all in one store, embeddable in-JVM, Apache-2.0, Cypher/Gremlin/SQL). The README should describe it as "one engine with one transaction manager" rather than implying a proven, […]

**Sources:**
- [ArcadeDB GitHub README (models, ACID, native graph engine, release 26.9.1)](https://github.com/ArcadeData/arcadedb)
- [arcadedb.com product page (marketing claims: single engine, 100% ACID, HNSW vector, traversal […]](https://arcadedb.com/)
- [ArcadeDB docs - Transactions (ACID, MVCC, isolation levels, txWalFlush)](https://docs.arcadedb.com/arcadedb/concepts/transactions.html)
- [ArcadeDB docs - Vector Search (LSM_VECTOR on JVector 4.0.0, quantization, 26.10.1 transactional […]](https://docs.arcadedb.com/arcadedb/concepts/vector-search.html)
- [ArcadeDB docs - Multi-Model (single storage layer / transaction manager claim)](https://docs.arcadedb.com/arcadedb/concepts/multi-model.html)
- [ArcadeDB docs - Graphs (endpoint references stored as vertex properties)](https://docs.arcadedb.com/arcadedb/concepts/graphs.html)

## C26. The project's domain is metabolomics and nutrigenomics, and blood panels can deliver 'metabolomics & nutrigenomics' diagnostics.

**README says:** "sequential blood panel diagnostics (Metabolomics & Nutrigenomics)"

**Evidence verdict:** overstated (confidence high). Grade: Mixed by sub-claim. Nutrigenomics adds benefit over standard personalisation: contradicted by human RCTs (Food4Me n=1,269 completers; DIETFITS n=609) and meta-analysis of 18 RCTs (Hollands 2016); one […]

**Honest version:** The README conflates three different things under one label. (1) The biomarkers it actually names (hs-CRP, fasting insulin, creatine kinase) are routine clinical chemistry, not metabolomics. (2) Metabolomics proper (targeted/untargeted MS or NMR profiling of ~150-1000 metabolites, e.g. Biocrates, Nightingale NMR 249-measure panel) is available from blood but is a research-grade tool: median within-person test-retest ICC ~0.5-0.7 over 4 months to 2 years, biomarkers of food intake mostly unvalidated, and no RCT has shown that blood-metabolomics-derived recommendations improve outcomes. The closest evidence, personalised programs built on postprandial glucose/TG responses plus microbiome (ZOE […]

**Key evidence:** AGAINST the nutrigenomics component: (a) Food4Me RCT (Celis-Morales 2017, Int J Epidemiol; 7 EU countries; 1,269 completers; MRC/EU funded): arms were generic advice vs personalised on diet vs diet+phenotype (anthropometry + blood biomarkers) vs diet+phenotype+genotype (5 diet-responsive variants). Personalised advice beat generic (saturated fat -1.14 %E, salt -0.65 g, red meat -5.48 g/d, Healthy Eating Index +1.27 points) but "there was no evidence that including phenotypic and phenotypic plus genotypic information enhanced the effectiveness"; i.e. the blood-biomarker and genotype layers added zero. (b) DIETFITS (Gardner 2018, JAMA; n=609; NIH-funded): 12-month weight loss -5.3 kg low-fat vs -6.0 kg low-carb (difference 0.7 kg, 95% CI -0.2 to 1.6); no diet x 3-SNP genotype-pattern interaction (P=0.20) and no diet x insulin-secretion interaction (P=0.47). Neither genotype nor a blood insulin phenotype identified who should eat which diet. (c) Hollands 2016 BMJ meta-analysis (18 RCTs, 10,515 abstracts screened): communicating DNA-based risk had no effect on diet (SMD 0.12, 95% CI […]

**Magnitude:** Incremental value of genotype over personalised advice: Food4Me, no detectable added effect on any dietary or biomarker outcome (n=1,269); DIETFITS, interaction P=0.20, between-diet weight difference 0.7 kg (CI crosses 0). Genetic risk communication on diet: SMD 0.12 (95% CI -0.00 to 0.24), i.e. a trivial-to-small effect with the CI touching zero. Genetic share of postprandial response variance: 9.5% (glucose), 0.8% (TG), 0.2% (C-peptide). Best […]

**Safety caveats:** Populations that can be harmed if the engine acts on a 'sequential blood panel' with the README's example additions: (a) Iron overload (HFE C282Y homozygotes ~1 in 230 non-Hispanic whites; transfusion-dependent thalassaemia, not searched here): AASLD 2011 grade 1C 'Vitamin C supplements and iron supplements should be avoided'; pharmacological vitamin C mobilises iron, saturates transferrin and increases pro-oxidant activity, with sudden-death risk in iron-loaded cardiomyopathy. The engine's 'Vitamin C reduces ferric iron' unlock and its 'Vitamin C + Copper + Proline' repair prescription are both contraindicated as supplements here; food-dose citrus is low risk. (b) Wilson disease: managed with low-copper diet and zinc; recommending copper-rich additions is contraindicated. (c) […]

**What this means for the engine:** 1. Rename the layer honestly: "clinical biomarker feedback loop," not "Metabolomics & Nutrigenomics diagnostics." Metabolomics and nutrigenomics are legitimate knowledge sources for the graph (HMDB, FooDB, KEGG edges) but are not what a blood panel returns. 2. Drop genotype as a recommendation weight; the best RCT evidence (Food4Me, DIETFITS) […]

**Sources:**
- [Celis-Morales et al. 2017, Effect of personalized nutrition on health-related behaviour change: […]](https://doi.org/10.1093/ije/dyw186)
- [Gardner et al. 2018, DIETFITS RCT: low-fat vs low-carb and association with genotype pattern or […]](https://doi.org/10.1001/jama.2018.0245)
- [Hollands et al. 2016, Impact of communicating genetic risks of disease on risk-reducing health […]](https://doi.org/10.1136/bmj.i1102)
- [Bermingham et al. 2024, Effects of a personalized nutrition program on cardiometabolic health: RCT […]](https://doi.org/10.1038/s41591-024-02951-6)
- [Berry et al. 2020, Human postprandial responses to food and potential for precision nutrition […]](https://doi.org/10.1038/s41591-020-0934-0)
- [Zeevi et al. 2015, Personalized Nutrition by Prediction of Glycemic Responses, Cell](https://doi.org/10.1016/j.cell.2015.11.001)

## C27. Medicine interactions and allergies can be made uniquely traceable per user from medical research and open data.

**README says:** "interactions with medicines, allergies, and more would be uniquely traceable for each user using medical research and open data"

**Evidence verdict:** partially_supported (confidence high). Grade: Mixed by sub-claim. Drug-gene interaction personalization: human RCT/cluster-RCT (PREPARE, Lancet 2023; PREDICT-1, NEJM 2008) and large prospective screening cohort (Chen 2011 NEJM) - strongest tier. […]

**Honest version:** Population-level drug-drug and food/herb-drug interaction knowledge is genuinely available from open or freely usable sources (NLM DailyMed SPL labels with bulk XML download; DDInter with ~0.24M DDI pairs across 1,833 approved drugs; the CPIC guideline API with 29 gene-drug guidelines; openFDA FAERS as an uncurated signal source). A small set of food-drug interactions is well characterized in human pharmacokinetic studies (grapefruit-CYP3A4: felodipine bioavailability 284% of water control, range 164-469%; St John's wort: indinavir AUC -57%). Making any of this "unique to a user" requires private, non-open inputs: a verified current medication list and, for the only personalization layer […]

**Key evidence:** FOR (interactions can be looked up from open data): DDInter is free without registration and holds ~0.24M DDI associations across 1,833 approved drugs with severity/mechanism/management annotations (Xiong 2022, NAR). DailyMed (NLM) provides all FDA drug labels including Drug Interactions sections as bulk-downloadable XML, though NLM does not review SPL content before publication. CPIC guidelines are served from a public REST API (29 guidelines incl. CYP2C19-clopidogrel, CYP2C9/VKORC1-warfarin, HLA-B-abacavir, HLA-A/B-carbamazepine, DPYD-fluoropyrimidines, SLCO1B1-statins, TPMT/NUDT15-thiopurines). DrugBank: only the "Open Data" subset is CC0; the full dataset (which contains the DDI and food-interaction tables) is CC BY-NC 4.0 restricted to academic users, and academic downloads were paused at time of check - a commercial engine cannot use it without a license. FOR (per-user drug-gene interactions are real and outcome-changing): PREPARE (Swen 2023, Lancet): 6,944 patients, 7 European countries, open-label cluster-randomized crossover; 12-gene panel; clinically relevant ADRs 21.0% vs […]

**Magnitude:** Pharmacogenomic personalization (the only per-user layer with RCT support): ADR relative reduction 30% (OR 0.70), absolute reduction 6.7-7.1 percentage points (PREPARE, n=6,944). HLA-B*57:01 screening: confirmed abacavir hypersensitivity 2.7% -> 0% (n=1,956). HLA-B*15:02 screening: ~10 expected SJS/TEN -> 0 (n=4,877). 99% of people carry >=1 actionable variant (n=1,013). Drug-gene + drug-drug-gene interactions add 51.3% more potentially […]

**Safety caveats:** Mapping the README's own "ADD" outputs to who gets hurt: (a) "Squeeze lemon on greens to maximise iron absorption"  -  anti-aligned for hereditary hemochromatosis (~1 in 150 of northern-European ancestry, most undiagnosed), thalassaemia and other iron-overload states; citrus at food doses is minor, but an engine whose objective is "maximise iron uptake" will systematically push these users the wrong way, and the diagnosis requires TSAT/ferritin, not open data. (b) "Add black pepper"  -  piperine inhibits intestinal/hepatic CYP3A4, P-gp and UGT; documented human increases for phenytoin, carbamazepine, theophylline, propranolol, nevirapine; by mechanism tacrolimus/cyclosporine and other narrow-therapeutic-index CYP3A4/P-gp substrates are at risk; the interaction was demonstrated with a […]

**What this means for the engine:** 1. Re-scope the claim: implement a "population-level interaction and declared-allergen flag layer", not "unique traceability". 2. Data sources that are actually usable: DailyMed SPL bulk XML (parse Drug Interactions / Contraindications sections; label-level evidence tier), DDInter (free; 0.24M pairs; carries severity + mechanism + management), […]

**Sources:**
- [Swen JJ et al. A 12-gene pharmacogenetic panel to prevent adverse drug reactions (PREPARE). Lancet […]](https://doi.org/10.1016/S0140-6736(22)01841-4)
- [Mallal S et al. HLA-B*5701 screening for hypersensitivity to abacavir (PREDICT-1). NEJM 2008](https://doi.org/10.1056/NEJMoa0706135)
- [Chen P et al. Carbamazepine-induced toxic effects and HLA-B*1502 screening in Taiwan. NEJM 2011](https://doi.org/10.1056/NEJMoa1009717)
- [Ji Y et al. Preemptive pharmacogenomic testing: five actionable genes, 99% carry an actionable […]](https://doi.org/10.1016/j.jmoldx.2016.01.003)
- [Verbeurgt P et al. How common are drug and gene interactions? 1143 genotyped patients. […]](https://doi.org/10.2217/pgs.14.6)
- [Relling MV, Klein TE. CPIC: Clinical Pharmacogenetics Implementation Consortium. Clin Pharmacol […]](https://doi.org/10.1038/clpt.2010.279)

## C28. The system's outputs carry no liability; validity is established only by observed effectiveness, data quality and individual response.

**README says:** "liability. there is none. you can only trust the outputs based on how effectively they have been, the quality of data provided, and whether ot actually works for you."

**Evidence verdict:** unsupported (confidence high). Grade: Claim itself: unsourced assertion (marketing/philosophy-level). Evidence against: (a) primary statutory and regulatory text (EU Directive 2024/2853; EU Regulation 2017/745 + MDCG 2019-11; UK UCTA […]

**Honest version:** "This project will be released as open-source software under a licence that disclaims warranties (e.g., MIT 'AS IS'). That disclaimer limits contractual claims between developers and users of the code; it does not remove product-liability, negligence, medical-device or data-protection obligations for anyone who deploys the engine to consumers, and in the UK/EU it cannot exclude liability for personal injury at all. The EU Product Liability Directive treats software and AI systems as products; it excludes only free/open-source software supplied outside a commercial activity, and the moment the engine is integrated into a paid app or SaaS that exclusion is lost and liability cannot be […]

**Key evidence:** LEGAL/REGULATORY (contradicts "there is none"): (1) EU Product Liability Directive 2024/2853, applying to products placed on the market after 9 Dec 2026: Art 4(1) defines "product" to include software; Recital 13 explicitly names "AI systems" and SaaS; Art 2(2) excludes only "free and open-source software that is developed or supplied outside the course of a commercial activity"; Recital 15 says a manufacturer who integrates such FOSS into a commercial product is liable; Art 15: liability "is not, in relation to the injured person, limited or excluded by a contractual provision or by national law." (2) UK Unfair Contract Terms Act 1977 s2(1): "A person cannot by reference to any contract term or to a notice given to persons generally or to particular persons exclude or restrict his liability for death or personal injury resulting from negligence"; Consumer Rights Act 2015 s65(1)-(2) repeats this for consumer notices and adds that agreeing to or knowing about the notice is not voluntary acceptance of risk. (3) FDA Clinical Decision Support Software guidance (final, 29 Jan 2026): the […]

**Magnitude:** Liability: not a magnitude question  -  statutory bars are absolute for personal injury from negligence (UK UCTA s2(1)/CRA s65) and for contractual exclusion toward injured persons (EU PLD Art 15); GDPR Art 83(5) exposure up to EUR 20 million or 4% of turnover; EU PLD FOSS exclusion applies only while non-commercial. Epistemic: SAMSON nocebo ratio 0.90 (placebo 15.4 vs statin 16.3 vs nothing 8.0 on 0-100 scale; n=60/49 completers); Cochrane […]

**Safety caveats:** Populations an add-only engine can injure with the README's own pairs: undiagnosed/diagnosed hereditary haemochromatosis and other iron overload (vitamin C + iron pairing, iron-fortified foods); kidney-stone formers (vitamin C ≥1 g/day, and pairing with high-oxalate greens); anyone on CYP3A4/P-gp substrates  -  epilepsy (phenytoin, carbamazepine), transplant (ciclosporin, tacrolimus), HIV (nevirapine), cardiac (digoxin, some DOACs/statins/calcium-channel blockers), asthma (theophylline), beta-blockers  -  from black pepper at culinary doses; HLA-B*35:01 carriers and anyone on hepatotoxic drugs or with liver disease (turmeric+piperine, cassia coumarin); users on anticoagulants (turmeric/curcumin, vitamin K swings from added greens for VKA users); CKD/eGFR<60 (magnesium supplements, […]

**What this means for the engine:** (1) Decide the intended purpose explicitly and write it down; the README currently straddles wellness and medical purposes, which is the worst position. Route A (general wellness): no disease names, no diagnostic thresholds ("high fasting insulin"), no treatment guidance tied to lab values, no medication-interaction management; outputs phrased as […]

**Sources:**
- [FDA - Clinical Decision Support Software: Guidance for Industry and FDA Staff (final, issued 29 Jan […]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software)
- [FDA CDS guidance PDF (text parsed locally: Criteria 1-4; 'recommendations to patients or caregivers […]](https://www.fda.gov/media/109618/download)
- [FDA - General Wellness: Policy for Low Risk Devices (final, issued 6 Jan 2026)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices)
- [FDA General Wellness guidance PDF (text parsed locally: disqualifiers incl. diagnostic thresholds, […]](https://www.fda.gov/media/90652/download)
- [Directive (EU) 2024/2853 on liability for defective products (software/AI as product; FOSS […]](https://eur-lex.europa.eu/eli/dir/2024/2853/oj)
- [Regulation (EU) 2017/745 (MDR) - Art 2(1) medical device definition; Recital 19 […]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0745)