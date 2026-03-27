<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.md">English</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/zombie-sprite-pack/readme.png" width="400" alt="Undead Patrol">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/actions"><img src="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.npmjs.com/package/@sprite-foundry/undead-patrol-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/undead-patrol-48" alt="npm version"></a>
  <a href="https://github.com/mcp-tool-shop-org/zombie-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/zombie-sprite-pack/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

Un pacchetto di nemici zombie in pixel art, con risoluzione di 48x48 pixel e 8 direzioni, completo di mappe di albedo, normal map e profondità, per un utilizzo versatile in diversi motori di gioco.

![Banner di Undead Patrol](previews/banner.png)

## Contenuto

8 varianti di zombie, ognuna con 8 angolazioni diverse:

![Disposizione delle varianti](previews/lineup.png)

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Shambler | Zombie base | Postura curva, lenta, malferma |
| Runner | Minaccia veloce | Postura eretta, in avanti, aggressiva |
| Riot Zombie | Carro armato | Spalle larghe, massiccia armatura/scudo |
| Hazmat Zombie | Specialista contaminato | Tuta, cappuccio sferico |
| Bloater | Minaccia ad area | Tronco largo, asimmetria gonfia |
| Skeletal Zombie | Fragile/antico | Arti sottili, aspetto angolare |
| Worker Zombie | Industriale/civile | Uniforme, cintura con attrezzi, equipaggiamento riconoscibile |
| Elite Zombie | Comandante/bruto | Alto, imponente, aspetto massiccio |

Ogni variante include tre livelli di mappa:

- **Albedo** — sprite con colori di base (PNG trasparente)
- **Normal** — normal map per illuminazione dinamica
- **Depth** — depth map per effetti di parallasse e rilievo

## Installazione

```bash
npm install @sprite-foundry/undead-patrol-48
```

## Struttura delle cartelle

```
assets/
  shambler/
    albedo/    8 directional PNGs (front, front_left, left, back_left, back, back_right, right, front_right)
    normal/    8 matching normal maps
    depth/     8 matching depth maps
    preview/   contact sheet
    manifest.json
  runner/
  riot-zombie/
  hazmat-zombie/
  bloater/
  skeletal-zombie/
  worker-zombie/
  elite-zombie/
pack.json          pack-level index
previews/          banner and lineup sheets
```

## Formato del manifest

Ogni variante ha un file `manifest.json`:

```json
{
  "slug": "shambler",
  "name": "Shambler",
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

Il file `pack.json` di livello superiore indicizza tutte le varianti con i percorsi a ciascun manifest.

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
- **Direzioni:** 8 (frontale, fronte-sinistra, sinistra, retro-sinistra, posteriore, retro-destra, destra, fronte-destra)
- **Formato:** PNG trasparente
- **Mappe:** albedo + normal + depth
- **Animazione:** pose statiche (versione 1)
- **Prospettiva:** dall'alto

## Estendere il pacchetto

Vuoi creare varianti di zombie aggiuntive che corrispondano allo stile artistico e al contratto di esportazione di questo pacchetto?

Questo pacchetto è stato creato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), una pipeline di generazione di pixel art open source basata su ComfyUI + SDXL. Il repository di Foundry contiene tutto ciò di cui hai bisogno:

- **Pipeline di generazione** — `pipeline/foundry_gen.py` controlla ComfyUI con configurazioni specifiche per ogni soggetto
- **Configurazioni dei soggetti** — `pipeline/chars/zombie_*.json` definiscono i prompt esatti, i seed, le regole della silhouette e le condizioni di rifiuto per ogni variante in questo pacchetto
- **Manifest batch** — `pipeline/manifests/undead_patrol_01.json` mappa tutte le 8 configurazioni alla struttura di esportazione
- **CLI di esportazione** — `foundry export <run_id>` crea pacchetti deterministici con checksum
- **Tuning di ControlNet** — profondità umanoide, intensità 0.60, end% 0.85 (documentato nel manifest)

Per aggiungere una nuova variante:

1. Crea una configurazione del soggetto in `pipeline/chars/` seguendo le configurazioni zombie esistenti
2. Registra: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Genera: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Rivedi, accetta, genera le mappe, accetta e completa, esporta
5. Copia il pacchetto esportato nella directory corrispondente `assets/<slug>/`

Il [README di Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contiene la guida completa alla pipeline.

## Sicurezza

Questo pacchetto contiene **solo immagini PNG statiche e metadati JSON**. Non sono presenti codice eseguibile, meccanismi di installazione, accesso alla rete né sistemi di telemetria. I file sono di sola lettura per progettazione.

Consultare il file [SECURITY.md](SECURITY.md) per la politica di sicurezza completa.

## Licenza

MIT: utilizzo consentito in progetti commerciali e non commerciali.

## Ringraziamenti

Generato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) utilizzando la pipeline ComfyUI + SDXL per pixel art.

Creato da <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a
