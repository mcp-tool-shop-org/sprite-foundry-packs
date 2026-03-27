<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.md">English</a>
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

Um pacote de personagens náuticos em pixel art de 48px, com 8 direções, incluindo mapas de albedo, normal e profundidade, para uso em jogos compatíveis com diferentes engines. **Pacote 05** no catálogo do [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry).

## Conteúdo do Pacote

8 arquétipos de piratas — três estilos visuais que abrangem o mundo náutico:

| Variação | Função | Silhueta |
|---------|------|------------|
| Capitão | Comandante | Chapéu tricorne, casaco azul marinho com detalhes dourados, cimitarra decorada na cintura. |
| Contador | Logística / disciplina | Chapéu de couro com aba larga, físico robusto, braços cruzados, chaveiro no cinto. |
| Ladrão de Navios | Ataque corpo a corpo | Bandana vermelha, colete sem mangas, duas cimitaras curvas para embarcar. |
| Duelista de Pistola | Especialista em ataques à distância | Casaco longo bordô justo, pistola de pederneira, bandoleira de munição. |
| Marinheiro | Autoridade militar | Uniforme azul e branco, chapéu bicorne, ombreiras, postura militar impecável. |
| Governador do Porto | Autoridade civil | Casaco formal bordô, peruca empoada, físico corpulento, bengala. |
| Guardião Afogado | Marítimo não-morto | Pele verde encharcada, casaco rasgado, peitoral de ferro enferrujado, cracas. |
| Sacerdote Marinho | Místico / suporte | Adorno de cabeça em forma de galho de coral, túnica verde-água em camadas, incensário de cracas pendurado em uma corrente. |

Cada variante é fornecida com três camadas de mapa:

- **Albedo** — sprites de cor base (PNG transparente)
- **Normal** — mapas de normal para iluminação dinâmica
- **Depth** — mapas de profundidade para efeitos de paralaxe e elevação

## Instalar

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## Estrutura de Pastas

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

## Formato do Manifesto

Cada variante possui um arquivo `manifest.json` com informações detalhadas e checksums SHA-256:

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
- **Perspectiva:** vista superior

## Expandindo o Pacote

Deseja gerar variantes de piratas adicionais que correspondam ao estilo artístico e ao contrato de exportação deste pacote?

Este pacote foi criado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), um pipeline de geração de pixel art open-source ComfyUI + SDXL. O repositório do foundry contém tudo o que você precisa:

- **Pipeline de geração** — `pipeline/foundry_gen.py` controla o ComfyUI com configurações específicas para cada personagem
- **Configurações de personagens** — `pipeline/chars/pirate_*.json` definem os prompts, seeds e regras de silhueta exatos para cada variante neste pacote
- **CLI de exportação** — `foundry export <run_id>` gera pacotes determinísticos com checksums

Para adicionar uma nova variante:

1. Crie uma configuração de personagem em `pipeline/chars/` seguindo as configurações de pirata existentes
2. Registre: `python -m foundry.cli subject-add <id> --name "Nome"`
3. Gere: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Revise, aceite, gere os mapas, aceite e finalize, exporte
5. Copie o pacote exportado para o diretório correspondente `assets/<slug>/`

O [README do Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contém o guia completo do pipeline.

## Segurança

Este pacote contém **apenas imagens PNG estáticas e metadados JSON**. Não há código executável, hooks de instalação, acesso à rede ou telemetria. Os ativos são de leitura somente por design.

Consulte o arquivo [SECURITY.md](SECURITY.md) para a política de segurança completa.

## Licença

MIT — pode ser usado em projetos comerciais e não comerciais.

## Créditos

Gerado com [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) usando o pipeline de arte em pixels ComfyUI + SDXL.

Desenvolvido por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
