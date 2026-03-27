<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.md">English</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

一个48x48像素、8个方向的像素风格僵尸敌人素材包，包含漫反射贴图、法线贴图和深度贴图，适用于各种游戏引擎。

![不死军团 宣传图](previews/banner.png)

## 包含内容

8种僵尸变体，每种变体包含8个方向的视图：

![变体展示](previews/lineup.png)

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 蹒跚者 | 基础不死生物 | 弯腰、缓慢、姿势僵硬 |
| 奔跑者 | 快速威胁 | 前倾、具有攻击性的姿态 |
| 暴动僵尸 | 装甲单位 | 宽肩膀、盾牌/装甲 |
| 防护服僵尸 | 受污染专家 | 防护服、圆顶头盔 |
| 膨胀僵尸 | 区域威胁 | 宽阔的躯干、不对称的膨胀 |
| 骷髅僵尸 | 脆弱/古老 | 细长的四肢、棱角分明的轮廓 |
| 工人僵尸 | 工业/平民 | 制服、工具带、可辨认的装备 |
| 精英僵尸 | 指挥官/蛮力 | 高大、威严、增强的体型 |

每种变体包含三个贴图层：

- **漫反射 (Albedo)** — 基础颜色精灵图 (透明 PNG)
- **法线 (Normal)** — 用于动态光照的法线贴图
- **深度 (Depth)** — 用于视差和高度效果的深度贴图

## 安装

```bash
npm install @sprite-foundry/undead-patrol-48
```

## 文件夹结构

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

## 清单格式

每种变体都包含一个 `manifest.json` 文件：

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

`pack.json` 文件（位于包的根目录）索引了所有变体，并包含每个清单的路径。

## 引擎兼容性

这些是带有 JSON 元数据的纯 PNG 文件。 它们适用于任何可以加载图像的引擎或框架：

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- 自定义引擎

不包含任何特定于引擎的格式或运行时依赖项。

## 规格

- **瓦片大小:** 48 x 48 像素
- **方向:** 8 个 (正面、左前、左侧、左后、背面、右后、右侧、右前)
- **格式:** 透明 PNG
- **贴图:** 漫反射 + 法线 + 深度
- **动画:** 静态姿势 (v1)
- **视角:** 俯视

## 扩展素材包

想生成更多符合此素材包艺术风格和导出规范的僵尸变体吗？

此素材包由 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 生成，这是一个开源的 ComfyUI + SDXL 像素艺术生成流水线。 Foundry 仓库包含所有你需要的内容：

- **生成流水线** — `pipeline/foundry_gen.py` 驱动 ComfyUI，并使用每个对象的配置
- **对象配置** — `pipeline/chars/zombie_*.json` 定义了此素材包中每个变体的确切提示、种子、轮廓规则和拒绝条件
- **批量清单** — `pipeline/manifests/undead_patrol_01.json` 将所有 8 个配置映射到导出结构
- **导出 CLI** — `foundry export <run_id>` 生成具有校验和的确定性素材包
- **ControlNet 调整** — 人体深度强度 0.60，结束百分比 0.85 (已在清单中记录)

要添加新的变体：

1. 在 `pipeline/chars/` 目录中创建一个对象配置，遵循现有的僵尸配置。
2. 注册：`python -m foundry.cli subject-add <id> --name "名称"`
3. 生成：`python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. 审查、接受、生成贴图、接受完成、导出
5. 将导出的素材包复制到相应的 `assets/<slug>/` 目录中。

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) 提供了完整的流水线教程。

## 安全

此软件包仅包含静态的PNG图像和JSON元数据。它不包含任何可执行代码、安装钩子、网络访问功能或遥测功能。资源文件设计为只读。

请参阅[SECURITY.md](SECURITY.md)以获取完整的安全策略。

## 许可证

MIT协议 — 可以在商业和非商业项目中使用。

## 鸣谢

使用[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry)以及ComfyUI + SDXL像素艺术流水线生成的。

由<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>构建。
