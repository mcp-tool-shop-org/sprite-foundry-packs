<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.md">English</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

Un pacchetto di eroi in pixel art, con risoluzione di 48px e 8 direzioni, completo di mappe di albedo, normali e di profondità, per un utilizzo versatile in diversi motori di gioco.

![Banner di Eroi Fantasy](previews/banner.png)

## Cosa è incluso

8 archetipi di eroi che formano un gruppo di avventurieri completo:

![Disposizione delle Varianti](previews/lineup.png)

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Guerriero | Combattente versatile in prima linea | Spada + scudo, armatura bilanciata |
| Arciere | Attaccante a distanza | Arco, mantello, silhouette più leggera |
| Mago | Incantatore | Bastone, veste, silhouette magica |
| Ladro | Incursor | Cappuccio, armatura leggera, pugnali, postura agile |
| Chierico | Guaritore/supporto | Mazza con flange, scudo con emblema solare, vesti |
| Barbaro | Danno elevato | Arma pesante, corpo superiore ampio, pelliccia/pelle |
| Paladino | Serbatoio d'élite | Armatura completa, scudo a forma di aquilone, martello da guerra, mantello |
| Monaco | Specialista veloce | Senza armatura, bende, bastone, silhouette disciplinata |

Ogni variante include tre livelli di mappa:

- **Albedo** — sprite con colori di base (PNG trasparente)
- **Normal** — mappe normali per l'illuminazione dinamica
- **Depth** — mappe di profondità per effetti di parallasse e rilievo

## Installazione

```bash
npm install @sprite-foundry/fantasy-heroes-48
```

## Struttura delle cartelle

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

## Formato del manifest

Ogni variante ha un file `manifest.json`:

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

Il file `pack.json` di livello superiore indicizza tutte le varianti con i percorsi di ciascun manifest.

## Compatibilità con i motori di gioco

Questi sono file PNG semplici con metadati JSON. Funzionano con qualsiasi motore o framework in grado di caricare immagini:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Motori personalizzati

Nessun formato specifico per il motore o dipendenza di runtime.

## Specifiche

- **Dimensione della tessera:** 48 x 48 px
- **Direzioni:** 8 (frontale, fronte-sinistra, sinistra, retro-sinistra, retro, retro-destra, destra, fronte-destra)
- **Formato:** PNG trasparente
- **Mappe:** albedo + normali + profondità
- **Animazione:** pose statiche (v1)
- **Prospettiva:** dall'alto

## Estendere il pacchetto

Vuoi generare varianti di eroi aggiuntive che corrispondano allo stile artistico e al contratto di esportazione di questo pacchetto?

Questo pacchetto è stato creato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), una pipeline di generazione di pixel art open source basata su ComfyUI + SDXL. Il repository di Foundry contiene tutto ciò di cui hai bisogno:

- **Pipeline di generazione** — `pipeline/foundry_gen.py` controlla ComfyUI con configurazioni specifiche per ogni soggetto
- **Configurazioni dei soggetti** — `pipeline/chars/hero_*.json` definiscono i prompt esatti, i seed, le regole della silhouette e le condizioni di rifiuto per ogni variante in questo pacchetto
- **Manifest batch** — `pipeline/manifests/fantasy_heroes_03.json` mappa tutte le 8 configurazioni alla struttura di esportazione
- **CLI di esportazione** — `foundry export <run_id>` crea pacchetti deterministici con checksum
- **Tuning di ControlNet** — profondità umanoide, intensità 0.60, fine% 0.85 (documentato nel manifest)

Per aggiungere una nuova variante:

1. Crea una configurazione del soggetto in `pipeline/chars/` seguendo le configurazioni degli eroi esistenti
2. Registra: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Genera: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Rivedi, accetta, genera le mappe, accetta la finalizzazione, esporta
5. Copia il pacchetto esportato nella directory corrispondente `assets/<slug>/`

Il [README di Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contiene la guida completa alla pipeline.

## Sicurezza

Questo pacchetto contiene **solo immagini PNG statiche e metadati JSON**. Non contiene codice eseguibile, né meccanismi di installazione, accesso alla rete o telemetria. I file sono di sola lettura per progettazione.

Consultare il file [SECURITY.md](SECURITY.md) per la politica di sicurezza completa.

## Licenza

MIT: utilizzo consentito in progetti commerciali e non commerciali.

## Ringraziamenti

Generato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) utilizzando la pipeline ComfyUI + SDXL per pixel art.

Creato da <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
