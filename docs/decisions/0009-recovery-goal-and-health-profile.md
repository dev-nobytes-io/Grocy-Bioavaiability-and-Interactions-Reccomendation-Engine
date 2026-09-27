# ADR-0009: Optimise recovery for people who train, informed by a full health profile

- **Status:** Accepted
- **Date:** 2026-09-27
- **Deciders:** founder
- **Related:** [scope](../product/scope.md), [health profile](../science/health-profile.md), [recovery nutrition](../science/recovery-nutrition.md), [SAFETY.md](../../SAFETY.md)

## Context

The research tested the original README's claims. Many of those claims were about disease markers, such as fasting insulin, inflammation and tissue damage. The research therefore spent much of its effort on disease and harm.

The founder's direction is different. The product is about **positive health**: helping people who train recover better through the best nutrition available to them. Disease and personal health information still matter a great deal. They are not the goal, but they decide what is safe, tolerable and useful for a given person.

## Decision

1. **The primary goal is recovery for people who train.** Recovery means being ready for the next session and continuing to adapt to training. It does not only mean feeling less sore. See [recovery nutrition](../science/recovery-nutrition.md).
2. **Every rule declares which goals it serves.** Recovery goals come first in ranking. Absorption rules, such as vitamin C with plant iron, serve recovery indirectly through nutrient status.
3. **The engine keeps a health profile** that the user fills in and controls. It covers:
   - body measurements: sex, age, height, weight, body fat and how it was measured;
   - training: type, frequency, experience, current phase, upcoming sessions and injuries;
   - diet pattern and restrictions;
   - allergies and intolerances;
   - long-term conditions;
   - recent events, such as illness, antibiotics, injury or surgery, each with an expiry;
   - medicines and declared supplements;
   - life stage, such as pregnancy or menstrual status.
4. **Health information shapes suggestions and is never treated.** It is used to withhold, adjust, swap or re-time suggestions, and to scale doses to the person. The engine never says "because you have condition X, eat Y to treat it".
5. **The profile stays on the user's machine** under [ADR-0003](0003-open-source-self-hosted.md). Every field is optional. Missing fields make the engine more cautious, not less.

## Consequences

- Rules need a `goals` field and an optional training-timing context. The rule schema and examples change.
- Body mass becomes a key input. Per-kilogram doses, such as protein per meal, and per-kilogram limits, such as the coumarin ceiling for cinnamon, depend on it.
- Intolerances produce **swap** suggestions where possible, such as a lactose-free alternative, rather than silence.
- Recent events need expiry dates, so a stomach bug last month does not shape advice today.
- The intended purpose in [SAFETY.md](../../SAFETY.md) now names recovery and the use of health information.
- Collecting conditions and medicines is sensitive. It is safe here because the data never leaves the user's machine and the engine never interprets it as a diagnosis. Any hosted version would need a new decision record.

## Alternatives considered

- **Disease-focused recommendations,** as much of the original README implied. Rejected by the founder. It is also the path that turns health software into a regulated medical device.
- **Ignoring health information** to keep the product purely positive. Rejected: it would give unsafe or intolerable advice to many people.
