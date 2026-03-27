---
title: Security
description: Trust model and security posture for Sprite Foundry asset packs.
sidebar:
  order: 5
---

## Trust model

Sprite Foundry Packs contain **static image assets only**. There is no executable code, no install scripts, and no runtime dependencies.

### What these packs touch

- **PNG image files** read from disk by your game engine at load time
- **JSON manifest files** with metadata, checksums, and provenance

### What these packs do NOT touch

- No filesystem writes — read-only static assets
- No network connections — no fetching, no telemetry, no analytics
- No secrets or credentials — nothing to read, store, or transmit
- No environment variables — no configuration needed
- No child processes — no scripts execute at install or runtime

### Permissions required

**None.** These are static files consumed by your game engine's asset loader.

## Provenance

Every sprite includes a `manifest.json` with full generation provenance:

- **Run ID** — links back to the Sprite Foundry generation run
- **Seed** — exact seed used for reproducibility
- **Git hash** — source commit of the generation pipeline
- **Checkpoint + LoRA** — exact model and weights used
- **SHA-256 checksums** — per-file integrity verification

## Integrity verification

Each pack includes a verify script that checks all assets exist and are structurally valid:

```bash
cd node_modules/@sprite-foundry/fantasy-heroes-48
npm run verify
```

The verify script:
1. Reads `pack.json` for the variant registry
2. Reads each variant's `manifest.json`
3. Checks that all expected PNG files exist (8 directions x 3 layers = 24 per variant)
4. Reports any missing files

## npm package safety

- **No `postinstall` hooks** — nothing runs at install time
- **No dependencies** — each pack is self-contained
- **`files` allowlist** — only `assets/`, `previews/`, `pack.json`, and docs are published
- **Public on npm** — source visible, auditable

## Reporting vulnerabilities

Email: **64996768+mcp-tool-shop@users.noreply.github.com**

Response timeline:
- Acknowledge: 48 hours
- Assess severity: 7 days
- Release fix: 30 days
