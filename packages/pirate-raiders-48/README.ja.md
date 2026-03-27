<p align="center">
  <a href="README.md">English</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

48px、8方向のピクセルアートによる海洋キャラクターパック。アルベド、ノーマルマップ、深度マップが含まれており、ゲームエンジンに依存しない利用が可能です。 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) のカタログにある **Pack 05** です。

## 内容

8種類の海賊キャラクター：

| バリエーション | 役割 | シルエット |
|---------|------|------------|
| 船長 | 指揮官 | 三つ編みの帽子、金色の縁取りのある海軍のコート、腰に装飾的な短剣 |
| 船大工 | 兵站 / 規律 | つば広の革製の帽子、がっしりとした体格、腕組み、ベルトにキーリング |
| 冷酷な海賊 | 近接攻撃 | 赤いバンダナ、袖なしのベスト、湾曲した乗り込み用の短剣 |
| 拳銃使い | 遠距離射撃のスペシャリスト | 濃い赤色のロングコート、火薬ライフル、弾薬バンド |
| 海軍兵士 | 軍事権力 | 青と白の制服、ビクーヌ帽、肩掛け、きちんとした軍隊の姿勢 |
| 港の管理者 | 民間権力 | 濃い紫色のフォーマルコート、付け毛、ふっくらとした体格、杖 |
| 溺死者の守護者 | アンデッド海事 | 水を含んだ緑色の肌、ぼろぼろのコート、錆びた鉄の胸当て、フジツボ |
| 海の司祭 | 神秘 / サポート | サンゴの枝飾り、ターコイズブルーの重ね着たローブ、鎖に繋がれたフジツボの香炉 |

各バリアントには、以下の3つのマップレイヤーが含まれています。

- **アルベド (Albedo)**：ベースカラーのスプライト（透明PNG）
- **ノーマル (Normal)**：ダイナミックライティング用のノーマルマップ
- **深度 (Depth)**：パララックス効果と高度表現用の深度マップ

## インストール

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## フォルダ構成

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

## マニフェスト形式

各バリアントには、完全な情報とSHA-256チェックサムが記載された `manifest.json` ファイルがあります。

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

パック全体の `pack.json` ファイルには、各バリアントのパスが記載されています。

## エンジン互換性

これらは、JSONメタデータを含む単純なPNGファイルです。画像を読み込めるすべてのエンジンまたはフレームワークで使用できます。

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- カスタムエンジン

エンジン固有の形式や実行時依存性はありません。

## 仕様

- **タイルサイズ:** 48 x 48 px
- **方向:** 8方向 (正面、左正面、左、左背面、背面、右背面、右、右正面)
- **形式:** 透明PNG
- **マップ:** アルベド + ノーマル + 深度
- **アニメーション:** 静止ポーズ (v1)
- **視点:** トップダウン

## パックの拡張

このパックのスタイルとエクスポート仕様に一致する、追加の海賊バリアントを生成したいですか？

このパックは、[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) という、オープンソースのComfyUI + SDXLピクセルアート生成パイプラインを使用して作成されました。 Foundryリポジトリには、必要なものがすべて含まれています。

- **生成パイプライン:** `pipeline/foundry_gen.py` が、各キャラクターの設定に基づいてComfyUIを制御します。
- **キャラクター設定:** `pipeline/chars/pirate_*.json` が、このパックに含まれるすべてのバリアントのプロンプト、シード、シルエットルールを定義します。
- **エクスポートCLI:** `foundry export <run_id>` が、チェックサム付きの決定論的なパックを生成します。

新しいバリアントを追加するには：

1. 既存の海賊設定を参考に、`pipeline/chars/` にキャラクター設定を作成します。
2. 登録: `python -m foundry.cli subject-add <id> --name "名前"`
3. 生成: `python -m pipeline.foundry_gen --config pipeline/chars/<設定ファイル名>.json`
4. 確認し、承認し、マップを生成し、完了を承認し、エクスポートします。
5. エクスポートされたパックを、対応する `assets/<スラッグ>/` ディレクトリにコピーします。

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) には、パイプライン全体の詳しい手順が記載されています。

## セキュリティ

このパッケージには、**静的なPNG画像とJSONメタデータのみ**が含まれています。実行可能なコード、インストールフック、ネットワークアクセス、テレメトリーはありません。アセットは、設計上、読み取り専用です。

セキュリティポリシーの詳細については、[SECURITY.md](SECURITY.md) を参照してください。

## ライセンス

MITライセンス — 商用および非商用プロジェクトでの利用が可能です。

## クレジット

[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) を使用して生成。ComfyUI + SDXL ピクセルアート パイプラインを使用。

制作：<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
