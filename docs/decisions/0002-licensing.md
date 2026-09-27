# ADR-0002: License code under Apache-2.0 and the knowledge base under CC BY 4.0

- **Status:** Accepted
- **Date:** 2026-09-27
- **Deciders:** founder
- **Related:** [LICENSE](../../LICENSE), [knowledge/LICENSE](../../knowledge/LICENSE), [data sources](../architecture/data-sources.md)

## Context

The original README aims to let "the broader society outside of research" build on open data. That needs a licence that allows reuse. The project has two kinds of work: software, and a curated knowledge base of evidence-graded rules. The research found that several data sources named in the README cannot be redistributed. KEGG requires a commercial licence for non-academic use. HMDB and FooDB are listed as non-commercial (CC BY-NC 4.0). See [claim C24](../research/claim-verification.md).

## Decision

- Everything outside `knowledge/`, including code and documentation, is licensed under the Apache License 2.0.
- Everything inside `knowledge/` is licensed under Creative Commons Attribution 4.0 International.
- Contributions are licensed inbound on the same terms as the directory they land in. There is no separate contributor agreement.
- Data from sources that forbid redistribution is never committed. Such sources can only be loaded locally by the user. See [ADR-0004](0004-knowledge-graph-first.md) and the [licence manifest](../../knowledge/sources/license-manifest.yaml).

## Consequences

- Anyone may reuse the code and the rule table, including commercially, with attribution.
- Apache-2.0 includes an explicit patent grant and matches ArcadeDB's licence.
- The knowledge graph needs licence tiers so non-redistributable data never leaks into anything the project publishes.
- A future hosted or commercial fork is allowed. Such a fork would carry its own regulatory and liability duties. See [ADR-0003](0003-open-source-self-hosted.md).

## Alternatives considered

- **MIT with CC BY 4.0.** Simpler and matches Grocy, but has no explicit patent grant.
- **AGPL-3.0 with CC BY-SA 4.0.** Keeps hosted forks open, but deters reuse by the research and clinical tools the project hopes to feed.
- **No licence yet.** Blocks all reuse and all outside contributions.
