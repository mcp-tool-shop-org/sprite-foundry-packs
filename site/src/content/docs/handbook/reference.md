---
title: Reference
description: Manifest schema, asset contracts, and directory layout for Sprite Foundry packs.
sidebar:
  order: 4
---

## Directory layout

Every pack follows an identical structure:

```
@sprite-foundry/<pack>/
  pack.json                  ← pack-level index
  assets/
    <variant>/
      manifest.json          ← per-variant metadata
      albedo/
        front.png
        front_left.png
        left.png
        back_left.png
        back.png
        back_right.png
        right.png
        front_right.png
      normal/
        (same 8 directions)
      depth/
        (same 8 directions)
  previews/
    <variant>-preview.png    ← contact sheet
```

## pack.json schema

The pack-level index describes the collection:

```json
{
  "name": "Undead Patrol",
  "slug": "undead-patrol",
  "version": "1.0.0",
  "tileSize": 48,
  "directions": ["front","front_left","left","back_left","back","back_right","right","front_right"],
  "layers": ["albedo","normal","depth"],
  "variants": [
    {
      "slug": "shambler",
      "name": "Shambler",
      "role": "Basic melee enemy",
      "path": "assets/shambler/manifest.json"
    }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name of the pack |
| `slug` | string | URL-safe identifier |
| `version` | string | Semver version |
| `tileSize` | number | Pixel dimensions (always 48) |
| `directions` | string[] | 8 cardinal + ordinal directions |
| `layers` | string[] | Map layer types |
| `variants` | object[] | Character variants in the pack |

## manifest.json schema

Each variant has a manifest with full provenance:

```json
{
  "schema_version": "1.0.0",
  "identity": {
    "subject_slug": "shambler",
    "display_name": "Shambler",
    "body_family": "bipedal"
  },
  "provenance": {
    "run_id": "foundry-run-042",
    "seed": 12345,
    "generation_timestamps": { "start": "...", "end": "..." },
    "regen_count": 0,
    "reject_count": 0,
    "git_hash": "abc1234"
  },
  "generation_stack": {
    "checkpoint": "juggernautXL",
    "lora": { "name": "pixel-art-xl", "weight": 0.85 }
  },
  "render_contract": {
    "width": 48,
    "height": 48,
    "direction_order": ["front","front_left","left","back_left","back","back_right","right","front_right"],
    "pivot": "center_bottom",
    "transparency": true
  },
  "files": {
    "albedo/front.png": { "sha256": "..." },
    "normal/front.png": { "sha256": "..." },
    "depth/front.png": { "sha256": "..." }
  }
}
```

### Key fields

| Field | Purpose |
|-------|---------|
| `render_contract.pivot` | Anchor point for sprite alignment — always `center_bottom` |
| `render_contract.direction_order` | Canonical order for animation frame indexing |
| `files` | SHA-256 checksums for integrity verification |
| `provenance` | Full generation audit trail |
| `generation_stack` | Model and LoRA used for generation |

## Directions

All packs use the same 8-direction system, ordered clockwise from front-facing:

```
        back
   back_left  back_right
      left      right
front_left  front_right
        front
```

Direction index (for sprite sheet or animation frame mapping):

| Index | Direction |
|-------|-----------|
| 0 | front |
| 1 | front_left |
| 2 | left |
| 3 | back_left |
| 4 | back |
| 5 | back_right |
| 6 | right |
| 7 | front_right |

## Map layers

### Albedo

Standard RGBA color sprite. Use as-is for basic rendering.

### Normal

Tangent-space normal map encoded in RGB:
- R = X axis (left/right surface angle)
- G = Y axis (up/down surface angle)
- B = Z axis (surface facing camera = bright blue)

Flat surfaces encode as `(128, 128, 255)` — standard OpenGL convention.

### Depth

Grayscale height map:
- **White (255)** = closest to camera
- **Black (0)** = farthest from camera

Use for parallax scrolling, occlusion sorting, or shadow casting.

## Render contract guarantees

Every sprite across all packs guarantees:

- **48x48 pixels** — consistent tile size
- **Transparent background** — PNG alpha channel
- **Center-bottom pivot** — feet at pixel (24, 48)
- **Consistent silhouettes** — same character recognizable across all 8 directions
- **Layer alignment** — albedo, normal, and depth maps are pixel-perfect aligned
