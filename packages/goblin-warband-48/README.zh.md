<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.md">English</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

**8 种哥布林变体 | 8 个方向 | 3 层 (漫反射 + 法线 + 深度) | 48 像素像素艺术**

适用于角色扮演游戏、战术游戏和地下城探险游戏的敌人素材包。 每个变体都有独特的轮廓——姿势、头部形状、装备、威胁感知和体型都不同，以便玩家可以一目了然地识别敌人。

## 变体

| # | 变体 | 角色 | 轮廓 |
|---|---------|------|------------|
| 1 | **Grunt** | 近战炮灰 | 矮小弯曲的身材，粗糙的棍棒 |
| 2 | **Archer** | 远程骚扰者 | 瘦削的身材，超大短弓，箭囊 |
| 3 | **Shaman** | 法师/治疗者 | 带角的头饰，带有图腾的法杖，穿着长袍 |
| 4 | **Brute** | 重型近战坦克 | 宽阔的肩膀，巨大的下巴，带刺的狼牙棒 |
| 5 | **Scout** | 快速侧翼攻击者 | 弓着身子，双匕首，穿着斗篷 |
| 6 | **Bomber** | 范围伤害威胁 | 鼓鼓囊囊的袋子，点燃的炸弹，护目镜 |
| 7 | **Warchief** | 精英领袖 | 带獠牙的头盔，旗帜杆，重型盔甲 |
| 8 | **Wolf-Rider** | 骑乘单位 | 骑在恶犬上的哥布林，独特的身体结构 |

## 安装

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

## 文件夹结构

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

## 清单格式

每个变体都包含一个 `manifest.json` 文件：

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

## 引擎兼容性

这些是标准的 PNG 文件，带有 JSON 元数据，不依赖于运行时环境。

| 引擎 | 集成 |
|--------|------------|
| **Godot 4** | 将 PNG 文件加载为 `Texture2D`，在 `CanvasTextureMaterial` 上使用法线贴图。 |
| **Unity** | 导入为精灵，将法线贴图分配给精灵材质。 |
| **Phaser** | 通过资源加载器加载，通过路径引用。 |
| **LÖVE** | 使用 `love.graphics.newImage()` 加载每个 PNG 文件。 |
| **Raw Canvas** | 使用 `drawImage()` 进行最近邻插值缩放。 |

使用 **最近邻插值** 放大，以保留像素艺术的清晰度。

## 扩展素材包

这个素材包是使用 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 生成的。 要创建新的哥布林变体：

1. 在 `pipeline/chars/` 目录下创建一个主体配置文件，遵循 foundry 的主体模式。
2. 锁定 5 个身体维度：**姿势、头部形状、装备轮廓、威胁感知、体型**。
3. 添加明确的 `reject_conditions`，以防止与其他现有变体发生重叠。
4. 运行：`subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`

请参阅 [Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry) 以获取完整的流水线文档。

## 验证

```bash
npm run verify
```

检查 `pack.json` 和变体清单中引用的每个资源是否存在于磁盘上。

## 安全与威胁模型

此软件包仅包含 **静态的 PNG 图像和 JSON 元数据**。 它具有：

- 没有可执行代码、脚本或二进制文件
- 没有安装钩子或安装后脚本
- 没有网络访问或遥测
- 没有文件系统写入

请参阅 [SECURITY.md](./SECURITY.md) 以获取完整的安全策略。

## 许可证

[MIT](./LICENSE)

---

由 <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> 构建
