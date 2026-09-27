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

The five draft rules each show a different part of the model.

| Rule | Shows |
|---|---|
| [R-0001](rules/R-0001-vitamin-c-nonheme-iron.yaml) Vitamin C and plant iron | An **add** rule with counter-evidence and a whole-diet caveat |
| [R-0002](rules/R-0002-fat-carotenoids.yaml) Fat and carotenoids | A **swap** rule with a dose range |
| [R-0003](rules/R-0003-tea-iron-timing.yaml) Tea and iron timing | An **inhibits** rule that produces a **move** suggestion |
| [R-0004](rules/R-0004-piperine-curcumin.yaml) Piperine and curcumin | A **supplement-dose-only** rule with a manufacturer flag and drug-interaction gate |
| [R-0005](rules/R-0005-calcium-zinc-no-effect.yaml) Calcium and zinc | A **no_effect** rule that stops the engine inferring a refuted interaction |

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
