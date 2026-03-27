<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.md">English</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/pirate-raiders-sprite-pack/readme.png" width="400" alt="Pirate Raiders" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/pirate-raiders-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/pirate-raiders-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/pirate-raiders-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/pirate-raiders-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/pirate-raiders-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://mcp-tool-shop-org.github.io/pirate-raiders-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page" /></a>
</p>

Un ensemble de personnages maritimes en pixel art, de 48 pixels de résolution, avec 8 directions possibles, et incluant des cartes d'albédo, de normales et de profondeur, pour une utilisation dans des jeux compatibles avec différents moteurs. **Pack 05** dans le catalogue de [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry).

## Ce qui est inclus

8 archétypes de pirates, regroupés en trois catégories visuelles qui couvrent le monde maritime :

| Variante | Rôle | Silhouette. |
|---------|------|------------|
| Capitaine. | Commandant | Chapeau tricorne, manteau bleu marine avec ornements dorés, sabre richement décoré à la ceinture. |
| Intendant. | Logistique / discipline | Chapeau en cuir à larges bords, corpulence robuste, bras croisés, porte-clés attaché à la ceinture. |
| Frontière impitoyable. | Assaut au corps à corps | Bandana rouge, gilet sans manches, deux sabres de abord courbés. |
| Duelliste au pistolet. | Spécialiste à distance | Long manteau bordeaux ajusté, pistolet à silex, bandoulière pour munitions. |
| Marin de la marine. | Autorité militaire | Uniform bleu et blanc, bicorne, ceintures croisées, posture militaire impeccable. |
| Gouverneur du port. | Autorité civile | Manteau formel prune, perruque poudrée, corpulence robuste, canne. |
| Gardien noyé. | Marins morts-vivants | Peau verdâtre et gorgée d'eau, manteau déchiré, plastron de fer rouillé, crustacés. |
| Prêtre de la mer. | Mystique / soutien | Headdress en forme de corail, robe à plusieurs couches de couleur turquoise, encensoir en forme de bourrelet suspendu à une chaîne. |

Chaque version est livrée avec trois couches de cartes :

- **Albédo** : textures de base (fichiers PNG transparents).
- **Normal** : cartes de normales pour l'éclairage dynamique.
- **Profondeur** : cartes de profondeur pour les effets de parallaxe et de relief.

## Installation

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## Structure des dossiers

```
assets/
  captain/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  quartermaster/
  cutthroat/
  pistoleer/
  navy-sailor/
  governor/
  drowned/
  sea-priest/
pack.json          pack-level index
previews/          contact sheets per variant
```

## Format de la manifestation

Chaque variante est accompagnée d'un fichier `manifest.json` qui contient toutes les informations sur son origine, ainsi que les sommes de contrôle SHA-256.

```json
{
  "schema_version": "1.0.0",
  "identity": { "subject_slug": "pirate_captain", "display_name": "Captain" },
  "render_contract": {
    "width": 48, "height": 48,
    "direction_order": ["front", "front_left", "left", "back_left", "back", "back_right", "right", "front_right"],
    "pivot": "center_bottom",
    "transparency": true
  },
  "files": { "albedo/front.png": "<sha256>", "normal/front.png": "<sha256>", "..." : "..." }
}
```

Le fichier `pack.json` au niveau du paquet indexe toutes les variantes et indique le chemin d'accès à chaque fichier de manifeste.

## Compatibilité des moteurs

Ce sont des fichiers PNG simples, accompagnés de métadonnées au format JSON. Ils sont compatibles avec n'importe quel moteur ou framework capable de charger des images.

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Moteurs personnalisés

Pas de format spécifique à un moteur ni de dépendance à l'exécution.

## Spécifications

- **Taille des tuiles :** 48 x 48 pixels
- **Orientations :** 8 (avant, avant_gauche, gauche, arrière_gauche, arrière, arrière_droite, droite, avant_droite)
- **Format :** PNG transparent
- **Cartes :** albédo + normale + profondeur
- **Animation :** poses statiques (version 1)
- **Perspective :** vue de dessus.

## Étendre le pack

Souhaitez-vous générer d'autres variantes de pirates qui correspondent au style artistique et aux conditions contractuelles de ce pack ?

Ce pack a été créé avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), une chaîne de génération de pixel art open source pour ComfyUI + SDXL. Le dépôt de Sprite Foundry contient tout ce dont vous avez besoin :

- **Génération par lot** — Le script `pipeline/foundry_gen.py` contrôle ComfyUI et utilise des configurations spécifiques pour chaque sujet.
- **Configurations des sujets** — Les fichiers `pipeline/chars/pirate_*.json` définissent les invites, les valeurs de départ (seeds) et les règles de silhouette exactes pour chaque variante de ce pack.
- **Interface en ligne de commande pour l'exportation** — La commande `foundry export <run_id>` génère des packs reproductibles avec des sommes de contrôle (checksums).

Pour ajouter une nouvelle variante :

1. Créez un fichier de configuration pour le sujet dans le répertoire `pipeline/chars/`, en suivant les exemples de configurations existantes pour les pirates.
2. Enregistrez : `python -m foundry.cli subject-add <id> --name "Nom"`
3. Générez : `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Vérifiez, validez, créez les cartes, validez la finalisation, exportez.
5. Copiez le paquet exporté dans le répertoire correspondant `assets/<slug>/`.

Le fichier README de [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contient une description détaillée de l'ensemble du processus.

## Sécurité

Ce paquet contient **uniquement des images PNG statiques et des métadonnées au format JSON**. Il ne contient aucun code exécutable, aucun mécanisme d'installation, aucun accès réseau et aucune collecte de données. Les ressources sont conçues pour être en lecture seule.

Consultez le fichier [SECURITY.md](SECURITY.md) pour connaître la politique de sécurité complète.

## Licence

MIT — utilisation autorisée dans les projets commerciaux et non commerciaux.

## Crédits

Généré avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) en utilisant le pipeline ComfyUI + SDXL pour l'art pixel.

Créé par <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
