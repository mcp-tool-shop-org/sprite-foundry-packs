---
title: Sprite Foundry Packs
description: 48px pixel-art sprite packs with albedo, normal, and depth maps for any game engine.
sidebar:
  order: 0
---

Sprite Foundry Packs is a collection of production-ready 48px pixel-art sprite packs, each published independently to npm. Every pack ships 8 character variants with full 8-directional coverage and 3-layer maps (albedo, normal, depth) for dynamic lighting and parallax effects.

## The catalog

| Pack | npm package | Variants | Theme |
|------|------------|----------|-------|
| Undead Patrol | `@sprite-foundry/undead-patrol-48` | 8 zombies | Horror/survival |
| Goblin Warband | `@sprite-foundry/goblin-warband-48` | 8 goblins | Fantasy enemies |
| Fantasy Heroes | `@sprite-foundry/fantasy-heroes-48` | 8 heroes | Classic RPG party |
| Fantasy Villains | `@sprite-foundry/fantasy-villains-48` | 8 villains | Boss encounters |
| Pirate Raiders | `@sprite-foundry/pirate-raiders-48` | 8 pirates | Maritime/naval |

## What you get per pack

- **192 PNG sprites** — 8 variants x 8 directions x 3 map layers
- **8 JSON manifests** — provenance, render contract, SHA-256 checksums per variant
- **8 preview sheets** — visual reference for each character
- **Zero runtime code** — static assets only, no install scripts, no dependencies

## Why 3 layers?

| Layer | Purpose | Use case |
|-------|---------|----------|
| **Albedo** | Base color sprite | Standard rendering, retro-style games |
| **Normal** | Per-pixel surface normals | Dynamic lighting (torches, spells, day/night) |
| **Depth** | Height/elevation data | Parallax scrolling, occlusion, shadow casting |

Most engines can use just the albedo layer. Normal and depth maps unlock advanced visual effects when your engine supports them.

## Quick start

```bash
npm install @sprite-foundry/fantasy-heroes-48
```

Then load sprites from `node_modules` using your engine's asset loader. See the [Getting Started](/sprite-foundry-packs/handbook/getting-started/) guide for engine-specific examples.
