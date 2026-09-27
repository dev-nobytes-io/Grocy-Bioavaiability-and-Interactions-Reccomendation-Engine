# Security policy

## Supported versions

Nothing has been released yet. Once releases begin, only the latest release will receive security fixes.

## Reporting a vulnerability

Report vulnerabilities privately through [GitHub private vulnerability reporting](https://github.com/dev-nobytes-io/Grocy-Bioavaiability-and-Interactions-Reccomendation-Engine/security/advisories/new). Do not open a public issue.

Include what you found, how to reproduce it, and what an attacker could do with it. You will get an acknowledgement as soon as a maintainer sees the report. The project is maintained by volunteers, so response times are best effort.

Report harmful suggestions under [SAFETY.md](SAFETY.md) instead, unless the report contains personal health data. In that case use the private channel above.

## What counts

- Any way for health, profile or inventory data to leave the host.
- Leaks or misuse of the Grocy API key.
- Code execution, injection or path traversal in importers or the engine.
- A malicious or tampered data source that could change suggestions without review.
- Dependency vulnerabilities that are reachable in this project.

## Security design commitments

- **Local-first.** The engine runs on the user's own machine next to Grocy. Health and inventory data stay there. See [ADR-0003](docs/decisions/0003-open-source-self-hosted.md).
- **No telemetry.** The software does not phone home.
- **Least privilege for Grocy.** The engine needs to read stock and products. Writing back to Grocy is optional and off by default. Where your Grocy version supports per-user permissions, run the engine under a dedicated Grocy user.
- **Secrets stay out of the repository.** API keys come from environment variables or a local file excluded by `.gitignore`.
- **Pinned, checksummed sources.** Importers record the version, retrieval date and checksum of every dataset they load, so a changed source is detectable.
- **Outbound calls are explicit.** Barcode lookups against public food databases send only the barcode. Any outbound call is listed in the documentation and can be disabled.
