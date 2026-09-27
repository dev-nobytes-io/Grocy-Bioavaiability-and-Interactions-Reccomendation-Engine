# Rule model

A rule is a curated, reviewed statement about how one food component changes the effect of another. Rules are the only thing that can produce a suggestion ([ADR-0007](../decisions/0007-graph-proposes-rules-decide.md)). The machine-checked definition is [rule.schema.json](../../knowledge/schema/rule.schema.json). This page explains it.

## One rule, one file

Each rule lives in `knowledge/rules/R-NNNN-short-name.yaml`. IDs are never reused. A rule that turns out to be wrong is set to `deprecated`, not deleted, so the history stays visible.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | `R-` and four digits. |
| `title` | yes | One sentence stating the rule. |
| `status` | yes | `draft`, `in_review`, `accepted` or `deprecated`. Only `accepted` rules produce suggestions. |
| `version` | yes | Increases with every substantive change. |
| `direction` | yes | `enhances`, `inhibits` or `no_effect`. |
| `output_class` | yes | `add`, `move`, `swap`, `skip`, or `none`. `no_effect` rules must use `none`. See [ADR-0005](../decisions/0005-full-advice-with-safety-gates.md). |
| `subject` | yes | The component that acts, with CURIE identifiers where known. |
| `target` | yes | The component or outcome that changes. |
| `dose.effective` | yes | Minimum and optional maximum effective dose, unit, and whether per meal, day or dose. |
| `dose.kitchen_reachable` | yes | Whether a normal meal can reach the effective dose. |
| `dose.supplement_dose_only` | yes | True if the effect is only shown at supplement doses. Such rules never fire from food. |
| `timing.window` | yes | `same_meal`, `separate_by_hours`, `daily`, `chronic` or `not_applicable`. |
| `effect.summary` | yes | What happens, in plain words. |
| `effect.magnitude` | yes | The effect size, with the dose and baseline it was measured at. |
| `effect.outcome_type` | yes | What was measured: absorption by isotope, absorption in plasma, a status marker, a functional marker, a clinical outcome, performance, pharmacokinetics, or mechanism only. |
| `effect.whole_diet_note` | no | Whether a single-meal effect survives across a whole diet. |
| `conditions.applies_to` | yes | Who the evidence covers. |
| `conditions.weak_or_absent_in` | no | Who it does little for. |
| `gates` | yes | Safety gate IDs from [gates.yaml](../../knowledge/gates/gates.yaml). An empty list must be a deliberate choice. |
| `evidence.grade` | yes | A to D. See the [evidence policy](../science/evidence-policy.md). Accepted rules cannot be grade D. |
| `evidence.replicated` | yes | Whether an independent group has reproduced the main finding. |
| `evidence.sponsor_flag` | yes | `independent`, `manufacturer`, `mixed` or `unknown`. |
| `evidence.sources` | yes | At least one source with a PMID, DOI or URL, and the finding it supports. |
| `evidence.counter_evidence` | no | Sources that point the other way. Recording them is expected. |
| `suggestion.text` | yes | What the user sees. Positive, plain, no disease claims. |
| `suggestion.label` | no | A caveat that must be shown with the suggestion. |
| `reviewers`, `last_reviewed` | for accepted | Who reviewed it and when. |
| `changelog` | yes | Dated list of changes. |

## Rules the schema enforces

- A `no_effect` rule must have `output_class: none`, and the reverse.
- An `accepted` rule must list at least one reviewer, a review date, and a grade of A, B or C.
- Every source must carry a PMID, DOI or URL.
- Gate IDs must look like `gate.name`.

## Rules the reviewer enforces

The schema cannot check these. Reviewers do.

- Every number in `effect.magnitude` appears in a cited source.
- The dose is what the study used, not an extrapolation.
- `kitchen_reachable` is honest. Check the amount in a realistic serving.
- Every relevant gate is listed.
- `counter_evidence` includes any known null or contrary result.
- `suggestion.text` fits the intended purpose in [SAFETY.md](../../SAFETY.md).

## How the engine uses a rule

1. **Match.** The rule's subject and target are both present in the planned meal, or the subject can be added from stock. Food classes match through the ontology, so a rule about citrus matches a lemon.
2. **Gate.** If any listed gate applies to the user, or its answer is unknown, the rule is dropped. See the [safety model](../science/safety-model.md).
3. **Dose.** If `supplement_dose_only` is true, or stock cannot reach the effective dose, the rule is dropped.
4. **Rank.** Remaining rules are ordered. The ranking function is not yet decided. See [open questions Q-01 and Q-02](../open-questions.md).
5. **Explain.** The top rule is shown with its `suggestion.text`, `label`, dose, grade and first source.

`no_effect` rules are never shown. They stop the graph from nominating an interaction that has already been tested and refuted.
