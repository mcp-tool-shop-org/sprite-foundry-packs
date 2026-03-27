<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/zombie-sprite-pack/readme.png" width="400" alt="Undead Patrol">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/undead-patrol-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/undead-patrol-48" alt="npm version"></a>
  <a href="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/zombie-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

A 48px, 8-direction pixel-art zombie enemy pack with albedo, normal, and depth maps for engine-agnostic game use.

![Undead Patrol Banner](previews/banner.png)

## What's Included

8 zombie variants, each with 8 directional views:

![Variant Lineup](previews/lineup.png)

| Variant | Role | Silhouette |
|---------|------|------------|
| Shambler | Baseline undead | Hunched, slow, broken posture |
| Runner | Fast threat | Lean, forward, aggressive stride |
| Riot Zombie | Armored tank | Heavy shoulders, shield/armor bulk |
| Hazmat Zombie | Contaminated specialist | Suit mass, round hood profile |
| Bloater | Area threat | Wide torso, swollen asymmetry |
| Skeletal Zombie | Fragile/ancient | Thin limbs, angular read |
| Worker Zombie | Industrial/civilian | Uniform, tool-belt, readable gear |
| Elite Zombie | Commander/brute | Tall, imposing, upgraded mass |

Each variant ships with three map layers:

- **Albedo** — base color sprites (transparent PNG)
- **Normal** — normal maps for dynamic lighting
- **Depth** — depth maps for parallax and elevation effects

## Install

```bash
npm install @sprite-foundry/undead-patrol-48
```

## Folder Structure

```
assets/
  shambler/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  runner/
  riot-zombie/
  hazmat-zombie/
  bloater/
  skeletal-zombie/
  worker-zombie/
  elite-zombie/
pack.json          pack-level index
previews/          banner and lineup sheets
```

## Manifest Format

Each variant has a `manifest.json`:

```json
{
  "slug": "shambler",
  "name": "Shambler",
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

The pack-level `pack.json` indexes all variants with paths to each manifest.

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

- **Tile size:** 48 x 48 px
- **Directions:** 8 (front, front_left, left, back_left, back, back_right, right, front_right)
- **Format:** transparent PNG
- **Maps:** albedo + normal + depth
- **Animation:** static poses (v1)
- **Perspective:** top-down

## Extending the Pack

Want to generate additional zombie variants that match this pack's art style and export contract?

This pack was produced with [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), an open-source ComfyUI + SDXL pixel-art generation pipeline. The foundry repo contains everything you need:

- **Generation pipeline** — `pipeline/foundry_gen.py` drives ComfyUI with per-subject configs
- **Subject configs** — `pipeline/chars/zombie_*.json` define the exact prompts, seeds, silhouette rules, and reject conditions for every variant in this pack
- **Batch manifest** — `pipeline/manifests/undead_patrol_01.json` maps all 8 configs to the export structure
- **Export CLI** — `foundry export <run_id>` produces deterministic packs with checksums
- **ControlNet tuning** — humanoid depth strength 0.60, end% 0.85 (documented in the manifest)

To add a new variant:

1. Create a subject config in `pipeline/chars/` following the existing zombie configs
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
