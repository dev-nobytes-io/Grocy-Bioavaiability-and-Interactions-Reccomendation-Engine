# ADR-0008: Use Python for importers, pipelines and analysis

- **Status:** Proposed
- **Date:** 2026-09-27
- **Deciders:** pending founder approval
- **Related:** [ADR-0004](0004-knowledge-graph-first.md), [ADR-0006](0006-arcadedb-graph-store.md)

## Context

Milestone 1 is data engineering. It parses RDF and OWL, reads CSV and JSON datasets, builds identifier crosswalks and loads a graph. Later milestones add statistical analysis for self-experiments. The language must suit all of that and be approachable for contributors from science backgrounds.

## Decision (proposed)

Use Python 3.12 or later for importers, the build pipeline, the rule validator and analysis code.

- Use `rdflib` or `owlready2` for RDF and OWL parsing, or the ROBOT command-line tool where it is simpler.
- Talk to ArcadeDB over its HTTP API or PostgreSQL wire protocol.
- Use `ruff` for linting and formatting, and `pytest` for tests.
- Manage dependencies with `uv` and a `pyproject.toml`.

The engine's user interface is not decided by this record.

## Consequences

- Scientists and data engineers can contribute without learning a new language.
- Mature libraries exist for every data format the sources use.
- A second language may be needed later for a user interface or a Home Assistant add-on.

## Alternatives considered

- **Java or Kotlin.** Same runtime as ArcadeDB, but weaker for scientific analysis and fewer likely contributors.
- **TypeScript.** Good for a user interface, weaker for RDF and statistics.
