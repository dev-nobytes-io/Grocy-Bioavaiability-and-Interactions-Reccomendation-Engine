# ADR-0006: Use ArcadeDB as the graph store, with conditions

- **Status:** Proposed
- **Date:** 2026-09-27
- **Deciders:** pending founder approval
- **Related:** [knowledge graph design](../architecture/knowledge-graph.md), [ADR-0004](0004-knowledge-graph-first.md), [open question Q-21](../open-questions.md)

## Context

The original README chose ArcadeDB: a multi-model database with graph, document, key-value and vector support in one process, licensed under Apache-2.0. With the knowledge graph first ([ADR-0004](0004-knowledge-graph-first.md)), the store is needed now.

The research knowledge-graph engineer found ArcadeDB defensible but raised these points. See the [expert panel](../research/expert-panel.md).

- **No RDF or SPARQL support.** FoodOn, ChEBI and the README's cited MeNu GUIDE graph are published as RDF or OWL. They must be converted to a property graph first. That converter is real work, and ArcadeDB does not help with it.
- **Recent storage fixes.** Recent releases fixed data-loss and index bugs, including records larger than a page, concurrent edge appends, and vector-index entries left by rolled-back transactions. The latest release as of this record is 26.9.1, dated 3 September 2026 ([releases](https://github.com/ArcadeData/arcadedb/releases)).
- **Workload size.** The whole graph plus one household's data likely fits in memory. Postgres with the Apache AGE extension, or an RDF triple store, would also work.
- **Alternatives exist.** Every reference platform the product research looked at started on Postgres or SQLite.

## Decision (proposed)

Use ArcadeDB for the reference knowledge graph, on these conditions:

1. Pin a specific release no older than 26.9.1. Read the release notes for storage and index fixes before each upgrade.
2. Keep RDF and OWL conversion as a separate, reproducible pipeline step that writes plain node and edge files. The graph can then be rebuilt from those files in any store.
3. Do not use the vector index until a feature needs it. Free-text state input is deferred. See the [roadmap](../product/roadmap.md).
4. Before committing, run a two-day spike. Load a ChEBI subset and FoodOn into ArcadeDB, and answer three competency questions. Record load time, query time and lines of conversion code. If the spike fails, revisit this record.

## Consequences

- The graph can be rebuilt in another store from the intermediate files, so the choice is reversible.
- The project depends on a Java runtime on the user's machine.
- Cypher and SQL queries are available. SPARQL is not.

## Alternatives considered

- **Postgres with Apache AGE and pgvector.** Mature and familiar. Graph queries are less natural.
- **An RDF store such as Apache Jena Fuseki.** Loads the ontologies natively with SPARQL. Weaker for property-rich edges such as dose and effect size.
- **SQLite plus a rule table only.** Enough for a rule-first product, but does not fit the knowledge-graph-first decision.
