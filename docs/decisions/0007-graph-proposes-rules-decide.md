# ADR-0007: Only curated rules produce suggestions; the graph proposes

- **Status:** Proposed
- **Date:** 2026-09-27
- **Deciders:** pending founder approval
- **Related:** [rule model](../architecture/rule-model.md), [evidence policy](../science/evidence-policy.md), [open questions Q-01, Q-02, Q-11](../open-questions.md)

## Context

The README's Anabolic Synergy Index scores paths through the graph and turns the best-scoring paths into suggestions. The research found three problems with letting graph paths drive advice directly:

- **Degree bias.** Unnormalised path scores rank nodes by how many connections they have. Highly connected compounds win regardless of relevance. This is shown mathematically and in audits of biomedical graphs. See the [gap memos](../research/gap-memos.md).
- **Source bias.** The authors of MeNu GUIDE, the README's only citation, report that their graph is biased toward specific foods and conditions ([preprint](https://www.biorxiv.org/content/10.1101/2024.10.12.618040v1)).
- **Mechanism is not effect.** A path from a food to a pathway says nothing about dose, size of effect, or who it applies to. Several README examples are real mechanisms with no effect at kitchen doses. See [claims C3 and C4](../research/claim-verification.md).

## Decision (proposed)

- The knowledge graph generates **candidates and explanations**. It never produces a user-facing suggestion on its own.
- A user-facing suggestion comes only from a **curated rule**: a reviewed file in `knowledge/rules/` with a dose, a population, an evidence grade, sources and safety gates.
- Graph paths can nominate new rules for human review. They carry a clear "hypothesis" label wherever they are shown.
- Any score over graph paths must be normalised and compared against a degree-preserving random baseline before it is used, even for nominating hypotheses.

## Consequences

- The number of possible suggestions is limited by how many rules have been reviewed. The research estimated that roughly 20 to 25 rules can be built on published human dose-response equations today.
- The Anabolic Synergy Index becomes a ranking function over rules that pass their gates. Its exact form is still open. See [Q-01 and Q-02](../open-questions.md).
- Review effort, not graph size, becomes the bottleneck. That is intended.

## Alternatives considered

- **Graph paths drive suggestions directly,** as in the README. Rejected for the reasons above.
- **No graph at all, rules only.** Simpler, but conflicts with [ADR-0004](0004-knowledge-graph-first.md) and loses a useful way to find new rules.
