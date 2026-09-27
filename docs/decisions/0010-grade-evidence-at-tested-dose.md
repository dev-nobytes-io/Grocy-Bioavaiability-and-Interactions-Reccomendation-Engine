# ADR-0010: Grade evidence at the tested dose, and treat supplement-dose-only as a firing condition

- **Status:** Proposed
- **Date:** 2026-09-27
- **Deciders:** pending founder approval
- **Related:** [evidence policy](../science/evidence-policy.md), [rule model](../architecture/rule-model.md), [open question Q-11](../open-questions.md), [ADR-0009](0009-recovery-goal-and-health-profile.md)

## Context

The first draft of the [evidence policy](../science/evidence-policy.md) did two jobs with one grade. The grade rated how strong the evidence was. It also capped any finding shown only at supplement doses at grade C, because a meal cannot reach that dose.

The recovery rules added under [ADR-0009](0009-recovery-goal-and-health-profile.md) exposed the problem. Two draft rules are about a supplement the user already has, at the dose the trials tested:

- [R-0011](../../knowledge/rules/R-0011-creatine-monohydrate.yaml), creatine at 3 to 5 g a day, rests on a meta-analysis of 100 placebo-controlled studies.
- [R-0008](../../knowledge/rules/R-0008-antioxidant-supplements-adaptation.yaml), skipping high-dose vitamin C and E during a training block, rests on two randomised controlled trials and a third controlled trial, from two independent groups.

Under the cap, both would be grade C, the same as one small unreplicated study. That hides a real difference in evidence strength. The cap was there to stop supplement-dose evidence being passed off as food advice. The `dose.supplement_dose_only` field already does that job: such a rule never fires from food.

Under [GOVERNANCE.md](../../GOVERNANCE.md), a change to the evidence policy needs a decision record.

## Decision

- `evidence.grade` rates how strong the evidence is at the dose the studies tested. It does not depend on whether food can reach that dose.
- `dose.supplement_dose_only` is a firing condition, not a grade. When it is true, the rule never fires from food. It fires only when that supplement is in the user's Grocy stock or declared in the health profile. It never suggests buying anything, and it carries a visible supplement-dose label.
- The grade C definition no longer lists "a supplement-dose-only finding".
- A grade C supplement rule follows the same opt-in and label rule as any other grade C rule. Which grades may produce suggestions stays open under [Q-11](../open-questions.md).

## Consequences

- R-0008 and R-0011 can stay at grade B. [R-0004](../../knowledge/rules/R-0004-piperine-curcumin.yaml), piperine with curcumin, stays at grade C because of its evidence: one small, manufacturer-linked study, contradicted by an independent crossover.
- Reviewers grade every rule by the same steps, then decide the supplement flag separately.
- The evidence policy, the rule model, the rule schema and the recovery nutrition page describe the grade this way. They mark it **Proposed** until this record is accepted.
- A user who has a supplement in stock may see a grade B suggestion about it. The label, `gate.pregnancy` and the upper-limit ledger still apply.

## Alternatives considered

- **Keep the cap at grade C for every supplement-dose-only rule.** Simple, but it rates a large meta-analysis the same as one small study and hides that difference from the user.
- **Apply the cap only when supplement-dose evidence supports a food suggestion.** This was an earlier working proposal. It is redundant, because a supplement-dose-only rule never fires from food at all.
