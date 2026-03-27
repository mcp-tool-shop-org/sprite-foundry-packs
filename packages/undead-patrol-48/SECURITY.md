# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | Yes       |

## Reporting a Vulnerability

Email: **64996768+mcp-tool-shop@users.noreply.github.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Version affected
- Potential impact

### Response timeline

| Action | Target |
|--------|--------|
| Acknowledge report | 48 hours |
| Assess severity | 7 days |
| Release fix | 30 days |

## Scope

This package is a **static asset pack** containing only PNG images and JSON metadata files.

- **Data touched:** PNG sprite files and JSON manifests (read-only by consumers)
- **No executable code** — no scripts, no binaries, no install hooks
- **No network egress** — assets are consumed entirely offline
- **No secrets handling** — does not read, store, or transmit credentials
- **No telemetry** is collected or sent
- **No file system writes** — consumers read assets from node_modules
