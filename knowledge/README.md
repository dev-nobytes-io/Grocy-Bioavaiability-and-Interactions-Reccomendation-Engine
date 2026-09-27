# Knowledge base

This directory holds the curated knowledge the engine is allowed to act on. It is licensed under [CC BY 4.0](LICENSE), separately from the code. See [ADR-0002](../docs/decisions/0002-licensing.md).

> **Status: draft.** Every rule and gate here is an unreviewed example. Nothing in this directory may be used to produce suggestions until a reviewer has accepted it under the [evidence policy](../docs/science/evidence-policy.md).

## Layout

| Path | Contents | Schema |
|---|---|---|
| `rules/` | One YAML file per curated interaction rule | [rule.schema.json](schema/rule.schema.json) |
| `gates/gates.yaml` | Safety gates and the health questions that trigger them | [gates.schema.json](schema/gates.schema.json) |
| `sources/license-manifest.yaml` | Every external dataset, its licence and its tier | [sources.schema.json](schema/sources.schema.json) |
| `schema/` | JSON Schemas for all of the above | |

## The example rules

The eleven draft rules each show a different part of the model. R-0006 to R-0011 serve recovery from training. See [recovery nutrition](../docs/science/recovery-nutrition.md).

| Rule | Shows |
|---|---|
| [R-0001](rules/R-0001-vitamin-c-nonheme-iron.yaml) Vitamin C and plant iron | An **add** rule with counter-evidence and a whole-diet caveat |
| [R-0002](rules/R-0002-fat-carotenoids.yaml) Fat and carotenoids | A **swap** rule with a dose range |
| [R-0003](rules/R-0003-tea-iron-timing.yaml) Tea and iron timing | An **inhibits** rule that produces a **move** suggestion |
| [R-0004](rules/R-0004-piperine-curcumin.yaml) Piperine and curcumin | A **supplement-dose-only** rule with a manufacturer flag and drug-interaction gate |
| [R-0005](rules/R-0005-calcium-zinc-no-effect.yaml) Calcium and zinc | A **no_effect** rule that stops the engine inferring a refuted interaction |
| [R-0006](rules/R-0006-post-training-protein-dose.yaml) Protein after training | An **add** rule with a per-kilogram dose and a **post_training** window |
| [R-0007](rules/R-0007-gelatin-vitamin-c-pre-training.yaml) Gelatin and vitamin C before loading | A grade C **pre_training** rule with more counter-evidence than support |
| [R-0008](rules/R-0008-antioxidant-supplements-adaptation.yaml) Vitamin C and E supplements | A **skip** rule for a declared supplement that protects training adaptation |
| [R-0009](rules/R-0009-carbohydrate-protein-no-effect.yaml) Carbohydrate with protein | A **no_effect** rule that replaces the "anabolic waste" idea |
| [R-0010](rules/R-0010-alcohol-after-training.yaml) Alcohol after training | A grade C **skip** rule tested only at a very large dose |
| [R-0011](rules/R-0011-creatine-monohydrate.yaml) Creatine monohydrate | A **supplement-dose-only** rule that fires only when the supplement is in stock |

## Validate

```sh
pip install check-jsonschema
check-jsonschema --schemafile knowledge/schema/rule.schema.json knowledge/rules/*.yaml
check-jsonschema --schemafile knowledge/schema/gates.schema.json knowledge/gates/gates.yaml
check-jsonschema --schemafile knowledge/schema/sources.schema.json knowledge/sources/license-manifest.yaml
```

Continuous integration runs the same checks on every pull request.

## Adding or changing a rule

See [CONTRIBUTING.md](../CONTRIBUTING.md#proposing-a-rule). The field-by-field guide is the [rule model](../docs/architecture/rule-model.md).

## Attribution

When you reuse this knowledge base, credit "Grocy Bioavailability and Interactions Recommendation Engine contributors" and link to this repository. Cite the primary sources listed in each rule as well.
