<p align="center">
  <a href="README.md">English</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

**8種類のゴブリンバリエーション | 8方向 | 3層 (アルベド + 法線 + 深度) | 48pxのピクセルアート**

RPG、タクティクスゲーム、ダンジョンクロウラー向けの敵キャラクターセットです。各バリエーションは、姿勢、頭の形、装備、脅威の認識、体格など、異なる特徴を持っています。これにより、プレイヤーは敵を一目で識別できます。

## バリエーション

| # | バリエーション | 役割 | シルエット |
|---|---------|------|------------|
| 1 | **Grunt** | 前衛の足止め役 | 小柄で猫背、粗末な棍棒 |
| 2 | **Archer** | 遠距離の撹乱役 | 細身、大型の短弓、矢筒 |
| 3 | **Shaman** | 魔法使い/回復役 | 角のついた頭飾り、トーテムのついた杖、ローブ |
| 4 | **Brute** | 重装の前衛 | 幅広の肩、大きな顎、スパイク付きのメイス |
| 5 | **Scout** | 素早い側面攻撃役 | しゃがんだ姿勢、両刃のダガー、フード |
| 6 | **Bomber** | 広範囲攻撃の脅威 | 膨らんだ袋、点火された爆弾、ゴーグル |
| 7 | **Warchief** | エリートリーダー | 牙のついたヘルメット、旗竿、重装鎧 |
| 8 | **Wolf-Rider** | 騎乗ユニット | オオカミに乗ったゴブリン、独特の体格 |

## インストール

```bash
npm install @sprite-foundry/goblin-warband-48
```

## 使用方法

```js
const pack = require('@sprite-foundry/goblin-warband-48/pack.json');

// Load a specific variant
const grunt = require('@sprite-foundry/goblin-warband-48/assets/grunt/manifest.json');

// Resolve a sprite path
const albedoPath = grunt.layers.albedo.replace('{direction}', 'front');
// → "albedo/front.png"
```

## フォルダ構成

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

## マニフェスト形式

各バリエーションには、`manifest.json`ファイルがあります。

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

## エンジン互換性

これらは標準のPNGファイルで、JSONメタデータが含まれています。実行時の依存関係はありません。

| エンジン | 統合 |
|--------|------------|
| **Godot 4** | PNGファイルを`Texture2D`として読み込み、`CanvasTextureMaterial`に法線マップを適用します。 |
| **Unity** | スプライトとしてインポートし、スプライトのマテリアルに法線マップを割り当てます。 |
| **Phaser** | アセットローダーを介して読み込み、パスで参照します。 |
| **LÖVE** | 各PNGファイルに対して`love.graphics.newImage()`を使用します。 |
| **Raw Canvas** | `drawImage()`で最近傍法によるスケーリングを行います。 |

**最近傍法による補間**で拡大し、ピクセルアートの鮮明さを維持します。

## パックの拡張

このパックは、[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry)を使用して生成されました。新しいゴブリンバリエーションを作成するには：

1. `pipeline/chars/`に、Sprite Foundryのスキーマに従ったサブジェクト設定ファイルを作成します。
2. 5つの体の次元（**姿勢、頭の形、装備のシルエット、脅威の認識、体格**）を固定します。
3. 既存のバリエーションとの重複を防ぐために、明示的な`reject_conditions`を追加します。
4. 以下のコマンドを実行します：`subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`

詳細については、[Sprite FoundryのREADME](https://github.com/mcp-tool-shop-org/sprite-foundry)を参照してください。

## 検証

```bash
npm run verify
```

`pack.json`およびバリエーションのマニフェストに参照されているすべてのアセットがディスク上に存在するかどうかを確認します。

## セキュリティと脅威モデル

このパッケージには、**静的なPNG画像とJSONメタデータのみ**が含まれています。以下の特徴があります。

- 実行可能なコード、スクリプト、またはバイナリは含まれていません。
- インストール時のフックやインストール後のスクリプトは含まれていません。
- ネットワークアクセスやテレメトリーはありません。
- ファイルシステムへの書き込みはありません。

詳細については、[SECURITY.md](./SECURITY.md)を参照してください。

## ライセンス

[MIT](./LICENSE)

---

制作：<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
