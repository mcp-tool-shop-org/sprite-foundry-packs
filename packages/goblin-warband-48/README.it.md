<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.md">English</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/goblin-sprite-pack/readme.png" width="400" alt="Goblin Warband — Pixel Art Pack" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/goblin-sprite-pack/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/goblin-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/goblin-warband-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/goblin-warband-48" alt="npm" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://mcp-tool-shop-org.github.io/goblin-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-brightgreen" alt="Landing Page" /></a>
</p>

**8 varianti di goblin | 8 direzioni | 3 livelli (albedo + normale + profondità) | pixel art da 48px**

Una collezione di nemici pronta all'uso per giochi di ruolo, giochi di strategia e dungeon crawler. Ogni variante ha una silhouette distintiva: postura, forma della testa, equipaggiamento, percezione della minaccia e massa corporea sono tutti diversi, in modo che i giocatori possano identificare i nemici a colpo d'occhio.

## Varianti

| # | Variante | Ruolo | Silhouette |
|---|---------|------|------------|
| 1 | **Grunt** | Unità di fanteria leggera | Corpo piccolo e curvo, mazza rudimentale |
| 2 | **Archer** | Unità di schermaglia a distanza | Corpo snello, arco corto di grandi dimensioni, faretra |
| 3 | **Shaman** | Incantatore/guaritore | Copricapo con corna, bastone con totem, vestito |
| 4 | **Brute** | Unità di fanteria pesante | Spalle larghe, mascella massiccia, maglio spinato |
| 5 | **Scout** | Unità di fianco veloce | In posizione accovacciata, pugnali doppi, con cappuccio |
| 6 | **Bomber** | Unità di danno ad area | Borsa gonfia, bomba con miccia accesa, occhiali |
| 7 | **Warchief** | Leader d'élite | Elmetto con zanne, asta con stendardo, armatura pesante |
| 8 | **Wolf-Rider** | Unità a cavallo | Goblin su lupo mannaro, struttura corporea unica |

## Installazione

```bash
npm install @sprite-foundry/goblin-warband-48
```

## Utilizzo

```js
const pack = require('@sprite-foundry/goblin-warband-48/pack.json');

// Load a specific variant
const grunt = require('@sprite-foundry/goblin-warband-48/assets/grunt/manifest.json');

// Resolve a sprite path
const albedoPath = grunt.layers.albedo.replace('{direction}', 'front');
// → "albedo/front.png"
```

## Struttura delle cartelle

```
assets/
  grunt/           # Melee fodder — baseline goblin
  archer/          # Ranged skirmisher with shortbow
  shaman/          # Caster with horned headdress + staff
  brute/           # Heavy tank with spiked maul
  scout/           # Fast flanker, crouched + hooded
  bomber/          # AoE threat with bomb + satchel
  warchief/        # Elite leader with banner + armor
  wolf-rider/      # Mounted unit — goblin on dire wolf
    albedo/        # Color sprites (8 directions)
    normal/        # Normal maps (8 directions)
    depth/         # Depth maps (8 directions)
    preview/       # Contact sheet
    manifest.json  # Variant metadata
pack.json          # Pack-level index
```

## Formato del manifest

Ogni variante ha un file `manifest.json`:

```json
{
  "slug": "grunt",
  "name": "Grunt",
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

## Compatibilità con il motore di gioco

Questi sono file PNG standard con metadati JSON: nessuna dipendenza a runtime.

| Motore di gioco | Integrazione |
|--------|------------|
| **Godot 4** | Caricare i PNG come `Texture2D`, utilizzare le normal map su `CanvasTextureMaterial` |
| **Unity** | Importare come sprite, assegnare le normal map al materiale dello sprite |
| **Phaser** | Caricare tramite asset loader, fare riferimento tramite percorso |
| **LÖVE** | `love.graphics.newImage()` per ogni PNG |
| **Raw Canvas** | `drawImage()` con scaling del vicino più prossimo |

Ridimensionare con **interpolazione del vicino più prossimo** per preservare la nitidezza della pixel art.

## Estendere il pacchetto

Questo pacchetto è stato generato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry). Per creare nuove varianti di goblin:

1. Creare un file di configurazione del soggetto in `pipeline/chars/` seguendo lo schema del soggetto di Foundry
2. Bloccare le 5 dimensioni del corpo: **postura, forma della testa, silhouette dell'equipaggiamento, percezione della minaccia, massa corporea**
3. Aggiungere esplicite `reject_conditions` per evitare la convergenza con le varianti esistenti
4. Eseguire: `subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`

Consultare il [README di Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) per la documentazione completa della pipeline.

## Verifica

```bash
npm run verify
```

Verifica che ogni asset referenziato in `pack.json` e nei manifest delle varianti esista sul disco.

## Sicurezza e modello di minaccia

Questo pacchetto contiene **solo immagini PNG statiche e metadati JSON**. Non contiene:

- Codice eseguibile, script o binari
- Hook di installazione o script di post-installazione
- Accesso alla rete o telemetria
- Scritture sul file system

Consultare [SECURITY.md](./SECURITY.md) per la politica di sicurezza completa.

## Licenza

[MIT](./LICENSE)

---

Creato da <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
