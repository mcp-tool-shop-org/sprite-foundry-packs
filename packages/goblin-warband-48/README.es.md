<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.md">English</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

**8 variantes de goblins | 8 direcciones | 3 capas (albedo + normal + profundidad) | Arte de píxeles de 48px**

Una colección de enemigos para juegos de rol, juegos de táctica y exploradores de mazmorras. Cada variante tiene un perfil distintivo: la postura, la forma de la cabeza, el equipo, la percepción de la amenaza y la masa corporal son diferentes, lo que permite a los jugadores identificar a los enemigos de un vistazo.

## Variantes

| # | Variante | Rol | Perfil |
|---|---------|------|------------|
| 1 | **Grunt** | Combate cuerpo a cuerpo | Cuerpo pequeño y encorvado, garrote tosco. |
| 2 | **Archer** | Combate a distancia | Delgado, arco corto de gran tamaño, carcaj. |
| 3 | **Shaman** | Hechicero/sanador | Adorno con cuernos, báculo con tótem, vestido. |
| 4 | **Brute** | Tanque de combate cuerpo a cuerpo | Hombros anchos, mandíbula masiva, maza con púas. |
| 5 | **Scout** | Flanqueador rápido | Agachado, dos dagas, capucha. |
| 6 | **Bomber** | Amenaza de área | Bolsa abultada, bomba con mecha encendida, gafas. |
| 7 | **Warchief** | Líder de élite | Casco con colmillos, asta con estandarte, armadura pesada. |
| 8 | **Wolf-Rider** | Unidad montada | Goblin montado en un lobo, diseño corporal único. |

## Instalación

```bash
npm install @sprite-foundry/goblin-warband-48
```

## Uso

```js
const pack = require('@sprite-foundry/goblin-warband-48/pack.json');

// Load a specific variant
const grunt = require('@sprite-foundry/goblin-warband-48/assets/grunt/manifest.json');

// Resolve a sprite path
const albedoPath = grunt.layers.albedo.replace('{direction}', 'front');
// → "albedo/front.png"
```

## Estructura de carpetas

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

## Formato del manifiesto

Cada variante tiene un archivo `manifest.json`:

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

## Compatibilidad con el motor

Estos son archivos PNG estándar con metadatos JSON; no requieren dependencias en tiempo de ejecución.

| Motor | Integración |
|--------|------------|
| **Godot 4** | Cargue los PNG como `Texture2D`, use mapas normales en `CanvasTextureMaterial`. |
| **Unity** | Importe como sprites, asigne mapas normales al material del sprite. |
| **Phaser** | Cargue a través del cargador de activos, haga referencia por ruta. |
| **LÖVE** | `love.graphics.newImage()` para cada PNG. |
| **Raw Canvas** | `drawImage()` con escalado de vecino más cercano. |

Escala con **interpolación de vecino más cercano** para preservar la nitidez del arte de píxeles.

## Extender el paquete

Este paquete se generó con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry). Para crear nuevas variantes de goblins:

1. Cree una configuración de sujeto en `pipeline/chars/` siguiendo el esquema de sujeto de Foundry.
2. Bloquee las 5 dimensiones del cuerpo: **postura, forma de la cabeza, silueta del equipo, percepción de la amenaza, masa corporal**.
3. Agregue `reject_conditions` explícitos para evitar la convergencia con las variantes existentes.
4. Ejecute: `subject-add` → `foundry_gen` → `batch-accept` → `produce` → `export`.

Consulte el [README de Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) para obtener la documentación completa del flujo de trabajo.

## Verificar

```bash
npm run verify
```

Verifica que cada activo referenciado en `pack.json` y en los manifiestos de las variantes exista en el disco.

## Seguridad y modelo de amenazas

Este paquete contiene **solo imágenes PNG estáticas y metadatos JSON**. No tiene:

- Código ejecutable, scripts o binarios.
- Hooks de instalación o scripts de postinstalación.
- Acceso a la red o telemetría.
- Escrituras en el sistema de archivos.

Consulte [SECURITY.md](./SECURITY.md) para obtener la política de seguridad completa.

## Licencia

[MIT](./LICENSE)

---

Creado por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
