<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.md">English</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

一个48px像素风格的英雄角色合集，包含8个方向，以及用于无引擎限制的游戏开发的漫反射图、法线图和深度图。

![奇幻英雄横幅](previews/banner.png)

## 包含内容

8种英雄原型，构成一个完整的冒险队伍：

![变体阵容](previews/lineup.png)

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 战士 | 全能的前排角色 | 剑+盾，平衡的装甲 |
| 游侠 | 远程攻击者 | 弓箭，斗篷，较轻的轮廓 |
| 法师 | 施法者 | 法杖，长袍，高魔法轮廓 |
| 盗贼 | 侧翼角色 | 兜帽，轻型盔甲，匕首，灵活的姿势 |
| 牧师 | 治疗/辅助 | 带有太阳标志的短柄钉锤，护盾，祭袍 |
| 野蛮人 | 高伤害 | 巨大的武器，宽大的上半身，皮毛 |
| 圣骑士 | 精锐坦克 | 全身板甲，风筝盾，战锤，斗篷 |
| 武僧 | 快速专精 | 无盔甲，缠绕，棍棒，专注的轮廓 |

每个变体包含三个图层：

- **漫反射图 (Albedo)** — 基础颜色精灵图 (透明PNG)
- **法线图 (Normal)** — 用于动态光照的法线图
- **深度图 (Depth)** — 用于视差和高度效果的深度图

## 安装

```bash
npm install @sprite-foundry/fantasy-heroes-48
```

## 文件夹结构

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

## 清单格式

每个变体都有一个 `manifest.json` 文件：

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

`pack.json` 文件（位于包的根目录下）索引了所有变体，并包含每个清单的路径。

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

- **瓦片尺寸：** 48 x 48 px
- **方向：** 8 个 (正面，左前，左侧，左后，背面，右后，右侧，右前)
- **格式：** 透明 PNG
- **图层：** 漫反射图 + 法线图 + 深度图
- **动画：** 静态姿势 (v1)
- **视角：** 俯视

## 扩展此包

想生成更多符合此包艺术风格和导出规范的英雄变体吗？

此包由 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 生成，这是一个开源的 ComfyUI + SDXL 像素艺术生成流水线。 Foundry 仓库包含所有你需要的内容：

- **生成流水线：** `pipeline/foundry_gen.py` 驱动 ComfyUI，并使用每个角色的配置
- **角色配置：** `pipeline/chars/hero_*.json` 定义了每个变体的精确提示、种子、轮廓规则和拒绝条件
- **批量清单：** `pipeline/manifests/fantasy_heroes_03.json` 将所有 8 个配置映射到导出结构
- **导出 CLI：** `foundry export <run_id>` 生成具有校验和的确定性包
- **ControlNet 调整：** 人体深度强度 0.60，结束百分比 0.85 (已记录在清单中)

要添加一个新的变体：

1. 在 `pipeline/chars/` 目录下创建一个角色配置，遵循现有的英雄配置。
2. 注册：`python -m foundry.cli subject-add <id> --name "名称"`
3. 生成：`python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. 审查、接受、生成地图、接受完成、导出
5. 将导出的包复制到相应的 `assets/<slug>/` 目录中

[Sprite Foundry README](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) 提供了完整的流水线教程。

## 安全性

此软件包仅包含静态的PNG图像和JSON元数据。它不包含任何可执行代码、安装钩子、网络访问功能或遥测功能。资源文件设计为只读。

请参阅[SECURITY.md](SECURITY.md)以获取完整的安全策略。

## 许可证

MIT协议 — 可以在商业和非商业项目中使用。

## 鸣谢

使用[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry)以及ComfyUI + SDXL像素艺术流水线生成的。

由<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>构建。
