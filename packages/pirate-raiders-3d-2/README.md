<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/readme.png" width="100%" alt="Pirate Raiders 3D-2 lineup" />
</p>

# Pirate Raiders 3D-2

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/pirate-raiders-3d-2"><img src="https://img.shields.io/npm/v/@sprite-foundry/pirate-raiders-3d-2" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/pirate-raiders-3d-2/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

**26 fantasy-pirate raiders, pre-rendered from true 3D meshes — 8 directions, perfect all-angle consistency, next-generation pipeline.** This is the second generation of the `pirate-raiders-3d` line: every raider is meshed once, then **one texture is baked onto that mesh from the reference art** (not regenerated per angle), so a held cutlass, a coiled rope, a minotaur's horns, and a turtle's shell are **the exact same object in every direction, pixel-for-pixel consistent** — no per-view drift, no re-imagined detail, no "which angle was this generated from" guessing. A **multi-species free-port raider crew**: a human captain commanding orcs, ogres, a sea-troll, goblins, dwarves, and a deep roster of rarer folk — lizardfolk, sahuagin, gnoll, dragonborn, minotaur, tortle, ratfolk, kenku, half-giant, and grung. **16 species — 7 human, 19 non-human.**

## What changed from `pirate-raiders-3d`

The original pack finished each angle with an independent image-generation pass per direction — a proven approach for adding painterly finish, but one where fine details (a hat's exact shape, a beard's color, a small prop) could drift slightly from angle to angle, since each of the 8 views was its own generation. This pack closes that gap architecturally: instead of regenerating appearance per view, **one texture is baked directly onto the 3D mesh** from the character's reference art, and all 8 camera angles are then just different views of that *one* textured object. There is no per-angle regeneration step left to drift. This is the same fix the wider 3D/graphics field converged on for exactly this problem (shared texture-baking over independent per-view diffusion) — see **How it's made** below.

The tradeoff, for now: this generation ships the **raw 3D render look only** — no painterly finish pass yet. If you want the hand-painted house-style finish, `pirate-raiders-3d` (the original pack) still ships that look; this pack is the sharper, more consistent 3D-native look, and a painterly pass over these new bases is a natural next step, not a promise made here.

## The full crew, turnaround by turnaround

Every raider below is the **same 3D mesh**, shown from 8 fixed camera angles (front, front-right, right, back-right, back, back-left, left, front-left). Nothing here was regenerated per angle — this is one object, rotated.

### Captain
![Captain turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/captain.png)

### Navigator
![Navigator turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/navigator.png)

### Sea-Witch
![Sea-Witch turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/sea-witch.png)

### Sawbones
![Sawbones turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/sawbones.png)

### Swashbuckler
![Swashbuckler turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/swashbuckler.png)

### Smuggler
![Smuggler turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/smuggler.png)

### Cabin Kid
![Cabin Kid turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/cabin-kid.png)

### First Mate
![First Mate turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/first-mate.png)

### Harpooner
![Harpooner turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/harpooner.png)

### Bosun
![Bosun turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/bosun.png)

### Berserker
![Berserker turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/berserker.png)

### Breaker
![Breaker turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/breaker.png)

### Marksman
![Marksman turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/marksman.png)

### Bombardier
![Bombardier turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/bombardier.png)

### Quartermaster
![Quartermaster turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/quartermaster.png)

### Cannoneer
![Cannoneer turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/cannoneer.png)

### Diver
![Diver turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/diver.png)

### Tide-Cultist
![Tide-Cultist turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/tide-cultist.png)

### Reaver
![Reaver turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/reaver.png)

### Marine
![Marine turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/marine.png)

### Juggernaut
![Juggernaut turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/juggernaut.png)

### Cook
![Cook turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/cook.png)

### Rigger
![Rigger turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/rigger.png)

### Stormcaller
![Stormcaller turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/stormcaller.png)

### Brig-Keeper
![Brig-Keeper turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/brig-keeper.png)

### Poisoner
![Poisoner turnaround](https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-3d-2/turnarounds/poisoner.png)

## What's Included

26 crew archetypes across 16 species, each with **8 directional views** at **768×768**, foot-anchored (pivot `[0.5, 1.0]`), on transparent alpha:

| Variant | Species | Role | Identity cue |
|---------|---------|------|--------------|
| Captain | human | fleet commander | Sea-coat, tricorn hat, wide buckled belt |
| Navigator | human | charts & helm | Bandana, astrolabe, rolled sea-chart |
| Sea-Witch | human | sea-magic caster | Sea-green robes, shells, coral staff |
| Sawbones | human | ship surgeon | Blood-stained apron, surgical saw |
| Swashbuckler | human | duelist | Open shirt, sash, feathered hat, rapier |
| Smuggler | human | fence / contraband | Hooded coat, many pockets, sash |
| Cabin Kid | human | deckhand | Oversized coat, flat cap, sash |
| First Mate | orc | enforcer | Tusks, officer's sea-coat |
| Harpooner | orc | ranged hunter | Tusks, bare arms, barbed harpoon |
| Bosun | ogre | deck discipline | Huge, harness straps, belaying maul |
| Berserker | ogre | boarding bruiser | Bare scarred chest, anchor-hook |
| Breaker | sea-troll | siege brute | Warty grey-green hide, anchor-club |
| Marksman | goblin | crossbow sniper | Green skin, brass eyepiece, crossbow |
| Bombardier | goblin | sea-bombs | Goggles, lit sea-bomb, explosive satchel |
| Quartermaster | dwarf | supplies & coin | Braided beard, ledger, hand-cannon |
| Cannoneer | dwarf | deck guns | Braided beard, apron, deck-cannon |
| Diver | lizardfolk | pearl-hunter | Scaled crest, tail, empty clawed hands |
| Tide-Cultist | sahuagin | kraken priest | Fins, scales, barnacled robes, idol-staff |
| Reaver | gnoll | frenzied boarder | Hyena head, mane, twin curved knives |
| Marine | dragonborn | armored boarder | Scaled, horned, naval armor, pike + shield |
| Juggernaut | minotaur | anchor tank | Bull head, horns, ship's anchor |
| Cook | tortle | galley & cleaver | Turtle shell, beak, apron |
| Rigger | ratfolk | topman / ropes | Rat head, whiskers, long tail, spyglass |
| Stormcaller | kenku | storm-magic | Crow/beaked mask, feathers, staff |
| Brig-Keeper | half-giant | jailer | Towering, leather vest, keys + chain |
| Poisoner | grung | dart & toxin | Bright frog-folk, blowgun at the mouth |

Each raider ships a `manifest.json` (`schema_version 2.0.0`) with a per-file SHA-256, the pivot, and per-engine notes.

## Install

```bash
npm install @sprite-foundry/pirate-raiders-3d-2
```

## Folder Structure

```
assets/
  captain/
    render/      8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    manifest.json
  ...25 more
```

The turnaround showcase images above are hosted in the [brand asset registry](https://github.com/mcp-tool-shop-org/brand/tree/main/logos/pirate-raiders-3d-2) at full resolution — they aren't shipped in the npm package itself, which only carries the game-ready sprite assets.

## Engine Compatibility

Plain transparent PNG + JSON — load them anywhere. Because the art is **pre-lit**, use an **unshaded / unlit** material; do not add a normal map.

- **Godot 4** — `render` on a `Sprite2D`, or as a billboarded `Sprite3D` with an unshaded `StandardMaterial3D`; depth-sort by the pivot. Swap the directional frame from your facing angle.
- **Unity (2D / URP)** — a **Sprite-Unlit** material with `_BaseMap` = the render frame; flip frames per facing.
- **Phaser / PixiJS / custom** — drop the PNG in as a sprite frame.

`manifest.json` carries the per-engine notes in `engineNotes`. No engine-specific format, no runtime dependency.

## The `-3d` line vs `-3d-2` vs `-hd` vs `48`

Four parallel tiers of the same fantasy raider crew, **same 26 archetypes**, different production and contract:

- **`pirate-raiders-48`** — retro 48px pixel art, for a pixel game.
- **`pirate-raiders-hd`** — high-fidelity 2.5D, **de-lit** (albedo + normal + mask + depth), for engines that **light the sprite at runtime**.
- **`pirate-raiders-3d`** — true-3D pre-rendered, **pre-lit**, two finished looks (painterly + raw render).
- **`pirate-raiders-3d-2`** (this pack) — next-gen true-3D pre-rendered, **pre-lit**, single sharper/more-consistent raw-render look (single-texture-bake, zero per-angle drift).

Pick `-hd` if you want to control the lighting yourself; pick `-3d` if you want both a painterly and a raw look; pick `-3d-2` if cross-angle consistency is the priority and you're fine with the raw-render look for now.

## Specs

- **Variants:** 26 crew archetypes across 16 species (7 human / 19 non-human)
- **Tile size:** 768 × 768 px
- **Directions:** 8 (`front, front_left, left, back_left, back, back_right, right, front_right`)
- **Look:** raw 3D render (pre-lit, transparent)
- **Total sprites:** 208 (26 × 8)
- **Format:** transparent PNG + `manifest.json` (schema 2.0.0)
- **Pivot:** `[0.5, 1.0]` (foot-anchored)

## How it's made (and why it's commercial-clean)

Each raider starts as a fresh high-fidelity concept in a house-trained painterly style (**Qwen-Image**, Apache-2.0). That concept is lifted into a textured 3D mesh by **TRELLIS.2** (MIT). Where earlier passes needed a touch-up, the mesh's **shape-conditioned texture generation** (also TRELLIS.2, MIT) re-bakes a single, clean texture directly onto the mesh from the reference art — one bake, not eight independent ones. The mesh is then **rendered from 8 fixed camera angles** in Blender (Cycles / OptiX, transparent alpha, OpenImageDenoise). Because every angle is a camera view of the *same* textured object, held props, fine color, and small details can't drift between views — there's no independent per-angle generation step left where drift could enter. This mirrors the fix the broader 3D-generation research field converged on for the same problem (independent per-view diffusion sampling breaking consistency across views — sometimes called the "Janus problem"): the reliable answer is a shared or single-pass texture, not per-view regeneration. No 3D geometry ships; you get pre-rendered 2.5D sprites. Every component is MIT / Apache-2.0; the assets are yours to ship in commercial and non-commercial projects.

## Security

This package contains **only static PNG images and JSON metadata** — no executable code, no install hooks, no network access, no telemetry. See [SECURITY.md](SECURITY.md).

## License

MIT — use in commercial and non-commercial projects.

## Credits

Built by <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> with the [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 3D pre-render pipeline (Qwen-Image + TRELLIS.2 mesh + TRELLIS.2 texture-bake + Blender).
