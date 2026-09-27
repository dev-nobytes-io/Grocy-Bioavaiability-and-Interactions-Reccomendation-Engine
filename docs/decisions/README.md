# Decision records

Significant decisions are recorded here as architecture decision records (ADRs). [GOVERNANCE.md](../../GOVERNANCE.md) defines what counts as significant.

## Process

1. Copy [template.md](template.md) to `NNNN-short-title.md` using the next free number.
2. Set the status to **Proposed** and open a pull request.
3. The founder approves or rejects. Accepted records are not edited except to mark them superseded.
4. To reverse a decision, write a new record that supersedes the old one.

## Index

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-record-decisions.md) | Record significant decisions as ADRs | Accepted |
| [0002](0002-licensing.md) | License code under Apache-2.0 and the knowledge base under CC BY 4.0 | Accepted |
| [0003](0003-open-source-self-hosted.md) | Build an open-source, self-hosted, local-first tool | Accepted |
| [0004](0004-knowledge-graph-first.md) | Build the knowledge graph first, with competency questions as exit criteria | Accepted |
| [0005](0005-full-advice-with-safety-gates.md) | Allow full advice, including removals, behind safety gates | Accepted |
| [0006](0006-arcadedb-graph-store.md) | Use ArcadeDB as the graph store, with conditions | Proposed |
| [0007](0007-graph-proposes-rules-decide.md) | Only curated rules produce suggestions; the graph proposes | Proposed |
| [0008](0008-python-for-pipelines.md) | Use Python for importers, pipelines and analysis | Proposed |
| [0009](0009-recovery-goal-and-health-profile.md) | Optimise recovery for people who train, informed by a full health profile | Accepted |
