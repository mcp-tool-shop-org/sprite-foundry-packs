# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | Yes       |

## Threat Model

This package contains **only static PNG images and JSON metadata**.

- **No executable code** — no JavaScript, no binaries, no WebAssembly
- **No install hooks** — no preinstall, postinstall, or lifecycle scripts
- **No network access** — no fetch, no telemetry, no analytics
- **No file system writes** — assets are read-only by design
- **No dependencies** — zero runtime dependencies

The attack surface is limited to:
- Malformed PNG files (mitigated by standard image decoders in all engines)
- Malformed JSON metadata (mitigated by standard JSON parsers)

## Reporting a Vulnerability

If you discover a security issue, please email:

**64996768+mcp-tool-shop@users.noreply.github.com**

You will receive a response within 48 hours. Please do not open a public issue for security vulnerabilities.

## Response Timeline

- **Acknowledgment:** within 48 hours
- **Assessment:** within 7 days
- **Fix (if applicable):** within 30 days
