# ADR-0003: Build an open-source, self-hosted, local-first tool

- **Status:** Accepted
- **Date:** 2026-09-27
- **Deciders:** founder
- **Related:** [SAFETY.md](../../SAFETY.md), [SECURITY.md](../../SECURITY.md), [open questions](../open-questions.md)

## Context

Who the software is for decides its legal, privacy and safety obligations. The research regulatory review found three relevant points. See the [regulatory analyst's report](../research/expert-panel.md).

- The EU Product Liability Directive 2024/2853 excludes free and open-source software supplied outside a commercial activity. That exclusion is lost if the software is sold, hosted as a service or exchanged for personal data.
- Regulators classify software by its intended purpose and the act of supply, not by its licence.
- Functions that map a person's lab values to interventions, or check their medicines for interactions, are what make health software a medical device in the US, EU and Australia.

Grocy itself is self-hosted, and its users already run their own servers.

## Decision

- The project publishes open-source software that people run themselves, next to their own Grocy instance.
- The project does not operate a hosted service, sell access, or collect user data.
- Health, profile and inventory data stay on the user's machine. The software sends no telemetry. The only outbound calls are explicit lookups, such as a barcode sent to a public food database, and each can be disabled.
- The intended purpose is general wellness, as stated in [SAFETY.md](../../SAFETY.md).

## Consequences

- No accounts, servers, or central database of user health data to secure.
- Pooled learning across users is not possible without a separate, opt-in design. That is [open question Q-12](../open-questions.md).
- Staying non-commercial keeps the EU open-source liability exclusion. Sponsorship tied to hosting or data would put it at risk.
- Distribution happens through self-hosting channels, such as a Home Assistant add-on or container image.
- Anyone may still fork and host it under [ADR-0002](0002-licensing.md). They take on the duties that come with that.

## Alternatives considered

- **Personal tool only.** Lighter, but conflicts with the goal of letting others build on it.
- **Hosted product.** Brings medical-device classification, data protection and product-liability work forward before anything has been shown to work.
