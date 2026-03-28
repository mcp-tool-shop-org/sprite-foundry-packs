<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.md">English</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/monster-pack/readme.png" width="400" alt="Monster Pack" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/monster-pack-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/monster-pack-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/monster-pack-48/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

一个48像素、8个方向的像素风格怪物素材包，包含漫反射贴图、法线贴图和深度贴图，适用于各种游戏引擎。

![怪物素材包宣传图](previews/banner.png)

## 包含内容

16种不同的怪物，分为6种体型：

![怪物种类展示](previews/lineup.png)

### 人形

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 钟楼守卫 | 诅咒/区域封锁 | 身穿长袍，手持沉重铃铛和锁链，带有铜色 |
| 空洞骑士 | 精英近战单位 | 空无一物的盔甲，剑，骷髅标志 |
| 牙齿收集者 | 潜行/拾荒者 | 类似地精，巨大的牙齿，咧嘴笑，穿着长外套 |

### 高大/瘦长

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 墨影 | 潜行/刺客 | 深色的细长生物，滴落着墨汁般的液体 |
| 提灯鱼怪 | 诱饵/伏击型生物 | 生物发光诱饵，半透明的皮肤，尖锐的牙齿 |
| 镜像追踪者 | 反射/反击 | 反光表面，水晶碎片，锋利的肢体 |
| 根傀儡 | 寄生/控制 | 被寄生根系控制的尸体，树皮般的腿 |
| 喉咙吟唱者 | 声波/群体控制 | 骨骼框架，暴露的肋骨，深色的斗篷 |

### 宽大/矮胖

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 时钟傀儡 | 重型坦克 | 机械构造，齿轮躯干，沉重的肢体 |
| 咧嘴偶像 | 环境危害 | 动画石像，雕刻的咧嘴笑，覆盖着苔藓 |
| 蜂巢守护者 | 召唤生物 | 巨大的昆虫类生物，甲壳，复眼 |

### 无定形

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 泥土复生者 | 缓慢追击 | 滴落的泥土雕像，燃烧的眼睛，裹尸布 |
| 鼠王 | 鼠群Boss | 融合在一起的鼠群，缠绕的尾巴，许多眼睛 |
| 孢子之母 | 范围伤害/减益 | 真菌团，蘑菇帽王冠，孢子云 |

### 节肢动物

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 骨骼编织者 | 陷阱/伏击 | 由偷来的骨骼构建的蜘蛛，骷髅头 |

### 带翅膀

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 飞龙 | 飞行Boss | 两足龙，蝙蝠翅膀，带刺的尾巴 |

每个变体都包含三个地图层：

- **漫反射 (Albedo)** — 基础颜色精灵 (透明PNG)
- **法线 (Normal)** — 法线贴图，用于动态光照
- **深度 (Depth)** — 深度贴图，用于视差和高度效果

## 安装

```bash
npm install @sprite-foundry/monster-pack-48
```

## 文件夹结构

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

## 清单格式

每个变体都有一个 `manifest.json` 文件：

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

`pack.json` 文件包含了所有变体的索引，以及每个变体的 `manifest` 文件的路径，并包含 `bodyClass` 元数据。

## 引擎兼容性

这些是带有 JSON 元数据的纯 PNG 文件。 它们适用于任何可以加载图像的引擎或框架：

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- 自定义引擎

不依赖于任何特定引擎的格式或运行时。

## 规格

- **变体数量：** 16 种怪物
- **体型：** 6 种 (人形, 高大/瘦长, 宽大/矮胖, 无定形, 节肢动物, 带翅膀)
- **像素尺寸：** 48 x 48 像素
- **方向：** 8 个 (正面, 左前, 左侧, 左后, 后面, 右后, 右侧, 右前)
- **总精灵数量：** 384 个 (16 x 8 x 3)
- **格式：** 透明 PNG
- **贴图：** 漫反射 + 法线 + 深度
- **动画：** 静态姿势 (v1)
- **视角：** 俯视

## 扩展内容包

您想生成更多符合此内容包的艺术风格和导出协议的怪物变体吗？

此内容包由 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 制作，它是一个开源的 ComfyUI + SDXL 像素艺术生成流水线。非人形怪物使用 **怪物通道**，该通道使用特定于身体类型的 ControlNet 深度引导，可以在不强制使用人类骨骼的情况下，生成具有独特身体结构的怪物。该项目的代码库包含了您所需的所有内容：

- **生成流水线** — `pipeline/foundry_gen.py` 脚本驱动 ComfyUI，并使用每个对象的配置。
- **对象配置** — `pipeline/chars/beast_*.json` 文件定义了此内容包中每个变体的精确提示、种子和身体类型。
- **深度生成器** — `pipeline/morph_refs/gen_amorphous_depth.py`、`gen_wide_squat_depth.py`、`gen_tall_thin_depth.py`
- **身体类型预设** — 自动选择每个生物类型的 ControlNet 强度和时间。
- **导出命令行工具** — `foundry export <run_id>` 生成具有校验和的确定性内容包。

要添加新的变体：

1. 在 `pipeline/chars/` 目录下创建一个新的对象配置文件，遵循现有的 `beast_*.json` 文件的格式。
2. 注册：`python -m foundry.cli subject-add <id> --name "Name"`
3. 生成：`python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. 审查、接受、生成贴图、接受完成、导出。
5. 将导出的内容包复制到相应的 `assets/<slug>/` 目录中。

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) 提供了完整的流水线操作指南。

## 安全性

此软件包仅包含 **静态的 PNG 图像和 JSON 元数据**。它不包含任何可执行代码、安装钩子、网络访问或遥测功能。 资源是只读的。

请参阅 [SECURITY.md](SECURITY.md) 以获取完整的安全策略。

## 许可证

MIT — 可以在商业和非商业项目中使用。

## 鸣谢

使用 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 和 ComfyUI + SDXL 像素艺术流水线生成。

由 <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a> 构建。
