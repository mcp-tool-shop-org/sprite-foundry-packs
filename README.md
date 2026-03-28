<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/sprite-foundry-packs/readme.png" width="500" alt="Sprite Foundry Packs" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/actions"><img src="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" /></a>
  <a href="https://mcp-tool-shop-org.github.io/sprite-foundry-packs/"><img src="https://img.shields.io/badge/Landing_Page-blue" alt="Landing Page" /></a>
</p>

Monorepo for all [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) asset packs. Each pack ships 16 character variants with 8 directional sprites across 3 map layers (albedo, normal, depth) at 48px resolution.

## Packs

| Pack | npm | Variants | Theme |
|------|-----|----------|-------|
| Undead Patrol | [`@sprite-foundry/undead-patrol-48`](https://www.npmjs.com/package/@sprite-foundry/undead-patrol-48) | 16 (8 zombies + 8 living) | Horror/survival |
| Goblin Warband | [`@sprite-foundry/goblin-warband-48`](https://www.npmjs.com/package/@sprite-foundry/goblin-warband-48) | 16 (8 combat + 8 camp) | Fantasy enemies |
| Fantasy Heroes | [`@sprite-foundry/fantasy-heroes-48`](https://www.npmjs.com/package/@sprite-foundry/fantasy-heroes-48) | 16 (8 core + 8 second party) | Classic RPG party |
| Fantasy Villains | [`@sprite-foundry/fantasy-villains-48`](https://www.npmjs.com/package/@sprite-foundry/fantasy-villains-48) | 16 (8 elite + 8 court) | Boss encounters |
| Pirate Raiders | [`@sprite-foundry/pirate-raiders-48`](https://www.npmjs.com/package/@sprite-foundry/pirate-raiders-48) | 16 (8 officers + 8 crew) | Maritime/naval |
| Townsfolk | [`@sprite-foundry/townsfolk-48`](https://www.npmjs.com/package/@sprite-foundry/townsfolk-48) | 16 (8 town core + 8 town life) | Medieval NPCs |
| Monster Pack | [`@sprite-foundry/monster-pack-48`](https://www.npmjs.com/package/@sprite-foundry/monster-pack-48) | 16 (6 body classes) | Monster bestiary |

## Install

```bash
# Install any pack individually
npm install @sprite-foundry/undead-patrol-48
npm install @sprite-foundry/goblin-warband-48
npm install @sprite-foundry/fantasy-heroes-48
npm install @sprite-foundry/fantasy-villains-48
npm install @sprite-foundry/pirate-raiders-48
npm install @sprite-foundry/townsfolk-48
npm install @sprite-foundry/monster-pack-48
```

## Asset Structure

Each pack follows an identical structure:

```
<pack>/assets/<variant>/
  albedo/     8 directional PNGs (base color)
  normal/     8 directional PNGs (dynamic lighting)
  depth/      8 directional PNGs (parallax/elevation)
  manifest.json   provenance + render contract + SHA-256 checksums
```

**Directions:** front, front_left, left, back_left, back, back_right, right, front_right

**Resolution:** 48x48px transparent PNGs

## Usage

```javascript
import { resolve } from 'path';

// Load a sprite from an installed pack
const spritePath = resolve(
  'node_modules/@sprite-foundry/undead-patrol-48/assets/shambler/albedo/front.png'
);

// Read the manifest for metadata
const manifest = require('@sprite-foundry/undead-patrol-48/assets/shambler/manifest.json');
```

Works with any engine: Godot, Phaser, PixiJS, RPG Maker, Unity, or raw canvas.

## Verify

```bash
# Verify all packs
npm run verify

# Verify a single pack
cd packages/undead-patrol-48 && npm run verify
```

## Per-Pack Assets

Each pack contains:
- **384 PNG sprites** (16 variants x 8 directions x 3 layers)
- **16 manifests** with full provenance and checksums
- **16 preview sheets** for visual reference
- **Total across all 7 packs: 2,688 sprites**

## Security and Trust

This repository contains **static image assets only**.

- **Data touched:** PNG files read from disk at install time
- **No executable code** — no install scripts, no postinstall hooks
- **No network egress** — assets are consumed locally
- **No secrets or credentials** in source or output
- **No telemetry** collected or sent
- **Permissions:** none required — read-only static files

## Monorepo Structure

```
sprite-foundry-packs/
  packages/
    undead-patrol-48/      @sprite-foundry/undead-patrol-48
    goblin-warband-48/     @sprite-foundry/goblin-warband-48
    fantasy-heroes-48/     @sprite-foundry/fantasy-heroes-48
    fantasy-villains-48/   @sprite-foundry/fantasy-villains-48
    pirate-raiders-48/     @sprite-foundry/pirate-raiders-48
    townsfolk-48/          @sprite-foundry/townsfolk-48
    monster-pack-48/       @sprite-foundry/monster-pack-48
  tooling/
    verify-all.mjs         shared verification script
```

Each pack is independently versioned and publishable to npm.

## Platforms

- **Node.js:** >= 14.0.0
- **Engines:** Godot 4.x, Phaser 3, PixiJS 7+, RPG Maker MZ, Unity (via StreamingAssets), or any engine that reads PNGs
- **OS:** Windows, macOS, Linux

## License

MIT

---

Built by <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
