# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions will follow [Semantic Versioning](https://semver.org/) once code is released.

## [Unreleased]

### Added

- Research record: a reviewed project brief, verification of 28 README claims, twelve discipline reports, a critic summary and eight gap memos.
- Governance: licence split (Apache-2.0 for code and docs, CC BY 4.0 for `knowledge/`), governance model, contribution guide, code of conduct, security policy and safety policy.
- Decision records ADR-0001 to ADR-0010. ADR-0006, ADR-0007, ADR-0008 and ADR-0010 are Proposed.
- ADR-0009: recovery for people who train is the primary goal, and a user-controlled health profile shapes suggestions without ever being treated.
- ADR-0010 (Proposed): the evidence grade rates the evidence at the tested dose, and supplement-dose-only is a separate firing condition.
- Product and architecture documentation for the knowledge-graph-first roadmap.
- Science documentation: evidence policy, health profile, safety model, recovery nutrition, and measurement and validation.
- Knowledge base scaffolding: rule, gate and source schemas, a safety gate catalogue, a data-source licence manifest and draft example rules R-0001 to R-0005.
- Health profile schema and an example profile for an invented person.
- Rule schema: a required `goals` field with nine fixed goals, an optional training `context`, and per-kilogram doses.
- Six draft recovery rules, R-0006 to R-0011, for eleven draft rules in total.
- Safety gates version 2: flag categories, safety and tolerance severity, swap actions for tolerance gates, recent-event flags with expiry, and new gates for lactose intolerance, coeliac disease and recent gastrointestinal illness. The catalogue holds 17 gates and 20 flags.
- Gate `scope`: a gate with global scope applies to every rule, whether or not the rule lists it. `gate.inborn_error`, `gate.upper_limit`, `gate.allergy` and `gate.coeliac_gluten` use it.
- Grocy integration design.
- Tracked open questions Q-01 to Q-35, each with a priority and what it blocks.
- Mermaid diagrams across governance, product, architecture and science documents.
- A documentation index and a glossary.
- Checks: a link checker (`scripts/check_links.py`), a Mermaid validator (`scripts/check_mermaid.py`), a markdownlint configuration, and a continuous integration workflow (`.github/workflows/checks.yml`) that runs them with knowledge schema validation.

### Changed

- The original README is preserved at `docs/vision/original-readme.md`. The new README is a project entry point.
- The "liability: there is none" statement is replaced by an intended-purpose statement and safety commitments in `SAFETY.md`.
- The intended purpose in `SAFETY.md` now names recovery from training and the use of health information (ADR-0009).
- Product principles, scope and roadmap are rewritten around recovery.
- Draft rules after review: corrected citations in R-0001, R-0003 and R-0006; R-0005 regraded from B to C; added gates to R-0002, R-0006, R-0007 and R-0010; revised suggestion text in R-0004, R-0007, R-0008, R-0010 and R-0011.
- Safety gates after review: the allergy gate withholds products of unknown allergen content, the medicines gate covers black pepper at any amount, the pregnancy gate covers suggestions that mention alcohol, and the lactose question separates intolerance from milk allergy. The schema now requires flag-triggered safety gates to withhold.
