<p align="center">
  <img src="previews/logo.png" width="400" alt="Fantasy Heroes HD" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/fantasy-heroes-hd"><img src="https://img.shields.io/npm/v/@sprite-foundry/fantasy-heroes-hd" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/fantasy-heroes-hd/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

**16 high-fidelity 2.5D fantasy heroes — de-lit, engine-relightable, 8-direction.** The HD companion to [`@sprite-foundry/fantasy-heroes-48`](https://www.npmjs.com/package/@sprite-foundry/fantasy-heroes-48): the same party and the same export contract, rebuilt at illustration fidelity for games that light their sprites at runtime (HD-2D / 2.5D).

![Fantasy Heroes HD lineup](previews/lineup.png)

## Why de-lit?

These sprites carry **form and material; your engine supplies the light.** That is the HD-2D contract (Octopath Traveler, Sea of Stars): a placed light casts real shadows, the normal map turns a flat billboard into volume, the mask's ambient-occlusion deepens the folds and its roughness lets steel catch a highlight the cloth doesn't. The same hero reads correctly at noon, at dusk, and in a torch-lit dungeon — from one pack.

## What's Included

16 hero archetypes, each with **8 directional views × 4 map layers** at **512×512**, foot-anchored (pivot `[0.5, 1.0]`):

| Variant | Role | Identity cue |
|---------|------|--------------|
| Fighter | Frontline all-rounder | Grey hair, leather-and-scale armor, sword + round shield |
| Ranger | Ranged striker | Hooded green cloak, longbow, quiver |
| Mage | Arcane caster | Deep-blue robe, pointed hat, green-gem staff |
| Rogue | Flanker | Black hood, dark leather, face-mask, twin daggers |
| Cleric | Healer / support | White-and-gold robes, holy mace, sacred emblem |
| Barbarian | Heavy damage | Bare chest, red hair, fur kilt, two-handed axe |
| Paladin | Elite tank | Blue-and-silver plate, red-cross kite shield |
| Monk | Fast specialist | Topknot, sleeveless gi, green sash, bo staff |
| Bard | Support / buff | Burgundy doublet, feathered cap, lute |
| Druid | Nature magic | Antlered headdress, green-brown robes, vine staff |
| Warlock | Dark-pact DPS | Black hooded robe, purple eldritch energy |
| Sorcerer | Raw magic DPS | White hair, blue robe, glowing arcane aura |
| Artificer | Tech / utility | Leather coat, brass goggles, tool belt, gadget |
| Samurai | Melee / discipline | Dark-blue lamellar, kabuto helm, katana |
| Knight | Tank / frontline | Steel full plate, red-plumed helm, sword + shield |
| White Mage | Healer / holy | Blonde, white-and-gold robes, ornate golden staff |

### The four layers

| Layer | What it is | Use it for |
|---|---|---|
| **albedo** | de-lit base colour — **no baked light, shadow, or AO** | the sprite; your engine lights it |
| **normal** | view-space surface normals — OpenGL-style (Y up), blue ≈ toward camera (flip green for DirectX) | real-time directional lighting |
| **mask** | **R = ambient occlusion · G = roughness · B = emissive** | contact shadows, material sheen, self-glow |
| **depth** | linear camera-distance (white = near) | parallax / tooling (not 2D lighting) |

Every layer is pixel-aligned across the 8 directions; each hero ships a `manifest.json` (`schema_version 2.0.0`) with a per-file SHA-256, the pivot, the mask channel map, and per-engine notes.

## Install

```bash
npm install @sprite-foundry/fantasy-heroes-hd
```

## Folder Structure

```
assets/
  fighter/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching view-space normal maps
    mask/      8 matching AO/roughness/emissive masks
    depth/     8 matching depth maps
    manifest.json
  ...15 more
```

## Engine Compatibility

Plain PNG + JSON — load them anywhere, then wire the layers into your lighting pipeline:

- **Godot 4** — `albedo` on a `Sprite2D`, `normal` via `CanvasTexture.normal_texture`, a `PointLight2D`; sample `mask.g` for specular, `mask.r` to modulate ambient.
- **Unity URP (2D)** — `albedo` → `_BaseMap`, `normal` → `_NormalMap`, `mask` → `_MaskMap` (R=AO, G=roughness).
- **Phaser / PixiJS / custom** — `albedo` + `normal` into the 2D lighting pipeline; `mask` / `depth` are tooling-side.

`manifest.json` carries the per-engine notes in `engineNotes`. No engine-specific format, no runtime dependency.

## The `-hd` line vs the `48` line

`fantasy-heroes-48` (retro 48px pixel-art) and `fantasy-heroes-hd` are **parallel tiers, not a breaking upgrade.** Same 16 heroes, same direction order, same foot-anchored framing — ship the 48px pack for a pixel game, ship `-hd` for a high-fidelity 2.5D game. Pick the tier your renderer wants.

## Specs

- **Variants:** 16 hero archetypes
- **Tile size:** 512 × 512 px
- **Directions:** 8
- **Layers:** albedo + normal + mask (AO/roughness/emissive) + depth
- **Total sprites:** 512 (16 × 8 × 4)
- **Format:** transparent PNG + `manifest.json` (schema 2.0.0)
- **Pivot:** `[0.5, 1.0]` (foot-anchored)

## How it's made (and why it's commercial-clean)

Each hero starts as a fresh high-fidelity concept in a house-trained painterly style (**Qwen-Image**, Apache-2.0). The 8 directional views are generated **without a 3D mesh** — **Qwen-Image-Edit-2511** (Apache-2.0) rotates the camera around the character while holding identity, so the face and detail survive every angle. Each view is then decomposed into its 2.5D layers by single-image estimators: a de-lit albedo + roughness from **Marigold-IID** (Apache-2.0 code, OpenRAIL weights — commercial-OK), real surface normals from **Marigold-Normals**, depth from **Depth-Anything-V2-Base** (Apache-2.0), a clean alpha matte from **BiRefNet** (MIT), and ambient occlusion derived from the depth — then packed to the contract above. The original `fantasy-heroes-48` silhouette, palette, and signature prop are preserved per hero. Identity stays in the image model — **no InsightFace / InstantID / face-adapter weights** (which carry non-commercial licenses) touch this pack. Every component is Apache-2.0 / MIT / commercial-OpenRAIL; the assets are yours to ship.

## Security

This package contains **only static PNG images and JSON metadata** — no executable code, no install hooks, no network access, no telemetry. See [SECURITY.md](SECURITY.md).

## License

MIT — use in commercial and non-commercial projects.

## Credits

Built by <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> with the [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) no-mesh 2.5D pipeline (Qwen-Image + Qwen-Image-Edit + Marigold + Depth-Anything-V2).
