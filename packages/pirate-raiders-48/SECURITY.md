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

This is a **static asset package** — pre-rendered PNG sprite images distributed via npm.

- **Data touched:** local PNG files only (read by game engines at runtime)
- **No executable code** — package contains only images and JSON metadata
- **No network egress** — no API calls, no telemetry, no phone-home
- **No secrets handling** — does not read, store, or transmit credentials
- **No telemetry** is collected or sent
- **Manifest checksums** — every asset has a SHA-256 hash in manifest.json for integrity verification
