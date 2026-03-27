<p align="center">
  <a href="README.md">English</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

48pxのピクセルアートヒーローキャラクターセット。アルベド、ノーマルマップ、深度マップが含まれており、ゲームエンジンに依存しない形で利用可能です。

![ファンタジーヒーロー バナー](previews/banner.png)

## 同梱内容

冒険パーティーを構成する8種類のヒーローキャラクター：

![バリエーション ラインナップ](previews/lineup.png)

| バリエーション | 役割 | シルエット |
|---------|------|------------|
| 戦士 | 前線でのオールラウンダー | 剣と盾、バランスの取れた装甲 |
| レンジャー | 遠距離攻撃 | 弓、マント、細身のシルエット |
| 魔法使い | 魔法使い | 杖、ローブ、魔法力のあるシルエット |
| 盗賊 | 奇襲部隊 | フード、軽装、ダガー、身軽な姿勢 |
| 聖職者 | 回復/サポート | メイス、盾（太陽の紋章）、聖衣 |
| バーバリアン | 高火力 | 巨大な武器、がっしりとした体格、毛皮/革 |
| パラディン | エリートタンク | 全身鎧、大型の盾、ウォーハンマー、マント |
| モンク | 素早いスペシャリスト | 無装甲、包帯、ボウスタッフ、鍛えられたシルエット |

各バリエーションには、以下の3つのマップレイヤーが含まれています。

- **アルベド (Albedo)** — 基本色スプライト（透明PNG）
- **ノーマル (Normal)** — ダイナミックライティング用のノーマルマップ
- **深度 (Depth)** — パララックス効果と高低差表現用の深度マップ

## インストール

```bash
npm install @sprite-foundry/fantasy-heroes-48
```

## フォルダ構成

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

## マニフェスト形式

各バリエーションには、`manifest.json`ファイルがあります。

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

パック全体の`pack.json`ファイルは、各バリエーションのパスと、それぞれのマニフェストへの参照を記述しています。

## ゲームエンジンとの互換性

これらは、JSONメタデータを含むシンプルなPNGファイルです。画像を読み込めるあらゆるゲームエンジンまたはフレームワークで使用できます。

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- カスタムエンジン

特定のエンジンに依存する形式やランタイムの依存関係はありません。

## 仕様

- **タイルサイズ:** 48 x 48 px
- **方向:** 8種類（正面、左正面、左、左背面、背面、右背面、右、右正面）
- **形式:** 透明PNG
- **マップ:** アルベド + ノーマル + 深度
- **アニメーション:** 静止ポーズ（v1）
- **視点:** トップダウン

## パックの拡張

このパックのスタイルとエクスポート仕様に合わせた、追加のヒーローバリエーションを作成したいですか？

このパックは、[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry)という、オープンソースのComfyUI + SDXLピクセルアート生成パイプラインを使用して作成されました。 Foundryリポジトリには、必要なものがすべて含まれています。

- **生成パイプライン:** `pipeline/foundry_gen.py`が、各キャラクターの設定に基づいてComfyUIを制御します。
- **キャラクター設定:** `pipeline/chars/hero_*.json`が、各バリエーションの正確なプロンプト、シード、シルエットルール、および拒否条件を定義します。
- **バッチマニフェスト:** `pipeline/manifests/fantasy_heroes_03.json`が、8つの設定をエクスポート構造にマッピングします。
- **エクスポートCLI:** `foundry export <run_id>`が、チェックサム付きの決定論的なパックを生成します。
- **ControlNetチューニング:** ヒューマノイド深度の強度: 0.60、エンドパーセント: 0.85（マニフェストに記載）

新しいバリエーションを追加するには：

1. 既存のヒーロー設定に従って、`pipeline/chars/`ディレクトリにキャラクター設定を作成します。
2. 登録: `python -m foundry.cli subject-add <id> --name "名前"`
3. 生成: `python -m pipeline.foundry_gen --config pipeline/chars/<設定ファイル名>.json`
4. 確認し、承認し、マップを生成し、完了を承認し、エクスポートします。
5. エクスポートされたパックを、対応する`assets/<スラッグ>/`ディレクトリにコピーします。

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme)には、パイプライン全体の詳しい手順が記載されています。

## セキュリティ

このパッケージには、**静的なPNG画像とJSONメタデータのみ**が含まれています。実行可能なコード、インストールスクリプト、ネットワークアクセス、およびテレメトリー機能は一切ありません。アセットは、設計上、読み取り専用です。

詳細なセキュリティポリシーについては、[SECURITY.md](SECURITY.md) を参照してください。

## ライセンス

MITライセンス — 商用および非商用プロジェクトでの利用が可能です。

## クレジット

[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) を使用して、ComfyUI + SDXL ピクセルアート パイプラインで生成されました。

制作：<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
