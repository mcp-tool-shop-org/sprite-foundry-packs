<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/monster-pack/readme.png" width="400" alt="Monster Pack" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/monster-pack-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/monster-pack-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/monster-pack-48/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

A 48px, 8-direction pixel-art monster bestiary with albedo, normal, and depth maps for engine-agnostic game use.

![Monster Pack Banner](previews/banner.png)

## What's Included

16 monster variants across 6 body classes:

![Variant Lineup](previews/lineup.png)

### Humanoid

| Variant | Role | Silhouette |
|---------|------|------------|
| Bell Warden | Curse / area denial | Robed figure with heavy bell, chains, copper tones |
| Hollow Knight | Elite melee | Empty suit of armor, sword, skull sigil |
| Teeth Collector | Rogue / scavenger | Goblin-like, oversized teeth grin, long coat |

### Tall/Thin

| Variant | Role | Silhouette |
|---------|------|------------|
| Ink Shade | Stealth / assassin | Dark elongated figure, dripping inky limbs |
| Lantern Angler | Lure / ambush predator | Bioluminescent lure, translucent skin, needle teeth |
| Mirror Stalker | Reflect / counter | Reflective surface, crystal shards, razor limbs |
| Root Puppet | Parasite / control | Corpse animated by parasitic roots, bark legs |
| Throat Singer | Sonic / crowd control | Skeletal frame, exposed ribcage, dark cloak |

### Wide/Squat

| Variant | Role | Silhouette |
|---------|------|------------|
| Clock Golem | Heavy tank | Mechanical construct, gear torso, heavy limbs |
| Grinning Idol | Environmental hazard | Animated stone totem, carved grin, moss-covered |
| Hive Keeper | Swarm summoner | Giant insectoid, chitin plates, compound eyes |

### Amorphous

| Variant | Role | Silhouette |
|---------|------|------------|
| Mud Revenant | Slow pursuit | Dripping clay figure, ember eyes, burial shroud |
| Rat King | Swarm boss | Fused mass of rats, knotted tails, many eyes |
| Spore Mother | AoE / debuff | Fungal mass, mushroom cap crown, spore cloud |

### Arthropod

| Variant | Role | Silhouette |
|---------|------|------------|
| Bone Weaver | Trap / ambush | Spider built from stolen bones, skull head |

### Winged

| Variant | Role | Silhouette |
|---------|------|------------|
| Wyvern | Flying boss | Two-legged dragon, bat wings, barbed tail |

Each variant ships with three map layers:

- **Albedo** — base color sprites (transparent PNG)
- **Normal** — normal maps for dynamic lighting
- **Depth** — depth maps for parallax and elevation effects

## Install

```bash
npm install @sprite-foundry/monster-pack-48
```

## Folder Structure

```
assets/
  bell_warden/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  bone_weaver/
  clock_golem/
  ...
pack.json          pack-level index (includes bodyClass per variant)
previews/          banner and lineup sheets
```

## Manifest Format

Each variant has a `manifest.json`:

```json
{
  "slug": "rat_king",
  "name": "Rat King",
  "version": "1.0.0",
  "tileSize": 48,
  "directions": ["front", "front_left", "left", "back_left", "back", "back_right", "right", "front_right"],
  "layers": {
    "albedo": "albedo/{direction}.png",
    "normal": "normal/{direction}.png",
    "depth": "depth/{direction}.png"
  },
  "preview": "preview/contact_sheet.png"
}
```

The pack-level `pack.json` indexes all variants with paths to each manifest and includes `bodyClass` metadata.

## Engine Compatibility

These are plain PNG files with JSON metadata. They work with any engine or framework that can load images:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Custom engines

No engine-specific format or runtime dependency.

## Specs

- **Variants:** 16 monsters
- **Body classes:** 6 (humanoid, tall/thin, wide/squat, amorphous, arthropod, winged)
- **Tile size:** 48 x 48 px
- **Directions:** 8 (front, front_left, left, back_left, back, back_right, right, front_right)
- **Total sprites:** 384 (16 x 8 x 3)
- **Format:** transparent PNG
- **Maps:** albedo + normal + depth
- **Animation:** static poses (v1)
- **Perspective:** top-down

## Extending the Pack

Want to generate additional monster variants that match this pack's art style and export contract?

This pack was produced with [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), an open-source ComfyUI + SDXL pixel-art generation pipeline. Non-humanoid monsters use the **monster lane** — body-class-specific ControlNet depth guides that enforce exotic body plans without forcing a human skeleton. The foundry repo contains everything you need:

- **Generation pipeline** — `pipeline/foundry_gen.py` drives ComfyUI with per-subject configs
- **Subject configs** — `pipeline/chars/beast_*.json` define the exact prompts, seeds, and body class for every variant in this pack
- **Depth generators** — `pipeline/morph_refs/gen_amorphous_depth.py`, `gen_wide_squat_depth.py`, `gen_tall_thin_depth.py`
- **Body class presets** — auto-select ControlNet strength and timing per creature type
- **Export CLI** — `foundry export <run_id>` produces deterministic packs with checksums

To add a new variant:

1. Create a subject config in `pipeline/chars/` following the existing beast configs
2. Register: `python -m foundry.cli subject-add <id> --name "Name"`
3. Generate: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Review, accept, produce maps, accept finish, export
5. Copy the exported pack into the matching `assets/<slug>/` directory

The [Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) has the full pipeline walkthrough.

## Security

This package contains **only static PNG images and JSON metadata**. There is no executable code, no install hooks, no network access, and no telemetry. Assets are read-only by design.

See [SECURITY.md](SECURITY.md) for the full security policy.

## License

MIT — use in commercial and non-commercial projects.

## Credits

Generated with [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) using ComfyUI + SDXL pixel-art pipeline.

Built by <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
