<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.md">English</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/monster-pack/readme.png" width="400" alt="Monster Pack" />
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@sprite-foundry/monster-pack-48"><img src="https://img.shields.io/npm/v/@sprite-foundry/monster-pack-48" alt="npm version" /></a>
  <a href="https://github.com/mcp-tool-shop-org/sprite-foundry-packs/blob/main/packages/monster-pack-48/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
</p>

Un bestiario de monstruos en pixel art de 48px, con 8 direcciones, que incluye mapas de albedo, normales y de profundidad para su uso en juegos, independientemente del motor utilizado.

![Banner del Paquete de Monstruos](previews/banner.png)

## ¿Qué incluye?

16 variantes de monstruos en 6 clases de cuerpo:

![Disposición de Variantes](previews/lineup.png)

### Humanoide

| Variante | Rol | Silueta |
|---------|------|------------|
| Guardián de la Campana | Maldición / negación de área | Figura con túnica, campana grande, cadenas, tonos cobrizos |
| Caballero Hueco | Combate cuerpo a cuerpo de élite | Armadura vacía, espada, símbolo de cráneo |
| Recolector de Dientes | Pícaro / carroñero | Similar a un goblin, con una sonrisa que muestra dientes grandes, capa larga |

### Alto/Delgado

| Variante | Rol | Silueta |
|---------|------|------------|
| Sombra de Tinta | Sigilo / asesino | Figura oscura y alargada, con extremidades que gotean tinta |
| Pez Laternilla | Cebo / depredador emboscado | Cebo bioluminiscente, piel translúcida, dientes afilados |
| Acechador del Espejo | Reflejo / contraataque | Superficie reflectante, fragmentos de cristal, extremidades afiladas |
| Marioneta de Raíz | Parásito / control | Cadáver animado por raíces parásitas, piernas de corteza |
| Cantor de Garganta | Sónico / control de multitudes | Estructura esquelética, caja torácica expuesta, capa oscura |

### Ancho/Bajo

| Variante | Rol | Silueta |
|---------|------|------------|
| Golem del Reloj | Tanque pesado | Construcción mecánica, torso con engranajes, extremidades pesadas |
| Ídolo Sonriente | Peligro ambiental | Tótem de piedra animado, sonrisa tallada, cubierto de musgo |
| Guardián del Enjambre | Invocador de enjambres | Insectoide gigante, placas de quitina, ojos compuestos |

### Amorfo

| Variante | Rol | Silueta |
|---------|------|------------|
| Espectro de Barro | Persecución lenta | Figura de arcilla que gotea, ojos brillantes, sudario de entierro |
| Rey Rata | Jefe de enjambre | Masa fusionada de ratas, colas enredadas, muchos ojos |
| Madre de Esporas | Daño de área / debuff | Masa fúngica, corona de sombrero de hongo, nube de esporas |

### Artrópodo

| Variante | Rol | Silueta |
|---------|------|------------|
| Tejedor de Huesos | Trampa / emboscada | Araña construida con huesos robados, cabeza de cráneo |

### Alado

| Variante | Rol | Silueta |
|---------|------|------------|
| Dragón Wyvern | Jefe volador | Dragón de dos patas, alas de murciélago, cola con púas |

Cada variante incluye tres capas de mapa:

- **Albedo:** sprites de color base (PNG transparente)
- **Normal:** mapas normales para iluminación dinámica
- **Profundidad:** mapas de profundidad para efectos de paralaje y elevación

## Instalación

```bash
npm install @sprite-foundry/monster-pack-48
```

## Estructura de carpetas

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

## Formato de manifiesto

Cada variante tiene un archivo `manifest.json`:

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

El archivo `pack.json` de nivel de paquete indexa todas las variantes con las rutas a cada manifiesto e incluye metadatos de `bodyClass`.

## Compatibilidad con motores

Estos son archivos PNG planos con metadatos JSON. Funcionan con cualquier motor o framework que pueda cargar imágenes:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Motores personalizados

No requiere formato específico del motor ni dependencia de tiempo de ejecución.

## Especificaciones

- **Variantes:** 16 monstruos
- **Clases de cuerpo:** 6 (humanoide, alto/delgado, ancho/bajo, amorfo, artrópodo, alado)
- **Tamaño de los tiles:** 48 x 48 px
- **Direcciones:** 8 (frente, frente_izquierda, izquierda, atrás_izquierda, atrás, atrás_derecha, derecha, frente_derecha)
- **Sprites totales:** 384 (16 x 8 x 3)
- **Formato:** PNG transparente
- **Mapas:** albedo + normal + profundidad
- **Animación:** poses estáticas (v1)
- **Perspectiva:** vista superior

## Extender el paquete

¿Desea generar variantes adicionales de monstruos que coincidan con el estilo artístico y el contrato de exportación de este paquete?

Este paquete se creó con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), una canalización de generación de arte de píxeles de código abierto basada en ComfyUI + SDXL. Los monstruos no humanoides utilizan la **pista de monstruos**, que son guías de profundidad de ControlNet específicas para cada tipo de cuerpo, que imponen formas corporales exóticas sin forzar un esqueleto humano. El repositorio de Foundry contiene todo lo que necesita:

- **Canalización de generación** — `pipeline/foundry_gen.py` controla ComfyUI con configuraciones específicas para cada sujeto.
- **Configuraciones de sujetos** — `pipeline/chars/beast_*.json` definen las indicaciones exactas, las semillas y la clase de cuerpo para cada variante de este paquete.
- **Generadores de profundidad** — `pipeline/morph_refs/gen_amorphous_depth.py`, `gen_wide_squat_depth.py`, `gen_tall_thin_depth.py`
- **Preajustes de clase de cuerpo** — selecciona automáticamente la intensidad y el tiempo de ControlNet según el tipo de criatura.
- **Interfaz de línea de comandos de exportación** — `foundry export <run_id>` crea paquetes deterministas con sumas de verificación.

Para agregar una nueva variante:

1. Cree una configuración de sujeto en `pipeline/chars/` siguiendo las configuraciones de "beast" existentes.
2. Registre: `python -m foundry.cli subject-add <id> --name "Nombre"`
3. Genere: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Revise, acepte, genere mapas, acepte la finalización y exporte.
5. Copie el paquete exportado en el directorio correspondiente `assets/<slug>/`.

El [README de Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) tiene una descripción completa de la canalización.

## Seguridad

Este paquete contiene **solo imágenes PNG estáticas y metadatos JSON**. No hay código ejecutable, ni ganchos de instalación, ni acceso a la red, ni telemetría. Los activos son de solo lectura por diseño.

Consulte [SECURITY.md](SECURITY.md) para obtener la política de seguridad completa.

## Licencia

MIT — se puede utilizar en proyectos comerciales y no comerciales.

## Créditos

Generado con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) utilizando la canalización de arte de píxeles ComfyUI + SDXL.

Desarrollado por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
