<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.md">English</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/fantasy-heroes-sprite-pack/readme.png" width="400" alt="Fantasy Heroes" />
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/fantasy-heroes-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/fantasy-heroes-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/fantasy-heroes-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/fantasy-heroes-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/fantasy-heroes-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://mcp-tool-shop-org.github.io/fantasy-heroes-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page" /></a>
</p>

Un ensemble de héros en pixel art de 48x48 pixels, avec 8 directions, comprenant des cartes d'albédo, de normales et de profondeur pour une utilisation dans les jeux, compatible avec tous les moteurs.

![Bannière des Héros Fantastiques](previews/banner.png)

## Contenu

8 archétypes de héros formant une équipe d'aventuriers complète :

![Composition Variée](previews/lineup.png)

| Variante | Rôle | Silhouette |
|---------|------|------------|
| Guerrier | Combattant polyvalent en première ligne | Épée + bouclier, armure équilibrée |
| Rôdeur | Attaquant à distance | Arc, cape, silhouette légère |
| Mage | Lanceur de sorts | Bâton, robe, silhouette magique |
| Voleur | Flanc | Capuche, armure légère, dagues, posture agile |
| Clerc | Guérisseur/support | Massue à flanges, bouclier avec emblème solaire, vêtements sacrés |
| Barbare | Dégâts importants | Arme massive, corps large, fourrure/cuir |
| Paladin | Tank d'élite | Armure complète, bouclier en forme de cerf-volant, marteau de guerre, cape |
| Moine | Spécialiste rapide | Sans armure, bandages, bâton, silhouette disciplinée |

Chaque variante est fournie avec trois couches de carte :

- **Albédo** — sprites de couleur de base (PNG transparent)
- **Normal** — cartes de normales pour l'éclairage dynamique
- **Profondeur** — cartes de profondeur pour les effets de parallaxe et de relief

## Installation

```bash
npm install @sprite-foundry/fantasy-heroes-48
```

## Structure des dossiers

```
assets/
  fighter/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  ranger/
  mage/
  rogue/
  cleric/
  barbarian/
  paladin/
  monk/
pack.json          pack-level index
previews/          banner and lineup sheets
```

## Format du manifeste

Chaque variante possède un fichier `manifest.json` :

```json
{
  "slug": "fighter",
  "name": "Fighter",
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

Le fichier `pack.json` au niveau du pack indexe toutes les variantes avec les chemins vers chaque manifeste.

## Compatibilité avec les moteurs

Ce sont des fichiers PNG simples avec des métadonnées JSON. Ils fonctionnent avec n'importe quel moteur ou framework capable de charger des images :

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Moteurs personnalisés

Pas de format spécifique au moteur ni de dépendance d'exécution.

## Spécifications

- **Taille de la tuile :** 48 x 48 pixels
- **Directions :** 8 (avant, avant_gauche, gauche, arrière_gauche, arrière, arrière_droite, droite, avant_droite)
- **Format :** PNG transparent
- **Cartes :** albédo + normal + profondeur
- **Animation :** poses statiques (v1)
- **Perspective :** vue de dessus

## Extension du pack

Souhaitez-vous générer des variantes de héros supplémentaires qui correspondent au style artistique et au contrat d'exportation de ce pack ?

Ce pack a été créé avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), une pipeline de génération de pixel art open source basée sur ComfyUI + SDXL. Le dépôt de Foundry contient tout ce dont vous avez besoin :

- **Pipeline de génération** — `pipeline/foundry_gen.py` contrôle ComfyUI avec des configurations spécifiques à chaque sujet
- **Configurations des sujets** — `pipeline/chars/hero_*.json` définissent les invites exactes, les graines, les règles de silhouette et les conditions de rejet pour chaque variante de ce pack
- **Manifeste par lot** — `pipeline/manifests/fantasy_heroes_03.json` associe les 8 configurations à la structure d'exportation
- **CLI d'exportation** — `foundry export <run_id>` crée des packs déterministes avec des sommes de contrôle
- **Réglage de ControlNet** — force de profondeur humanoïde 0,60, fin% 0,85 (documenté dans le manifeste)

Pour ajouter une nouvelle variante :

1. Créez une configuration de sujet dans `pipeline/chars/` en suivant les configurations de héros existantes
2. Enregistrez : `python -m foundry.cli subject-add <id> --name "Nom"`
3. Générez : `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Examinez, acceptez, créez les cartes, acceptez la finalisation, exportez
5. Copiez le pack exporté dans le répertoire correspondant `assets/<slug>/`

La documentation [README de Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contient la description complète du pipeline.

## Sécurité

Ce paquet contient **uniquement des images PNG statiques et des métadonnées JSON**. Il ne contient aucun code exécutable, aucun script d'installation, aucun accès réseau et aucune télémétrie. Les ressources sont en lecture seule par conception.

Consultez le fichier [SECURITY.md](SECURITY.md) pour la politique de sécurité complète.

## Licence

MIT — utilisation autorisée dans les projets commerciaux et non commerciaux.

## Crédits

Généré avec [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) en utilisant le pipeline ComfyUI + SDXL pour l'art pixelisé.

Créé par <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a
