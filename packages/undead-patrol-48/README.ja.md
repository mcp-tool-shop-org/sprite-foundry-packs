<p align="center">
  <a href="README.md">English</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

48pxのピクセルアートゾンビ敵キャラクターセット。アルベド、ノーマルマップ、深度マップが含まれており、ゲームエンジンに依存しない形で利用可能です。

![アンデッドパトロール バナー](previews/banner.png)

## 同梱内容

ゾンビのバリエーションが8種類。各バリエーションは8方向の視点を持っています。

![バリエーション一覧](previews/lineup.png)

| バリエーション | 役割 | シルエット |
|---------|------|------------|
| シャムラー (Shambler) | 基本的なアンデッド | 猫背で、動きが遅く、よろめきのある姿勢 |
| ランナー (Runner) | 素早い敵 | 前傾姿勢で、素早く、攻撃的な動き |
| 暴動ゾンビ (Riot Zombie) | 装甲の重装 | 肩幅が広く、シールドや装甲が装着されている |
| 防護服ゾンビ (Hazmat Zombie) | 汚染物質の専門家 | 防護服の形状、丸いフード |
| ブロウター (Bloater) | 広範囲に影響を与える敵 | 太い胴体、左右非対称な膨らみ |
| スケルトンゾンビ (Skeletal Zombie) | もろく、古代の | 細い手足、角ばった形状 |
| 作業員ゾンビ (Worker Zombie) | 工業用/民間 | 制服、工具ベルト、特徴的な装備 |
| エリートゾンビ (Elite Zombie) | 指揮官/巨漢 | 背が高く、威圧感があり、強化された外見 |

各バリエーションには、以下の3つのマップレイヤーが含まれています。

- **アルベド (Albedo)** — ベースカラーのスプライト (透明PNG)
- **ノーマル (Normal)** — ダイナミックライティング用のノーマルマップ
- **深度 (Depth)** — パーラックス効果や高度表現用の深度マップ

## インストール

```bash
npm install @sprite-foundry/undead-patrol-48
```

## フォルダ構成

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

## マニフェスト形式

各バリエーションには、`manifest.json`ファイルがあります。

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

パック全体の`pack.json`ファイルは、各バリエーションのパスと、それぞれのマニフェストへのリンクを記述しています。

## エンジン互換性

これらは、JSONメタデータを含むシンプルなPNGファイルです。画像を読み込むことができるすべてのエンジンまたはフレームワークで使用できます。

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

このパックのスタイルとエクスポート仕様に一致する、追加のゾンビバリエーションを生成したいですか？

このパックは、[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry)という、オープンソースのComfyUI + SDXLピクセルアート生成パイプラインを使用して作成されました。 Foundryリポジトリには、必要なものがすべて含まれています。

- **生成パイプライン:** `pipeline/foundry_gen.py` が、各キャラクター設定に基づいてComfyUIを制御します。
- **キャラクター設定:** `pipeline/chars/zombie_*.json` が、各バリエーションの正確なプロンプト、シード、シルエットルール、および拒否条件を定義します。
- **バッチマニフェスト:** `pipeline/manifests/undead_patrol_01.json` が、8つの設定をエクスポート構造にマッピングします。
- **エクスポートCLI:** `foundry export <run_id>` が、チェックサム付きの決定論的なパックを生成します。
- **ControlNetチューニング:** ヒューマノイド深度強度 0.60、end% 0.85 (マニフェストに記載)

新しいバリエーションを追加するには：

1. 既存のゾンビ設定に従って、`pipeline/chars/` にキャラクター設定を作成します。
2. 登録: `python -m foundry.cli subject-add <id> --name "名前"`
3. 生成: `python -m pipeline.foundry_gen --config pipeline/chars/<設定ファイル名>.json`
4. 確認し、承認し、マップを生成し、完了を承認し、エクスポートします。
5. エクスポートされたパックを、対応する `assets/<スラッグ>/` ディレクトリにコピーします。

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) には、パイプライン全体の詳しい手順が記載されています。

## セキュリティ

このパッケージには、**静的なPNG画像とJSON形式のメタデータのみ**が含まれています。実行可能なコード、インストールスクリプト、ネットワークアクセス、およびテレメトリー機能は一切含まれていません。アセットは、設計上、読み取り専用です。

セキュリティポリシーの詳細については、[SECURITY.md](SECURITY.md) を参照してください。

## ライセンス

MITライセンス — 商用および非商用プロジェクトでの利用が可能です。

## クレジット

[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) を使用して、ComfyUI + SDXL ピクセルアート パイプラインで生成されました。

制作：<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
