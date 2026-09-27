# Glossary

This page explains the abbreviations and project terms used across the documentation. Each entry gives the expansion for an abbreviation, a short definition and a link to the page that uses the term most. Definitions follow the project documents. Where a term is a project design choice, the linked page is the source of truth.

To add a term, follow the writing style in [CONTRIBUTING.md](../CONTRIBUTING.md).

[A](#a) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u)

## A

**ABAB.** A self-experiment schedule that runs blocks in the order A, B, A, B, where A and B are the two conditions being compared. It is one of the two randomised schedules in the M5 protocol. See [measurement and validation](science/measurement.md#the-self-experiment-protocol-milestone-m5).

**Adaptation.** The changes that training is meant to cause, such as more muscle, stronger tendons and more mitochondria. It is one half of recovery, and a rule goal (`adaptation`) for keeping long-term training gains. See [recovery nutrition](science/recovery-nutrition.md#what-recovery-means).

**ADR** (architecture decision record). A short numbered document that records one significant decision, its context, its consequences and the alternatives considered. Each starts as Proposed and becomes Accepted when the founder approves it. See [decision records](decisions/README.md).

**API** (application programming interface). The interface a program uses to talk to another program. The engine reads Grocy through Grocy's API with a key for a dedicated user. See [Grocy integration](architecture/grocy-integration.md).

**ASI** (Anabolic Synergy Index). The original README's name for the solver that scored paths through the graph and turned the best paths into suggestions. Under the proposed ADR-0007 it would become a ranking function over rules that pass their gates. Its exact form and name are still open: see [Q-01](open-questions.md), [Q-02](open-questions.md) and [Q-34](open-questions.md), and [ADR-0007](decisions/0007-graph-proposes-rules-decide.md).

## C

**CC BY 4.0** (Creative Commons Attribution 4.0). The licence for everything in `knowledge/`. It allows reuse, including commercial reuse, with credit. See [ADR-0002](decisions/0002-licensing.md).

**CC0** (Creative Commons Zero). A public domain dedication. USDA FoodData Central and the NIH Dietary Supplement Label Database are listed under it. See [data sources](architecture/data-sources.md).

**CGM** (continuous glucose monitor). A wearable sensor that reads glucose every few minutes. It is the densest signal for the glucose variant of the self-experiment protocol. See [measurement and validation](science/measurement.md).

**ChEBI** (Chemical Entities of Biological Interest). An open database of compounds, compound classes and roles, published as an ontology under CC BY 4.0. It is a core source for `Compound` nodes in the graph. See [knowledge graph](architecture/knowledge-graph.md).

**CI** (continuous integration). Automated checks that run on every pull request. They validate knowledge files against their schemas and lint the Markdown. See [evidence policy](science/evidence-policy.md#review-process).

**CJEU** (Court of Justice of the European Union). The court whose 2017 judgment in case C-329/16 held that software using patient-specific data to detect drug interactions is a medical device for that function. See [safety model](science/safety-model.md#what-would-make-it-a-medical-device).

**CK** (creatine kinase). A blood enzyme that rises after hard or unaccustomed exercise. The project treats it as a poor recovery marker, because it reflects the workout, not the meal. See [measurement and validation](science/measurement.md#what-blood-can-and-cannot-do).

**Competency question** (CQ). A fixed question the knowledge graph must answer with a committed, tested query, numbered CQ-01 onwards. Milestone M1 is done when CQ-01 to CQ-10 pass. See [knowledge graph](architecture/knowledge-graph.md#competency-questions).

**CURIE** (compact URI, where URI means uniform resource identifier). A short prefixed identifier such as `CHEBI:29073` or `FOODON:03000221`. Rules use CURIE values for their subject and target where known. See [knowledge graph](architecture/knowledge-graph.md#node-types).

**CVI** (within-subject coefficient of variation). How much one person's result varies from test to test when nothing has changed. It feeds the reference change value formula. See [claim verification](research/claim-verification.md).

**CYP3A4** (cytochrome P450 3A4). An enzyme that handles many medicines. Piperine inhibits it, which is why `gate.cyp3a4_pgp_medicine` withholds pepper and grapefruit suggestions for people on affected medicines. See [safety model](science/safety-model.md#gate-catalogue).

## D

**Deferred.** See [licence tier](#l).

**Direction.** A rule field that says whether the subject `enhances`, `inhibits` or has `no_effect` on the target. See [rule model](architecture/rule-model.md#fields).

**DOI** (digital object identifier). A permanent identifier for a published article or dataset. Every rule source must carry a PMID, DOI or URL. See [rule model](architecture/rule-model.md#fields).

**DSLD** (Dietary Supplement Label Database). A National Institutes of Health (NIH) database of supplement labels. A declared supplement in the health profile may carry an optional DSLD identifier. See [health profile](science/health-profile.md#declared-supplements).

**DWPC** (degree-weighted path count). A path score from drug-repurposing work on the Hetionet graph that corrects for how connected each node is. It is one tested method for the degree bias that affects any path score in the graph. See [knowledge graph](architecture/knowledge-graph.md#scoring-over-paths) and the [gap memos](research/gap-memos.md).

## E

**EFSA** (European Food Safety Authority). One of two sources of tolerable upper intake levels the project could use. Which standard applies is open question Q-07. See [safety model](science/safety-model.md#per-kilogram-scaling-and-the-upper-limit-ledger).

**Entity resolution.** Matching each Grocy product to a food class in FoodOn, and where possible to a FoodData Central record, with a recorded method and confidence. It is part of milestone M3. See [Grocy integration](architecture/grocy-integration.md#entity-resolution).

**Evidence grade** (A to D). The strength of the evidence behind a rule. A means several concordant human randomised controlled trials or a meta-analysis at the recommended dose; B means at least one well-conducted controlled human study; C means a single small or unreplicated study, manufacturer-only or observational data; D means animal, cell or mechanism only and never produces a suggestion. The grade rates the evidence at the dose that was tested. Whether a rule needs a supplement dose is a separate firing condition (see Supplement dose only; proposed in [ADR-0010](decisions/0010-grade-evidence-at-tested-dose.md)). See [evidence policy](science/evidence-policy.md#evidence-grades).

**Excluded.** See [licence tier](#l).

**Exclusion filter.** The step that removes foods the user does not eat, from their diet pattern, restrictions, dislikes and other foods. It is not a gate, needs no reason and shows no message. See [safety model](science/safety-model.md#evaluation-order).

## F

**Fail closed.** How safety gates treat a missing answer. If the user has not answered a gate's question, the engine treats the answer as "yes" and withholds. See [safety model](science/safety-model.md#principles).

**FDC** (FoodData Central). The United States Department of Agriculture (USDA) food composition database, including branded foods with barcodes. It is public domain and a core source. See [Grocy integration](architecture/grocy-integration.md#entity-resolution).

**Flag.** A named yes, no or unknown answer in the health profile, such as `flag.kidney_disease`. Flags trigger gates. Recent-event flags also carry an expiry. See [health profile](science/health-profile.md#conditions).

**FODMAP** (fermentable carbohydrates). Short for fermentable oligosaccharides, disaccharides, monosaccharides and polyols. People with irritable bowel syndrome (IBS) or FODMAP sensitivity are covered by `gate.fermentable_fibre`. See [health profile](science/health-profile.md#conditions).

**FoodOn.** An open food ontology that gives food identity and hierarchy, under CC BY 4.0. Grocy products resolve to FoodOn classes, so a rule about citrus can match a lemon. See [Grocy integration](architecture/grocy-integration.md#entity-resolution).

## G

**G6PD** (glucose-6-phosphate dehydrogenase). An enzyme. People with G6PD deficiency are covered by `gate.g6pd`. The project brief notes the right gate is an enzyme assay, not a genotype. See [health profile](science/health-profile.md#conditions).

**Gate.** A check that runs before ranking and can withhold, swap, cap or annotate a suggestion based on the health profile. Gates are defined in `knowledge/gates/gates.yaml`. A gate is either a safety gate or a tolerance gate. See [safety model](science/safety-model.md).

**GDPR** (General Data Protection Regulation). The European Union data protection law. The research discussed how it applies to health data, including the exemption for purely personal use. See [expert panel](research/expert-panel.md).

**Goal.** What a rule serves, from a fixed list: `muscle_repair`, `glycogen_restoration`, `connective_tissue`, `adaptation`, `sleep`, `micronutrient_status`, `hydration`, `gut_comfort` and `general`. Recovery goals rank first. See [rule model](architecture/rule-model.md#goals).

**Grocy.** A self-hosted household inventory application. The engine reads stock, products, barcodes and quantity units from it, read-only. See [Grocy integration](architecture/grocy-integration.md).

**GTIN** (Global Trade Item Number). The number behind a product barcode. The engine looks it up in FoodData Central branded foods, then in Open Food Facts. See [Grocy integration](architecture/grocy-integration.md#entity-resolution).

## H

**HbA1c** (glycated haemoglobin). A blood status marker. It is one of the few markers the project expects can respond to a supplied nutrient over 8 to 16 weeks in people who start low. See [measurement and validation](science/measurement.md#what-blood-can-and-cannot-do).

**Health profile.** What the user tells the engine about themselves: body measurements, training, diet, allergies, intolerances, conditions, recent events, medicines, supplements, life stage and daily state. It shapes suggestions and is never treated. It stays on the user's machine and every field is optional. See [health profile](science/health-profile.md).

**HFE C282Y.** A variant of the HFE gene linked to hereditary haemochromatosis (iron overload). For people homozygous for it, vitamin C with iron is the wrong direction; `gate.iron_overload` covers them. See [project brief](vision/project-brief.md).

**HRV** (heart rate variability). A daily signal that tracks readiness as a slow trend. See [measurement and validation](science/measurement.md#signals-for-recovery).

**hs-CRP** (high-sensitivity C-reactive protein). A blood marker of inflammation. It rises after hard training, infection and poor sleep, so the project treats it as a poor recovery marker. See [measurement and validation](science/measurement.md#what-blood-can-and-cannot-do).

## I

**iAUC** (incremental area under the curve). The rise in a measure, such as blood glucose, above its starting level over a set time, often 2 hours after a meal. See [measurement and validation](science/measurement.md) and the [gap memos](research/gap-memos.md).

**ICC** (intraclass correlation). How consistent a measurement is when repeated in the same person. A low ICC for duplicate meals means one person's response to the same meal varies a lot. See [measurement and validation](science/measurement.md).

**Intended purpose.** The wording in [SAFETY.md](../SAFETY.md) that says what the tool is for and what it is not. Every feature must fit inside it. See [scope](product/scope.md#intended-purpose).

**ISSN** (International Society of Sports Nutrition). Publisher of the position stands the project cites on protein, nutrient timing and creatine. See [recovery nutrition](science/recovery-nutrition.md).

## K

**KG** (knowledge graph). The reference graph built in milestone M1 from open datasets, with provenance on every node and edge. It proposes candidate interactions for review; only curated rules produce suggestions. See [knowledge graph](architecture/knowledge-graph.md).

**Kitchen reachable.** A rule field (`dose.kitchen_reachable`) that says whether a normal meal can reach the effective dose. Reviewers check it against a realistic serving. See [rule model](architecture/rule-model.md#fields).

## L

**Ledger.** A running total that caps a suggested amount. The upper-limit ledger adds the suggested amount, declared supplements and earlier accepted suggestions for each nutrient, and compares the total with the tolerable upper intake level. The coumarin ledger does the same against the tolerable daily intake. See [safety model](science/safety-model.md#per-kilogram-scaling-and-the-upper-limit-ledger).

**Licence tier.** How a data source may be used, decided by its licence. **Core** sources are redistributable and form the graph. **Runtime lookup** sources are queried one item at a time and never bundled. **Local only** sources are not redistributable; a user may import them on their own machine and export tooling refuses them. **Deferred** sources are not needed until a later milestone. **Excluded** sources are not used. See [data sources](architecture/data-sources.md#tiers).

**Local-first.** The data stays on the user's machine. There is no telemetry, and the only outbound traffic is explicit, documented lookups. See [ADR-0003](decisions/0003-open-source-self-hosted.md).

**Local only.** See [licence tier](#l).

## M

**MDR** (Medical Device Regulation). European Union Regulation 2017/745. Software is a medical device under it when its maker intends it for purposes such as diagnosing or treating disease. See [safety model](science/safety-model.md#what-would-make-it-a-medical-device).

**Metabotype.** A group of people who share a pattern of how their gut microbes convert a compound, such as producers and non-producers of urolithin A. Microbiome-based suggestions are deferred. See [claim verification](research/claim-verification.md) and [scope](product/scope.md#deferred-with-the-reason).

**Milestone** (M0 to M5). A stage of the roadmap, done when its exit criteria pass rather than by a date. M0 is documentation and governance, M1 the reference knowledge graph, M2 curated rules and safety gates, M3 Grocy integration and entity resolution, M4 the suggestion engine v0, and M5 the self-experiment protocol. See [roadmap](product/roadmap.md).

**MPS** (muscle protein synthesis). The rate at which muscle builds new protein after eating and training. It is a functional marker, not muscle growth itself. See [recovery nutrition](science/recovery-nutrition.md#protein) and [claim verification](research/claim-verification.md).

## N

**n-of-1.** A randomised crossover trial in one person. The M5 self-experiment protocol follows this approach. See [measurement and validation](science/measurement.md#the-self-experiment-protocol-milestone-m5).

**no_effect rule.** A rule with direction `no_effect` and output class `none`, recording an interaction that was tested and refuted. It never produces a suggestion. It stops false warnings and stops the graph from proposing the pair again. See [evidence policy](science/evidence-policy.md#negative-results-are-first-class).

**Noise floor.** How much an outcome varies within one condition for one person. The smallest detectable effect follows from it. See [measurement and validation](science/measurement.md#the-self-experiment-protocol-milestone-m5).

**Non-heme iron.** Iron from plant foods, also called plant iron. Vitamin C in the same meal raises how much is absorbed, mainly for people with low iron stores. See [rule R-0001](../knowledge/rules/R-0001-vitamin-c-nonheme-iron.yaml) and the [evidence policy](science/evidence-policy.md#worked-examples).

## O

**OFF** (Open Food Facts). An open database of products by barcode under the Open Database Licence (ODbL), which is share-alike. It is a runtime lookup: the engine sends one barcode per request and never bundles the data. See [data sources](architecture/data-sources.md).

**OLS** (Ontology Lookup Service). A service from the European Bioinformatics Institute (EBI) for searching ontologies. It is a proposed optional fallback for entity resolution and counts as an external lookup. See [Grocy integration](architecture/grocy-integration.md#entity-resolution).

**Output class.** What kind of suggestion a rule produces: **add** a food, **move** it to another time, **swap** it for another, or **skip** it. `no_effect` rules use `none`. Skip applies to foods and self-selected supplements only, never to prescribed medicines. See [ADR-0005](decisions/0005-full-advice-with-safety-gates.md).

**OWL** (Web Ontology Language). A format for publishing ontologies. FoodOn and ChEBI are OWL ontologies, which the build converts to plain node and edge files. See [knowledge graph](architecture/knowledge-graph.md#build-pipeline).

## P

**P-gp** (P-glycoprotein). A transporter that moves many medicines out of cells. Piperine inhibits it, which is part of the basis for `gate.cyp3a4_pgp_medicine`. See [claim verification](research/claim-verification.md).

**PINP** (procollagen type I N-terminal propeptide). A blood marker of collagen synthesis. The gelatin and vitamin C studies behind rule R-0007 measured it. See [expert panel](research/expert-panel.md) and [recovery nutrition](science/recovery-nutrition.md#connective-tissue).

**PLD** (Product Liability Directive). European Union Directive 2024/2853, which treats software as a product. The research noted that its exclusion for free and open-source software applies only while the software is supplied outside commercial activity. See [critic summary](research/critic-summary.md).

**PMID** (PubMed identifier). The number that identifies an article in PubMed. Rules and documents cite sources by PMID where one exists. See [evidence policy](science/evidence-policy.md).

**Proposed.** A status for a decision or default that is not yet agreed. It links to the related open question or decision record. See [open questions](open-questions.md).

## R

**RCT** (randomised controlled trial). A study that assigns people to conditions at random. Several concordant RCTs are part of the bar for grade A. See [evidence policy](science/evidence-policy.md#evidence-grades).

**RCV** (reference change value). The smallest change between two results from one person that is unlikely to be noise. It combines within-subject biological variation with the analyser's own error. See [measurement and validation](science/measurement.md#why-one-persons-result-is-hard-to-read).

**RDF** (Resource Description Framework). A standard format for linked data. ArcadeDB, the graph store proposed in ADR-0006, has no RDF support, so RDF sources are converted to node and edge files. See [ADR-0006](decisions/0006-arcadedb-graph-store.md).

**Recent event.** A flag with a start date, such as a stomach upset, antibiotics or an injury. Its definition sets how many days it lasts, after which it stops shaping suggestions and stays in the user's history. See [health profile](science/health-profile.md#recent-events).

**Recovery.** As this project uses it: being ready for the next session and still adapting to training. It is not the same as feeling less sore. See [ADR-0009](decisions/0009-recovery-goal-and-health-profile.md) and [recovery nutrition](science/recovery-nutrition.md#what-recovery-means).

**Reference change value.** See [RCV](#r).

**RPE** (rating of perceived exertion). A 0 to 10 score of how hard a session felt. Multiplied by minutes, it is a training-load measure. See [measurement and validation](science/measurement.md#signals-for-recovery).

**Rule.** A curated, reviewed statement about how one food component changes the effect of another, or changes recovery from training. Each rule is one YAML file in `knowledge/rules/`. Only accepted rules can produce a suggestion. See [rule model](architecture/rule-model.md).

**Runtime lookup.** See [licence tier](#l).

## S

**Safety gate.** A gate that protects against harm. It withholds or caps, never swaps, and fails closed when its question is unanswered. See [safety model](science/safety-model.md#principles).

**Smallest detectable effect.** The smallest effect a self-experiment run could have seen, given the noise floor and the number of days per condition. See [measurement and validation](science/measurement.md#the-self-experiment-protocol-milestone-m5).

**SPARQL** (SPARQL Protocol and RDF Query Language). The standard query language for RDF data. ArcadeDB, the proposed graph store, does not support it; queries would use Cypher or SQL. See [ADR-0006](decisions/0006-arcadedb-graph-store.md).

**Supplement dose only.** A rule field (`dose.supplement_dose_only`) set when an effect has only been shown at supplement doses. Such a rule never fires from food, fires only when the supplement is in stock or declared, and never recommends buying anything. See [rule model](architecture/rule-model.md#supplement-rules).

## T

**TDI** (tolerable daily intake). The daily amount of a substance judged safe over a lifetime. For coumarin it is 0.1 mg per kg of body weight, which the coumarin ledger enforces. See [safety model](science/safety-model.md#per-kilogram-scaling-and-the-upper-limit-ledger).

**Tolerance gate.** A gate that protects comfort, such as lactose intolerance. It prefers a swap to a tolerated version, and only withholds when no swap exists or the rule says so. See [safety model](science/safety-model.md#principles).

**Training window.** A rule's optional `context.training_window`: `pre_training`, `post_training`, `rest_day` or `any`. It ties the rule to the user's session plan, and the rule fires only when the plan matches. See [rule model](architecture/rule-model.md#training-context).

## U

**UL** (tolerable upper intake level). The highest daily intake of a nutrient unlikely to cause harm, set by sex, age and life stage. `gate.upper_limit` caps suggestions against it through the upper-limit ledger. See [safety model](science/safety-model.md#per-kilogram-scaling-and-the-upper-limit-ledger).

**USDA** (United States Department of Agriculture). Publisher of FoodData Central and the nutrient retention factors, both core sources. See [data sources](architecture/data-sources.md).
