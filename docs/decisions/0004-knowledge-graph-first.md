# ADR-0004: Build the knowledge graph first, with competency questions as exit criteria

- **Status:** Accepted
- **Date:** 2026-09-27
- **Deciders:** founder
- **Related:** [roadmap](../product/roadmap.md), [knowledge graph design](../architecture/knowledge-graph.md), [open question Q-20](../open-questions.md)

## Context

The research offered three possible first slices:

1. **A three-week self-experiment** with a continuous glucose monitor and no product code. It would test whether a kitchen-scale change is detectable in one person at all. The research brief recommended this.
2. **A pairing suggester:** a curated rule table plus Grocy stock, producing one suggestion per meal.
3. **The knowledge graph:** import open food, compound and pathway data and explore it.

The founder chose the knowledge graph. It is the foundation the README describes, and every later feature reads from it.

The research flagged three risks for this path:

- It is the slowest route to anything a user sees.
- A large graph has no natural finish line and can absorb months of data engineering.
- Scores computed over graph paths tend to favour whatever nodes have the most connections, such as vitamin C or water, rather than what matters. See the [ML engineer's report](../research/expert-panel.md) and [gap memos](../research/gap-memos.md).

## Decision

Milestone 1 builds a reference knowledge graph of foods, compounds, nutrients and pathways from licence-clean open sources, with provenance on every node and edge.

The milestone is done when the graph answers a fixed list of **competency questions** with committed, tested queries. The list is in the [knowledge graph design](../architecture/knowledge-graph.md#competency-questions). New questions can be added by pull request. The milestone does not grow otherwise.

The graph is a reference and hypothesis layer. It does not produce user suggestions by itself. See [ADR-0007](0007-graph-proposes-rules-decide.md).

Sources that cannot be redistributed are supported only as optional local imports that the user runs. They are tagged so nothing derived from them is published. See [ADR-0002](0002-licensing.md).

## Consequences

- The first months are data engineering: identifier crosswalks, RDF-to-property-graph conversion, and provenance.
- The competency questions give the milestone a finish line and a test suite.
- Grocy integration and the rule layer start after milestone 1, or in parallel if contributors appear.
- The self-experiment needs no product code, so it can run in parallel at any time. The roadmap lists it as milestone 5, but nothing prevents starting it earlier.
- A time box for milestone 1 is not yet set. See open question Q-20.

## Alternatives considered

- **Self-experiment first.** Cheapest test of the core hypothesis. Recommended by the research, not chosen.
- **Pairing suggester first.** Fastest to user value, but builds the rule layer without the reference data it will later need.
