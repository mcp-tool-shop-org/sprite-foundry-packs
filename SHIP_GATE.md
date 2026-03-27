# Ship Gate

> No repo is "done" until every applicable line is checked.

**Tags:** `[all]` every repo · `[npm]` published artifacts
**Detected:** `[all]` `[npm]`

---

## A. Security Baseline

- [x] `[all]` SECURITY.md exists (report email, supported versions, response timeline) (2026-03-27)
- [x] `[all]` README includes threat model paragraph (data touched, data NOT touched, permissions required) (2026-03-27)
- [x] `[all]` No secrets, tokens, or credentials in source or diagnostics output (2026-03-27)
- [x] `[all]` No telemetry by default — state it explicitly even if obvious (2026-03-27)

### Default safety posture

- [ ] `[cli|mcp|desktop]` SKIP: static asset packs — no CLI, MCP, or desktop components
- [ ] `[cli|mcp|desktop]` SKIP: static asset packs — no file operations
- [ ] `[mcp]` SKIP: not an MCP server
- [ ] `[mcp]` SKIP: not an MCP server

## B. Error Handling

- [x] `[all]` SKIP: no executable code — static PNG assets only. Verify script uses structured console output (2026-03-27)
- [ ] `[cli]` SKIP: not a CLI tool
- [ ] `[cli]` SKIP: not a CLI tool
- [ ] `[mcp]` SKIP: not an MCP server
- [ ] `[mcp]` SKIP: not an MCP server
- [ ] `[desktop]` SKIP: not a desktop app
- [ ] `[vscode]` SKIP: not a VS Code extension

## C. Operator Docs

- [x] `[all]` README is current: what it does, install, usage, supported platforms + runtime versions (2026-03-27)
- [x] `[all]` CHANGELOG.md (Keep a Changelog format) (2026-03-27)
- [x] `[all]` LICENSE file present and repo states support status (2026-03-27)
- [ ] `[cli]` SKIP: not a CLI tool
- [ ] `[cli|mcp|desktop]` SKIP: no logging — static assets
- [ ] `[mcp]` SKIP: not an MCP server
- [ ] `[complex]` SKIP: not a complex system

## D. Shipping Hygiene

- [x] `[all]` `verify` script exists (test + build + smoke in one command) (2026-03-27)
- [x] `[all]` Version in manifest matches git tag (2026-03-27)
- [ ] `[all]` SKIP: no dependencies to scan — static assets only
- [ ] `[all]` SKIP: no dependencies to update — static assets only
- [x] `[npm]` `npm pack --dry-run` includes: assets/, README.md, CHANGELOG.md, LICENSE (2026-03-27)
- [x] `[npm]` `engines.node` set (2026-03-27)
- [ ] `[npm]` SKIP: monorepo root is private, individual packs have no lockfile (static assets)
- [ ] `[vsix]` SKIP: not a VS Code extension
- [ ] `[desktop]` SKIP: not a desktop app

## E. Identity (soft gate — does not block ship)

- [ ] `[all]` Logo in README header
- [ ] `[all]` Translations (polyglot-mcp, 8 languages)
- [ ] `[org]` Landing page (@mcptoolshop/site-theme)
- [ ] `[all]` GitHub repo metadata: description, homepage, topics

---

## Gate Rules

**Hard gate (A-D):** Must pass before any version is tagged or published.
If a section doesn't apply, mark `SKIP:` with justification — don't leave it unchecked.

**Soft gate (E):** Should be done. Product ships without it, but isn't "whole."
