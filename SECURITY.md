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

This repository contains **static image assets only** (PNG sprite sheets).

- **Data touched:** PNG image files read from disk at install time via npm
- **No executable code** — no install scripts, no postinstall hooks, no runtime code
- **No network egress** — assets are consumed locally by game engines
- **No secrets handling** — does not read, store, or transmit credentials
- **No telemetry** is collected or sent
