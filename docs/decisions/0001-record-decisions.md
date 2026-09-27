# ADR-0001: Record significant decisions as ADRs

- **Status:** Accepted
- **Date:** 2026-09-27
- **Deciders:** founder
- **Related:** [GOVERNANCE.md](../../GOVERNANCE.md)

## Context

The project starts with one maintainer and a large research record. Decisions made in chat or in someone's head get lost, and later contributors cannot tell whether a choice was deliberate. Health-adjacent software also needs an audit trail for why a safety-relevant choice was made.

## Decision

Record every significant decision as a short Markdown file in `docs/decisions/`, numbered in order, using [the template](template.md). Governance defines which decisions are significant.

## Consequences

- Contributors can see why things are the way they are.
- Reversing a decision means writing a new record, which forces the reason to be stated.
- There is a small writing cost for each significant change.

## Alternatives considered

- **Issues only.** Searchable, but scattered and easy to lose when closed.
- **A wiki.** Not versioned with the code and not reviewed in pull requests.
