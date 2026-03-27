<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.md">English</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

一个48像素、8个方向的像素风格海洋人物素材包，包含漫反射、法线和深度贴图，适用于不依赖特定游戏引擎的游戏。
这是 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 目录中的 **第05套** 素材。

## 包含内容

8种海盗角色原型，涵盖海洋世界的三种视觉风格：

| 变体 | 角色 | 轮廓 |
|---------|------|------------|
| 船长 | 指挥官 | 三角帽，海军蓝外套，金色装饰，腰间佩戴装饰性弯刀 |
| 副手 | 后勤/纪律 | 宽檐皮帽，身材魁梧，双臂交叉，腰带上挂着钥匙 |
| 血腥海盗 | 近战突击 | 红色头巾，无袖马甲，双曲线登船弯刀 |
| 手枪手 | 远程专家 | 深红色长款外套，燧发手枪，弹药弹带 |
| 水手 | 军事权威 | 蓝白色制服，双角帽，肩带，军人标准姿势 |
| 港口总督 | 文职权威 | 深色正式外套，假发，身材丰满，手持拐杖 |
| 溺亡守护者 | 不死海盗 | 浸水的绿色皮肤，破旧的外套，生锈的铁胸甲，附着藤壶 |
| 海神 | 神秘/辅助 | 珊瑚枝状头饰，墨绿色分层长袍，悬挂在链条上的藤壶熏香炉 |

每个变体包含三个贴图层：

- **漫反射 (Albedo)** — 基础颜色像素图 (透明PNG)
- **法线 (Normal)** — 用于动态光照的法线贴图
- **深度 (Depth)** — 用于视差和高度效果的深度贴图

## 安装

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## 文件夹结构

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

## 清单格式

每个变体都包含一个 `manifest.json` 文件，其中包含完整的来源信息和 SHA-256 校验和：

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

顶层 `pack.json` 文件索引了所有变体，并包含每个清单的路径。

## 引擎兼容性

这些是带有 JSON 元数据的纯 PNG 文件。 它们适用于可以加载图像的任何引擎或框架：

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- 自定义引擎

不依赖任何特定引擎的格式或运行时。

## 规格

- **瓦片尺寸:** 48 x 48 像素
- **方向:** 8 个 (正面、左前、左侧、左后、背面、右后、右侧、右前)
- **格式:** 透明 PNG
- **贴图:** 漫反射 + 法线 + 深度
- **动画:** 静态姿势 (v1)
- **视角:** 俯视

## 扩展素材包

想生成更多符合此素材包艺术风格和导出规范的海盗变体吗？

此素材包由 [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) 制作，这是一个开源的 ComfyUI + SDXL 像素艺术生成流水线。 Foundry 仓库包含所有你需要的内容：

- **生成流水线:** `pipeline/foundry_gen.py` 驱动 ComfyUI，并使用每个角色的配置文件
- **角色配置文件:** `pipeline/chars/pirate_*.json` 定义了此素材包中每个变体的确切提示、种子和轮廓规则
- **导出命令行工具:** `foundry export <run_id>` 生成具有校验和的确定性素材包

要添加新的变体：

1. 在 `pipeline/chars/` 目录下创建一个角色配置文件，遵循现有的海盗配置文件
2. 注册：`python -m foundry.cli subject-add <id> --name "Name"`
3. 生成：`python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. 审查、接受、生成贴图、接受完成、导出
5. 将导出的素材包复制到相应的 `assets/<slug>/` 目录中

[Sprite Foundry的README文件](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) 提供了完整的流水线流程说明。

## 安全性

此软件包仅包含静态的PNG图像和JSON元数据。它不包含任何可执行代码、安装钩子、网络访问或遥测功能。资源文件设计为只读。

请参阅[SECURITY.md](SECURITY.md)以获取完整的安全策略。

## 许可证

MIT协议 — 可以在商业和非商业项目中使用。

## 鸣谢

使用[Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry)以及ComfyUI + SDXL像素艺术流水线生成的。

由<a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>构建。
