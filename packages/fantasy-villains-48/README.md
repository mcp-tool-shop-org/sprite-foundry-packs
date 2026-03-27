<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/fantasy-villains-sprite-pack/readme.png" width="400" alt="Fantasy Villains" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/fantasy-villains-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/fantasy-villains-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/fantasy-villains-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/fantasy-villains-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/fantasy-villains-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://mcp-tool-shop-org.github.io/fantasy-villains-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page" /></a>
</p>

A 48px, 8-direction pixel-art pack of boss-ready humanoid antagonists with albedo, normal, and depth maps for engine-agnostic game use.

![Fantasy Villains Banner](previews/banner.png)

## What's Included

8 villain archetypes — elite humanoid antagonists, not generic monsters:

![Variant Lineup](previews/lineup.png)

| Variant | Role | Silhouette |
|---------|------|------------|
| Blackguard | Elite tank | Closed dark helm, tower shield, spiked mace, black plate |
| Dread Ranger | Ranged hunter | Skull mask over hood, longbow, bone trophies, tattered cloak |
| Necromancer | Summoner/caster | Bone crown, skull staff, tattered robes, gaunt frame |
| Assassin | Flanker | Face mask, curved daggers, vial bandolier, compact crouched posture |
| Cult Priest | Support/debuffer | Horned headdress, censer on chain, structured red/black vestments |
| Reaver | Heavy damage | Executioner's cleaver, half-mask, bare scarred torso, widest villain |
| Warlord | Commander | Crown-helm with plume, halberd, banner on back, ornate gold/red armor |
| Dark Monk | Fast specialist | Shaved tattooed head, chain-weighted staff, metal-studded wraps |

Each variant ships with three map layers:

- **Albedo** — base color sprites (transparent PNG)
- **Normal** — normal maps for dynamic lighting
- **Depth** — depth maps for parallax and elevation effects

## Install

```bash
npm install @sprite-foundry/fantasy-villains-48
```

## Folder Structure

```
assets/
  blackguard/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  dread-ranger/
  necromancer/
  assassin/
  cult-priest/
  reaver/
  warlord/
  dark-monk/
pack.json          pack-level index
previews/          banner and lineup sheets
```

## Manifest Format

Each variant has a `manifest.json`:

```json
{
  "slug": "blackguard",
  "name": "Blackguard",
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

Want to generate additional villain variants that match this pack's art style and export contract?

This pack was produced with [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), an open-source ComfyUI + SDXL pixel-art generation pipeline. The foundry repo contains everything you need:

- **Generation pipeline** — `pipeline/foundry_gen.py` drives ComfyUI with per-subject configs
- **Subject configs** — `pipeline/chars/villain_*.json` define the exact prompts, seeds, silhouette rules, and reject conditions for every variant in this pack
- **Batch manifest** — `pipeline/manifests/fantasy_villains_04.json` maps all 8 configs to the export structure
- **Export CLI** — `foundry export <run_id>` produces deterministic packs with checksums
- **ControlNet tuning** — humanoid depth strength 0.60, end% 0.85 (documented in the manifest)

To add a new variant:

1. Create a subject config in `pipeline/chars/` following the existing villain configs
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
