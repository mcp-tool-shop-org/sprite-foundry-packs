<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.md">English</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/monster-pack/readme.png" width="400" alt="Monster Pack" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/monster-pack-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/monster-pack-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/monster-pack-48/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

Un bestiaire de monstres en pixel art de 48x48 pixels, avec 8 directions, incluant les cartes d'albédo, de normales et de profondeur, pour une utilisation dans les jeux, quel que soit le moteur utilisé.

![Bannière du pack de monstres](previews/banner.png)

## Contenu

16 variantes de monstres répartis en 6 classes de corps :

![Présentation des variantes](previews/lineup.png)

### Humanoïde

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Gardien de cloche | Malédiction / restriction de zone | Figure en robe avec une grande cloche, des chaînes, des tons cuivrés |
| Chevalier spectral | Combat rapproché d'élite | Armure vide, épée, symbole de crâne |
| Collectionneur de dents | Voleur / récupérateur | Ressemble à un gobelin, grand sourire avec des dents disproportionnées, long manteau |

### Grand/Mince

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Ombre d'encre | Discrétion / assassin | Figure sombre et allongée, membres dégoulinant d'encre |
| Pêcheur de lanterne | Appât / prédateur en embuscade | Appât bioluminescent, peau translucide, dents acérées |
| Espion miroir | Réflexion / contre-attaque | Surface réfléchissante, éclats de cristal, membres acérés |
| Marionnette de racines | Parasite / contrôle | Cadavre animé par des racines parasites, jambes en écorce |
| Chantre de la gorge | Sonique / contrôle de foule | Squelette, cage thoracique exposée, longue cape sombre |

### Large/Bas

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Golem de l'horloge | Tank lourd | Construction mécanique, torse avec des engrenages, membres massifs |
| Idole souriante | Danger environnemental | Totem de pierre animé, sourire sculpté, recouvert de mousse |
| Gardien du nid | Invocateur de nuées | Insectoïde géant, plaques de chitine, yeux composés |

### Amorphe

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Spectre de boue | Poursuite lente | Figure de boue dégoulinante, yeux en braise, linceul funéraire |
| Roi des rats | Boss de nuée | Masse de rats fusionnés, queues nouées, nombreux yeux |
| Mère des spores | Effet de zone / debuff | Masse fongique, couronne de champignon, nuage de spores |

### Artropode

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Tisseur d'os | Piège / embuscade | Araignée construite à partir d'os volés, tête de crâne |

### Ailé

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Wyverne | Boss volant | Dragon à deux pattes, ailes de chauve-souris, queue épineuse |

Chaque variante est fournie avec trois calques de carte :

- **Albédo** — sprites de couleur de base (PNG transparent)
- **Normal** — cartes de normales pour un éclairage dynamique
- **Profondeur** — cartes de profondeur pour les effets de parallaxe et de relief

## Installation

```bash
npm install @sprite-foundry/monster-pack-48
```

## Structure des dossiers

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

## Format du manifeste

Chaque variante possède un fichier `manifest.json` :

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

Le fichier `pack.json` de niveau pack indexe toutes les variantes avec les chemins vers chaque manifeste et inclut les métadonnées `bodyClass`.

## Compatibilité moteur

Il s'agit de fichiers PNG simples avec des métadonnées JSON. Ils fonctionnent avec n'importe quel moteur ou framework capable de charger des images :

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Moteurs personnalisés

Pas de format spécifique au moteur ni de dépendance d'exécution.

## Spécifications

- **Variantes :** 16 monstres
- **Classes de corps :** 6 (humanoïde, grand/mince, large/bas, amorphe, artropode, ailé)
- **Taille des tuiles :** 48 x 48 pixels
- **Directions :** 8 (avant, avant_gauche, gauche, arrière_gauche, arrière, arrière_droit, droite, avant_droit)
- **Nombre total de sprites :** 384 (16 x 8 x 3)
- **Format :** PNG transparent
- **Cartes :** albédo + normal + profondeur
- **Animation :** poses statiques (v1)
- **Perspective :** vue de dessus

## Extension du pack

Souhaitez-vous générer des variantes de monstres supplémentaires qui correspondent au style artistique et au contrat d'exportation de ce pack ?

Ce pack a été créé avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), une chaîne de génération de pixel art open source basée sur ComfyUI + SDXL. Les monstres non humanoïdes utilisent la **voie des monstres** — des guides de profondeur ControlNet spécifiques à chaque type de corps, qui permettent des formes corporelles exotiques sans imposer un squelette humain. Le dépôt de Sprite Foundry contient tout ce dont vous avez besoin :

- **Chaîne de génération** — `pipeline/foundry_gen.py` contrôle ComfyUI avec des configurations spécifiques à chaque sujet.
- **Configurations des sujets** — `pipeline/chars/beast_*.json` définissent les invites, les graines et le type de corps exact pour chaque variante de ce pack.
- **Générateurs de profondeur** — `pipeline/morph_refs/gen_amorphous_depth.py`, `gen_wide_squat_depth.py`, `gen_tall_thin_depth.py`
- **Préconfigurations des types de corps** — sélection automatique de la force et du timing de ControlNet en fonction du type de créature.
- **Interface de ligne de commande d'exportation** — `foundry export <run_id>` crée des packs déterministes avec des sommes de contrôle.

Pour ajouter une nouvelle variante :

1. Créez une configuration de sujet dans `pipeline/chars/` en suivant les configurations de monstres existantes.
2. Enregistrez : `python -m foundry.cli subject-add <id> --name "Nom"`
3. Générez : `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Vérifiez, acceptez, générez les cartes, acceptez la finalisation, exportez.
5. Copiez le pack exporté dans le répertoire correspondant `assets/<slug>/`.

Le fichier [README de Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contient une description complète de la chaîne de génération.

## Sécurité

Ce paquet contient **uniquement des images PNG statiques et des métadonnées JSON**. Il ne contient aucun code exécutable, aucun hook d'installation, aucun accès réseau et aucune télémétrie. Les ressources sont en lecture seule par conception.

Consultez le fichier [SECURITY.md](SECURITY.md) pour connaître la politique de sécurité complète.

## Licence

MIT — utilisation autorisée dans les projets commerciaux et non commerciaux.

## Crédits

Généré avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) en utilisant la chaîne de génération de pixel art ComfyUI + SDXL.

Créé par <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
