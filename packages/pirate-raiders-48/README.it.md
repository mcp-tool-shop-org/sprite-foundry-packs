<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.md">English</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

Un pacchetto di personaggi marittimi in pixel art, con risoluzione di 48px e 8 direzioni, completo di mappe di albedo, normali e profondità, per un utilizzo versatile in diversi motori di gioco. **Pacchetto 05** nel catalogo di [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry).

## Contenuto

8 archetipi di pirati, che coprono diversi aspetti del mondo marittimo:

| Variante | Ruolo | Aspetto |
|---------|------|------------|
| Capitano | Comandante | Cappello a tricorno, cappotto blu con bordi dorati, spada ricurva all'anca |
| Ufficiale di bordo | Logistica / disciplina | Cappello di pelle con ampia tesa, corporatura robusta, braccia incrociate, portachiavi alla cintura |
| Assaltatore | Combattimento corpo a corpo | Fascia rossa, gilet senza maniche, due spade ricurve per l'abbordaggio |
| Duellante con pistola | Specialista a distanza | Lungo cappotto bordeaux, pistola a pietra, bandoliera per munizioni |
| Marinaio | Autorità militare | Uniforme blu e bianca, cappello a tricorno, spalline, postura militare impeccabile |
| Governatore del porto | Autorità civile | Lungo cappotto formale color prugna, parrucca impolverata, corporatura robusta, bastone da passeggio |
| Guardiano dei morti | Marittimo non morto | Pelle verde e umida, cappotto strappato, corazza di ferro arrugginita, cirripedi |
| Sacerdote marino | Mistico / supporto | Copricapo a forma di ramo di corallo, veste multistrato color turchese, incensiere con cirripedi appesi a una catena |

Ogni variante include tre livelli di mappa:

- **Albedo** — sprite con colori di base (PNG trasparente)
- **Normal** — mappe normali per l'illuminazione dinamica
- **Depth** — mappe di profondità per effetti di parallasse e rilievo

## Installazione

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## Struttura delle cartelle

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

## Formato del manifest

Ogni variante contiene un file `manifest.json` con informazioni dettagliate e checksum SHA-256:

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

Il file `pack.json` a livello di pacchetto contiene un indice di tutte le varianti, con i percorsi a ciascun manifest.

## Compatibilità con i motori di gioco

Questi sono file PNG semplici con metadati JSON. Funzionano con qualsiasi motore o framework in grado di caricare immagini:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Motori personalizzati

Nessun formato specifico per il motore o dipendenza in fase di runtime.

## Specifiche

- **Dimensione della tile:** 48 x 48 px
- **Direzioni:** 8 (fronte, fronte-sinistra, sinistra, retro-sinistra, retro, retro-destra, destra, fronte-destra)
- **Formato:** PNG trasparente
- **Mappe:** albedo + normali + profondità
- **Animazione:** pose statiche (versione 1)
- **Prospettiva:** dall'alto

## Estendere il pacchetto

Vuoi creare varianti di pirati aggiuntive che si abbinino allo stile artistico e al contratto di esportazione di questo pacchetto?

Questo pacchetto è stato creato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), una pipeline di generazione di pixel art open source basata su ComfyUI + SDXL. Il repository di Foundry contiene tutto ciò di cui hai bisogno:

- **Pipeline di generazione** — `pipeline/foundry_gen.py` controlla ComfyUI con configurazioni specifiche per ogni soggetto
- **Configurazioni dei soggetti** — `pipeline/chars/pirate_*.json` definiscono i prompt esatti, i seed e le regole di silhouette per ogni variante in questo pacchetto
- **CLI di esportazione** — `foundry export <run_id>` crea pacchetti deterministici con checksum

Per aggiungere una nuova variante:

1. Crea una configurazione del soggetto in `pipeline/chars/` seguendo le configurazioni dei pirati esistenti
2. Registra: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Genera: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Rivedi, accetta, genera le mappe, accetta e finalizza, esporta
5. Copia il pacchetto esportato nella directory corrispondente `assets/<slug>/`

Il file README di [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contiene una descrizione dettagliata dell'intero processo.

## Sicurezza

Questo pacchetto contiene **solo immagini PNG statiche e metadati JSON**. Non contiene codice eseguibile, né meccanismi di installazione, accesso alla rete o telemetria. I file sono progettati per essere di sola lettura.

Consultare il file [SECURITY.md](SECURITY.md) per la politica di sicurezza completa.

## Licenza

MIT: può essere utilizzato in progetti commerciali e non commerciali.

## Ringraziamenti

Generato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) utilizzando la pipeline ComfyUI + SDXL per pixel art.

Creato da <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a
