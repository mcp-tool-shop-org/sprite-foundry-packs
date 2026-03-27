---
title: Getting Started
description: Install sprite packs from npm and load them in your game engine.
sidebar:
  order: 1
---

Every pack is a standalone npm package. Install only the packs you need — they have no dependencies and no runtime code.

## Install

```bash
# Pick any combination of packs
npm install @sprite-foundry/undead-patrol-48
npm install @sprite-foundry/goblin-warband-48
npm install @sprite-foundry/fantasy-heroes-48
npm install @sprite-foundry/fantasy-villains-48
npm install @sprite-foundry/pirate-raiders-48
```

After install, sprites are available at:

```
node_modules/@sprite-foundry/<pack>/assets/<variant>/<layer>/<direction>.png
```

## Loading sprites

### Node.js / bundler projects

```javascript
const path = require('path');

// Resolve the path to a specific sprite
const sprite = path.resolve(
  'node_modules/@sprite-foundry/fantasy-heroes-48',
  'assets/paladin/albedo/front.png'
);

// Read the manifest for metadata
const manifest = require(
  '@sprite-foundry/fantasy-heroes-48/assets/paladin/manifest.json'
);
console.log(manifest.render_contract.direction_order);
// → ['front','front_left','left','back_left','back','back_right','right','front_right']
```

### Godot 4

Copy the assets into your project's resource directory, then load them as textures:

```gdscript
# Copy pack assets into res://sprites/undead-patrol/ first
var shambler_front = load("res://sprites/undead-patrol/shambler/albedo/front.png")
var shambler_normal = load("res://sprites/undead-patrol/shambler/normal/front.png")

# Apply to a Sprite2D with normal map
$Sprite2D.texture = shambler_front
$Sprite2D.material.normal_map = shambler_normal
```

### Phaser 3

```javascript
// In your preload function
function preload() {
  const variants = ['shambler', 'runner', 'bloater'];
  const directions = ['front', 'front_left', 'left', 'back_left',
                      'back', 'back_right', 'right', 'front_right'];

  for (const v of variants) {
    for (const d of directions) {
      this.load.image(
        `${v}_${d}`,
        `assets/undead-patrol/${v}/albedo/${d}.png`
      );
    }
  }
}
```

### PixiJS

```javascript
import { Assets, Sprite } from 'pixi.js';

const texture = await Assets.load(
  'node_modules/@sprite-foundry/goblin-warband-48/assets/grunt/albedo/front.png'
);
const goblin = new Sprite(texture);
goblin.anchor.set(0.5, 1.0); // center-bottom pivot per manifest
```

## Verify installation

Each pack includes a verify script that checks all assets exist and match their manifests:

```bash
cd node_modules/@sprite-foundry/fantasy-heroes-48
npm run verify
# → All assets verified
```

From the monorepo root, verify all packs at once:

```bash
npm run verify
```

## Next steps

- Browse the [Pack Catalog](/sprite-foundry-packs/handbook/catalog/) for variant details
- Read the [Reference](/sprite-foundry-packs/handbook/reference/) for manifest schema and asset contracts
