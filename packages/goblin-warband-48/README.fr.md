<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.md">English</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

**8 variantes de gobelins | 8 directions | 3 couches (albédo + normal + profondeur) | Pixel art de 48px**

Un ensemble d'ennemis prêt à l'emploi pour les RPG, les jeux de stratégie et les jeux d'exploration de donjons. Chaque variante a une silhouette distincte : la posture, la forme de la tête, l'équipement, l'apparence menaçante et la masse corporelle sont tous différents, ce qui permet aux joueurs d'identifier les ennemis en un coup d'œil.

## Variantes

| # | Variante | Rôle | Silhouette |
|---|---------|------|------------|
| 1 | **Grunt** | Combattant de mêlée | Corps petit et voûté, club rudimentaire |
| 2 | **Archer** | Combattant à distance | Corps mince, arc court de grande taille, carquasse |
| 3 | **Shaman** | Lanceur de sorts/soigneur | Headdress orné de cornes, bâton avec totem, vêtement ample |
| 4 | **Brute** | Tank de mêlée lourd | Épaules larges, mâchoire massive, masse d'armes cloutée |
| 5 | **Scout** | Flanc rapide | Corps accroupi, deux dagues, capuche |
| 6 | **Bomber** | Menace de zone | Sac volumineux, bombe avec fusible allumé, lunettes |
| 7 | **Warchief** | Chef d'élite | Casque avec des défenses, hampe de drapeau, armure lourde |
| 8 | **Wolf-Rider** | Unité montée | Gobelin sur loup sauvage, plan corporel unique |

## Installation

```bash
npm install @sprite-foundry/goblin-warband-48
```

## Utilisation

```js
const pack = require('@sprite-foundry/goblin-warband-48/pack.json');

// Load a specific variant
const grunt = require('@sprite-foundry/goblin-warband-48/assets/grunt/manifest.json');

// Resolve a sprite path
const albedoPath = grunt.layers.albedo.replace('{direction}', 'front');
// → "albedo/front.png"
```

## Structure des dossiers

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

## Format du manifeste

Chaque variante possède un fichier `manifest.json` :

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

## Compatibilité avec les moteurs

Il s'agit de fichiers PNG standard avec des métadonnées JSON – aucune dépendance d'exécution.

| Moteur | Intégration |
|--------|------------|
| **Godot 4** | Chargez les PNG en tant que `Texture2D`, utilisez les cartes normales sur `CanvasTextureMaterial`. |
| **Unity** | Importez en tant que sprites, attribuez les cartes normales au matériau du sprite. |
| **Phaser** | Chargez via le chargeur d'actifs, référez-vous par chemin. |
| **LÖVE** | `love.graphics.newImage()` pour chaque PNG. |
| **Raw Canvas** | `drawImage()` avec mise à l'échelle par le plus proche voisin. |

Augmentez la résolution avec une **interpolation par le plus proche voisin** pour préserver la netteté du pixel art.

## Extension du pack

Ce pack a été généré avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry). Pour créer de nouvelles variantes de gobelins :

1. Créez une configuration de sujet dans `pipeline/chars/` en suivant le schéma de sujet de Foundry.
2. Fixez les 5 dimensions du corps : **posture, forme de la tête, silhouette de l'équipement, apparence menaçante, masse corporelle**.
3. Ajoutez des `reject_conditions` explicites pour éviter la convergence avec les variantes existantes.
4. Exécutez : `subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`.

Consultez la documentation complète du pipeline dans le [README de Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry).

## Vérification

```bash
npm run verify
```

Vérifie que chaque ressource référencée dans `pack.json` et les manifestes des variantes existe sur le disque.

## Sécurité et modèle de menace

Ce paquet contient **uniquement des images PNG statiques et des métadonnées JSON**. Il ne contient pas :

- De code exécutable, de scripts ou de binaires
- D'hooks d'installation ou de scripts post-installation
- D'accès réseau ou de télémétrie
- D'écritures sur le système de fichiers

Consultez [SECURITY.md](./SECURITY.md) pour la politique de sécurité complète.

## Licence

[MIT](./LICENSE)

---

Créé par <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
