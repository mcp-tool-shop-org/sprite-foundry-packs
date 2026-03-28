<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.md">English</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/monster-pack/readme.png" width="400" alt="Monster Pack" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/monster-pack-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/monster-pack-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/monster-pack-48/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

Um bestiário de monstros em pixel art, com 48px, em 8 direções, incluindo mapas de albedo, normal e profundidade, para uso em jogos compatíveis com diferentes engines.

![Banner do Pacote de Monstros](previews/banner.png)

## O que está incluído

16 variações de monstros, divididas em 6 classes de corpo:

![Disposição das Variações](previews/lineup.png)

### Humanoide

| Variação | Função | Silhueta |
|---------|------|------------|
| Guardião do Sino | Cura / negação de área | Figura vestida com um sino grande, correntes, tons de cobre |
| Cavaleiro Espectral | Combate corpo a corpo avançado | Armadura vazia, espada, símbolo de caveira |
| Coletor de Dentes | Ladrão / saqueador | Semelhante a um goblin, com dentes grandes e sorriso, casaco comprido |

### Alto/Magro

| Variação | Função | Silhueta |
|---------|------|------------|
| Sombra de Tinta | Furtividade / assassino | Figura escura e alongada, com membros que gotejam tinta |
| Pescador de Lanterna | Isca / predador de emboscada | Isca bioluminescente, pele translúcida, dentes afiados |
| Seguidor do Espelho | Reflexo / contra-ataque | Superfície reflexiva, fragmentos de cristal, membros afiados |
| Marionete de Raízes | Parasita / controle | Corpo animado por raízes parasitas, pernas de casca |
| Cantor da Garganta | Sônico / controle de multidão | Estrutura esquelética, costelas expostas, manto escuro |

### Largo/Robusto

| Variação | Função | Silhueta |
|---------|------|------------|
| Golem do Relógio | Tanque pesado | Construção mecânica, torso com engrenagens, membros pesados |
| Ídolo Sorridente | Perigo ambiental | Totem de pedra animado, sorriso esculpido, coberto de musgo |
| Guardião da Colmeia | Invocador de enxames | Inseto gigante, placas de quitina, olhos compostos |

### Amórfico

| Variação | Função | Silhueta |
|---------|------|------------|
| Espectro de Lama | Perseguição lenta | Figura de argila gotejante, olhos de brasa, sudário de enterro |
| Rei dos Ratos | Chefe de enxame | Massa fundida de ratos, caudas entrelaçadas, muitos olhos |
| Mãe dos Esporos | Dano de área / debuff | Massa fúngica, coroa de cogumelo, nuvem de esporos |

### Artrópode

| Variação | Função | Silhueta |
|---------|------|------------|
| Tecelão de Ossos | Armadilha / emboscada | Aranha construída com ossos roubados, cabeça de caveira |

### Alado

| Variação | Função | Silhueta |
|---------|------|------------|
| Grifo | Chefe voador | Dragão de duas pernas, asas de morcego, cauda com espinhos |

Cada variação é fornecida com três camadas de mapa:

- **Albedo** — sprites de cor base (PNG transparente)
- **Normal** — mapas normais para iluminação dinâmica
- **Depth** — mapas de profundidade para efeitos de paralaxe e elevação

## Instalação

```bash
npm install @sprite-foundry/monster-pack-48
```

## Estrutura de Pastas

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

## Formato do Manifesto

Cada variação possui um arquivo `manifest.json`:

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

O arquivo `pack.json` de nível do pacote indexa todas as variações com os caminhos para cada manifesto e inclui metadados de `bodyClass`.

## Compatibilidade com Engines

Estes são arquivos PNG simples com metadados JSON. Eles funcionam com qualquer engine ou framework que possa carregar imagens:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Engines personalizadas

Não requer formato específico de engine ou dependência de runtime.

## Especificações

- **Variações:** 16 monstros
- **Classes de corpo:** 6 (humanoide, alto/magro, largo/robusto, amórfico, artrópode, alado)
- **Tamanho do tile:** 48 x 48 px
- **Direções:** 8 (frente, frente_esquerda, esquerda, trás_esquerda, trás, trás_direita, direita, frente_direita)
- **Total de sprites:** 384 (16 x 8 x 3)
- **Formato:** PNG transparente
- **Mapas:** albedo + normal + profundidade
- **Animação:** poses estáticas (v1)
- **Perspectiva:** visão superior

## Expandindo o Pacote

Deseja gerar mais variações de monstros que correspondam ao estilo artístico e ao contrato de exportação deste pacote?

Este pacote foi criado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), um pipeline de geração de pixel art de código aberto, baseado em ComfyUI + SDXL. Monstros não humanoides utilizam a **"monster lane"** – guias de profundidade ControlNet específicos para cada tipo de corpo, que impõem estruturas corporais exóticas sem forçar um esqueleto humano. O repositório do Sprite Foundry contém tudo o que você precisa:

- **Pipeline de geração** — `pipeline/foundry_gen.py` controla o ComfyUI com configurações específicas para cada criatura.
- **Configurações das criaturas** — `pipeline/chars/beast_*.json` definem os prompts, as sementes e a classe de corpo exatos para cada variação neste pacote.
- **Geradores de profundidade** — `pipeline/morph_refs/gen_amorphous_depth.py`, `gen_wide_squat_depth.py`, `gen_tall_thin_depth.py`
- **Predefinições de classe de corpo** — seleção automática da intensidade e do tempo do ControlNet para cada tipo de criatura.
- **Interface de linha de comando de exportação** — `foundry export <run_id>` cria pacotes determinísticos com checksums.

Para adicionar uma nova variação:

1. Crie uma configuração para a criatura em `pipeline/chars/`, seguindo as configurações existentes de "beast".
2. Registre: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Gere: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Revise, aceite, gere os mapas, aceite a finalização e exporte.
5. Copie o pacote exportado para o diretório correspondente `assets/<slug>/`.

O [README do Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contém um guia completo do pipeline.

## Segurança

Este pacote contém **apenas imagens PNG estáticas e metadados JSON**. Não há código executável, nem ganchos de instalação, nem acesso à rede e nem telemetria. Os recursos são de apenas leitura por design.

Consulte o arquivo [SECURITY.md](SECURITY.md) para a política de segurança completa.

## Licença

MIT — pode ser usado em projetos comerciais e não comerciais.

## Créditos

Gerado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) usando o pipeline de pixel art ComfyUI + SDXL.

Desenvolvido por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
