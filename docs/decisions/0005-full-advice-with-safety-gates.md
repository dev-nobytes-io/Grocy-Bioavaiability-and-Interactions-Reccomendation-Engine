# ADR-0005: Allow full advice, including removals, behind safety gates

- **Status:** Accepted
- **Date:** 2026-09-27
- **Deciders:** founder
- **Related:** [product principles](../product/principles.md), [safety model](../science/safety-model.md), [SAFETY.md](../../SAFETY.md)

## Context

The original README framed the engine as purely additive: "not a food cop", only ever suggesting what to add. The research found two problems with that. See [claim C21](../research/claim-verification.md) and the critic's [consensus points](../research/critic-summary.md).

- **Additive framing is not a safety property.** Every example pairing in the README has a group it can harm. Vitamin C with iron is the wrong direction for people with iron overload. Black pepper at culinary amounts raises blood levels of some anti-epileptic and HIV drugs. Leafy greens destabilise warfarin.
- **The strongest levers are not additions.** For plant iron, drinking tea one hour after the meal instead of with it restored absorption to the level of a water control in a crossover study (Ahmad Fuzi 2017, n=12, [doi:10.3945/ajcn.117.161364](https://doi.org/10.3945/ajcn.117.161364)). An add-only engine cannot say that.

## Decision

The engine may produce four classes of suggestion:

| Class | Example |
|---|---|
| **add** | Add a vitamin C source to this lentil meal. |
| **move** | Have your tea an hour after this meal rather than with it. |
| **swap** | Use full-fat dressing instead of fat-free on this salad. |
| **skip** | Leave out the extra cassia cinnamon today; your declared intake is near the coumarin limit. |

Tone rules keep the original spirit:

- Lead with an addition when one exists.
- Give the reason and the evidence for every suggestion.
- Never moralise, shame or use words like "bad" or "cheat".

Safety gates run before any of this. A gated suggestion is withheld, not rephrased. See the [safety model](../science/safety-model.md).

## Consequences

- The rule schema needs a direction field (`enhances`, `inhibits`, `no_effect`) and an output class.
- Inhibition rules and timing rules become first-class, which is where much of the best evidence is.
- The product can no longer be described as "additive only". The positive tone becomes a writing rule rather than a constraint on content.
- "Skip" suggestions about prescribed medicines are out of scope under [SAFETY.md](../../SAFETY.md). Skip applies to foods and self-selected supplements only.

## Alternatives considered

- **Strictly additive.** Keeps the philosophy pure, but cannot express the strongest evidence and still harms gated groups.
- **Additive interface with silent vetoes underneath.** Recommended by the research. Safer than strictly additive, but still cannot give timing advice.
