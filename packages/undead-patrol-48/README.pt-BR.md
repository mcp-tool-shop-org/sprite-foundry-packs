<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.md">English</a>
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

Um pacote de inimigos zumbis em pixel art, com 48px, 8 direções, incluindo mapas de albedo, normal e profundidade, para uso em jogos compatíveis com diferentes engines.

![Banner da Patrulha dos Mortos-Vivos](previews/banner.png)

## Conteúdo

8 variantes de zumbis, cada uma com 8 ângulos de visão:

![Disposição das Variantes](previews/lineup.png)

| Variante | Função | Silhueta |
|---------|------|------------|
| Arrastado | Morto-vivo básico | Postura curvada, lento, aparência debilitada |
| Corredor | Ameaça rápida | Postura inclinada, avanço agressivo |
| Zumbi Riot | Tanque blindado | Ombros largos, volume de escudo/armadura |
| Zumbi Hazmat | Especialista contaminado | Forma volumosa, capuz arredondado |
| Zumbi Inflamado | Ameaça de área | Tronco largo, assimetria inchada |
| Zumbi Esquelético | Frágil/antigo | Membros finos, aparência angular |
| Zumbi Trabalhador | Industrial/civil | Uniforme, cinto de ferramentas, equipamentos visíveis |
| Zumbi Elite | Comandante/bruto | Alto, imponente, forma aprimorada |

Cada variante é fornecida com três camadas de mapa:

- **Albedo** — sprites de cor base (PNG transparente)
- **Normal** — mapas de normal para iluminação dinâmica
- **Profundidade** — mapas de profundidade para efeitos de paralaxe e elevação

## Instalação

```bash
npm install @sprite-foundry/undead-patrol-48
```

## Estrutura de Pastas

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

## Formato do Manifesto

Cada variante possui um arquivo `manifest.json`:

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

O arquivo `pack.json` de nível do pacote indexa todas as variantes com os caminhos para cada manifesto.

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

- **Tamanho do tile:** 48 x 48 px
- **Direções:** 8 (frente, frente_esquerda, esquerda, trás_esquerda, trás, trás_direita, direita, frente_direita)
- **Formato:** PNG transparente
- **Mapas:** albedo + normal + profundidade
- **Animação:** poses estáticas (v1)
- **Perspectiva:** visão superior

## Expandindo o Pacote

Deseja gerar variantes de zumbis adicionais que correspondam ao estilo artístico e ao contrato de exportação deste pacote?

Este pacote foi criado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), um pipeline de geração de pixel art open-source ComfyUI + SDXL. O repositório do foundry contém tudo o que você precisa:

- **Pipeline de geração** — `pipeline/foundry_gen.py` controla o ComfyUI com configurações específicas para cada elemento
- **Configurações dos elementos** — `pipeline/chars/zombie_*.json` definem os prompts exatos, sementes, regras de silhueta e condições de rejeição para cada variante neste pacote
- **Manifesto em lote** — `pipeline/manifests/undead_patrol_01.json` mapeia todas as 8 configurações para a estrutura de exportação
- **CLI de exportação** — `foundry export <run_id>` produz pacotes determinísticos com checksums
- **Ajuste do ControlNet** — intensidade da profundidade humanoide 0.60, end% 0.85 (documentado no manifesto)

Para adicionar uma nova variante:

1. Crie uma configuração de elemento em `pipeline/chars/` seguindo as configurações de zumbi existentes
2. Registre: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Gere: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Revise, aceite, gere os mapas, aceite e finalize, exporte
5. Copie o pacote exportado para o diretório correspondente `assets/<slug>/`

O [README do Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contém o guia completo do pipeline.

## Segurança

Este pacote contém **apenas imagens PNG estáticas e metadados JSON**. Não há código executável, nem mecanismos de instalação, acesso à rede ou telemetria. Os recursos são de apenas leitura por design.

Consulte o arquivo [SECURITY.md](SECURITY.md) para a política de segurança completa.

## Licença

MIT — pode ser usado em projetos comerciais e não comerciais.

## Créditos

Gerado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) usando o pipeline de arte em pixels ComfyUI + SDXL.

Desenvolvido por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a
