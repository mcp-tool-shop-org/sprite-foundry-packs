<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.md">English</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/monster-pack/readme.png" width="400" alt="Monster Pack" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/monster-pack-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/monster-pack-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/monster-pack-48/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

Un bestiario di mostri in pixel art, con 16 varianti e 6 classi di corpo, risoluzione 48x48 pixel, con mappe di albedo, normali e profondità, per un utilizzo indipendente dal motore di gioco.

![Banner del Pacchetto di Mostri](previews/banner.png)

## Cosa è incluso

16 varianti di mostri, suddivise in 6 classi di corpo:

![Disposizione delle Varianti](previews/lineup.png)

### Umanoide

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Guardiano delle Campane | Malattia / negazione dell'area | Figura avvolta in una tunica, con una campana pesante, catene, tonalità ramate |
| Cavaliere Oscuro | Combattimento corpo a corpo di élite | Armatura vuota, spada, simbolo a forma di teschio |
| Collezionista di Denti | Ladro / saccheggiatore | Simile a un goblin, con un sorriso che mostra denti sproporzionati, lungo cappotto |

### Alto/Sottile

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Ombra di Inchiostro | Furtività / assassino | Figura allungata e scura, con arti che gocciolano inchiostro |
| Pescatore Lanterna | Esca / predatore in agguato | Esca bioluminescente, pelle traslucida, denti a spillo |
| Inseguace dello Specchio | Riflesso / contrattacco | Superficie riflettente, schegge di cristallo, arti affilati |
| Marionetta delle Radici | Parassita / controllo | Cadavere animato da radici parassite, gambe simili a corteccia |
| Cantante della Gola | Sonico / controllo della folla | Scheletro, costole esposte, mantello scuro |

### Largo/Basso

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Golem dell'Orologio | Serbatoio pesante | Costruzione meccanica, torso con ingranaggi, arti pesanti |
| Idolo Sorridente | Pericolo ambientale | Totem di pietra animato, sorriso scolpito, ricoperto di muschio |
| Custode dell'Alveare | Invocatore di sciami | Insettoide gigante, placche di chitina, occhi composti |

### Amorfo

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Spettro di Fango | Inseguimento lento | Figura di argilla che gocciola, occhi simili a braci, sudario |
| Re dei Ratti | Boss a sciami | Massa fusa di ratti, code nodose, molti occhi |
| Madre delle Spore | AoE / debuff | Massa fungina, corona a forma di cappello di fungo, nube di spore |

### Artropode

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Tessitore di Ossa | Trappola / agguato | Ragno costruito con ossa rubate, testa a forma di teschio |

### Alato

| Variante | Ruolo | Silhouette |
|---------|------|------------|
| Drago | Boss volante | Drago bipede, ali da pipistrello, coda spinosa |

Ogni variante viene fornita con tre livelli di mappa:

- **Albedo** — sprite del colore di base (PNG trasparente)
- **Normal** — mappe normali per l'illuminazione dinamica
- **Depth** — mappe di profondità per effetti di parallasse e elevazione

## Installazione

```bash
npm install @sprite-foundry/monster-pack-48
```

## Struttura delle cartelle

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

## Formato del manifest

Ogni variante ha un file `manifest.json`:

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

Il file `pack.json` di livello superiore indicizza tutte le varianti con i percorsi di ciascun manifest e include i metadati `bodyClass`.

## Compatibilità con il motore

Questi sono file PNG semplici con metadati JSON. Funzionano con qualsiasi motore o framework in grado di caricare immagini:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Motori personalizzati

Nessun formato specifico per il motore o dipendenza di runtime.

## Specifiche

- **Varianti:** 16 mostri
- **Classi di corpo:** 6 (umanoide, alto/sottile, largo/basso, amorfo, artropode, alato)
- **Dimensione delle piastrelle:** 48 x 48 px
- **Direzioni:** 8 (frontale, fronte-sinistra, sinistra, retro-sinistra, retro, retro-destra, destra, fronte-destra)
- **Sprite totali:** 384 (16 x 8 x 3)
- **Formato:** PNG trasparente
- **Mappe:** albedo + normali + profondità
- **Animazione:** pose statiche (v1)
- **Prospettiva:** dall'alto

## Estendere il pacchetto

Desiderate generare varianti di mostri aggiuntive che corrispondano allo stile artistico e al contratto di questo pacchetto?

Questo pacchetto è stato creato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), una pipeline open-source di generazione di pixel art basata su ComfyUI + SDXL. I mostri non umanoidi utilizzano la **"corsia dei mostri"**, ovvero guide di profondità ControlNet specifiche per la classe del corpo, che impongono forme corporee insolite senza forzare uno scheletro umano. Il repository di Foundry contiene tutto ciò di cui avete bisogno:

- **Pipeline di generazione** — `pipeline/foundry_gen.py` controlla ComfyUI con configurazioni specifiche per ogni soggetto.
- **Configurazioni dei soggetti** — `pipeline/chars/beast_*.json` definiscono i prompt, i seed e la classe del corpo esatti per ogni variante in questo pacchetto.
- **Generatori di profondità** — `pipeline/morph_refs/gen_amorphous_depth.py`, `gen_wide_squat_depth.py`, `gen_tall_thin_depth.py`
- **Preset delle classi di corpo** — selezione automatica della forza e della temporizzazione di ControlNet per ogni tipo di creatura.
- **Interfaccia a riga di comando per l'esportazione** — `foundry export <run_id>` crea pacchetti deterministici con checksum.

Per aggiungere una nuova variante:

1. Create una configurazione del soggetto in `pipeline/chars/` seguendo le configurazioni esistenti per i mostri.
2. Registrate: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Generate: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Verificate, accettate, create le mappe, accettate la finalizzazione, esportate.
5. Copiate il pacchetto esportato nella directory corrispondente `assets/<slug>/`.

Il [README di Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contiene una descrizione dettagliata dell'intera pipeline.

## Sicurezza

Questo pacchetto contiene **solo immagini PNG statiche e metadati JSON**. Non contiene codice eseguibile, hook di installazione, accesso alla rete o telemetria. Gli asset sono di sola lettura per progettazione.

Consultate [SECURITY.md](SECURITY.md) per la politica di sicurezza completa.

## Licenza

MIT — utilizzabile in progetti commerciali e non commerciali.

## Crediti

Generato con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) utilizzando la pipeline di pixel art ComfyUI + SDXL.

Creato da <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
