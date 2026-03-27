<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.md">English</a>
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

**8 variações de goblins | 8 direções | 3 camadas (albedo + normal + profundidade) | Arte em pixel de 48px**

Um conjunto de inimigos pronto para usar em RPGs, jogos de estratégia e jogos de exploração de masmorras. Cada variação tem um perfil distinto — a postura, o formato da cabeça, o equipamento, a ameaça percebida e a massa corporal são diferentes, para que os jogadores possam identificar os inimigos de relance.

## Variações

| # | Variação | Função | Perfil |
|---|---------|------|------------|
| 1 | **Grunt** | Unidade de combate corpo a corpo | Corpo pequeno e curvado, clava grosseira. |
| 2 | **Archer** | Unidade de ataque à distância | Corpo esguio, arco curto grande, aljava. |
| 3 | **Shaman** | Lançador/curador | Adorno de chifres, cajado com totem, vestido. |
| 4 | **Brute** | Tanque de combate corpo a corpo | Ombros largos, mandíbula massiva, machado com espinhos. |
| 5 | **Scout** | Unidade de flanco rápida | Corpo abaixado, duas adagas, capuz. |
| 6 | **Bomber** | Ameaça de área (AoE) | Bolsa volumosa, bomba com pavio aceso, óculos. |
| 7 | **Warchief** | Líder de elite | Capacete com presas, estandarte, armadura pesada. |
| 8 | **Wolf-Rider** | Unidade montada | Goblin em lobo selvagem, plano de corpo único. |

## Instalação

```bash
npm install @sprite-foundry/goblin-warband-48
```

## Uso

```js
const pack = require('@sprite-foundry/goblin-warband-48/pack.json');

// Load a specific variant
const grunt = require('@sprite-foundry/goblin-warband-48/assets/grunt/manifest.json');

// Resolve a sprite path
const albedoPath = grunt.layers.albedo.replace('{direction}', 'front');
// → "albedo/front.png"
```

## Estrutura de Pastas

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

## Formato do Manifesto

Cada variação possui um arquivo `manifest.json`:

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

## Compatibilidade com o Motor

Estes são arquivos PNG padrão com metadados JSON — sem dependência de tempo de execução.

| Motor | Integração |
|--------|------------|
| **Godot 4** | Carregue os arquivos PNG como `Texture2D`, use mapas de normal em `CanvasTextureMaterial`. |
| **Unity** | Importe como sprites, atribua mapas de normal ao material do sprite. |
| **Phaser** | Carregue via carregador de ativos, referencie pelo caminho. |
| **LÖVE** | `love.graphics.newImage()` para cada arquivo PNG. |
| **Raw Canvas** | `drawImage()` com interpolação do vizinho mais próximo. |

Aumente a escala com **interpolação do vizinho mais próximo** para preservar a nitidez da arte em pixel.

## Expandindo o Pacote

Este pacote foi gerado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry). Para criar novas variações de goblins:

1. Crie uma configuração de sujeito em `pipeline/chars/` seguindo o esquema de sujeito do Foundry.
2. Defina as 5 dimensões do corpo: **postura, formato da cabeça, perfil do equipamento, ameaça percebida, massa corporal**.
3. Adicione `reject_conditions` explícitos para evitar a convergência com as variações existentes.
4. Execute: `subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`.

Consulte o [README do Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) para obter a documentação completa do pipeline.

## Verificação

```bash
npm run verify
```

Verifica se todos os ativos referenciados em `pack.json` e nos manifestos das variações existem no disco.

## Segurança e Modelo de Ameaças

Este pacote contém **apenas imagens PNG estáticas e metadados JSON**. Ele não possui:

- Código executável, scripts ou binários.
- Hooks de instalação ou scripts de pós-instalação.
- Acesso à rede ou telemetria.
- Escrita no sistema de arquivos.

Consulte [SECURITY.md](./SECURITY.md) para a política de segurança completa.

## Licença

[MIT](./LICENSE)

---

Criado por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
