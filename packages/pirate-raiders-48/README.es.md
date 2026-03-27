<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.md">English</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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

Un paquete de personajes marítimos de arte de píxeles de 48x48 píxeles y 8 direcciones, con mapas de albedo, normales y de profundidad para su uso en juegos independientes de cualquier motor. **Paquete 05** en el catálogo de [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry).

## ¿Qué incluye?

8 arquetipos de piratas: tres estilos visuales que cubren el mundo marítimo:

| Variante | Rol | Silueta |
|---------|------|------------|
| Capitán | Comandante | Sombrero de tres picos, abrigo azul marino con adornos dorados, sable ornamentado en la cadera. |
| Maestre | Logística / disciplina | Sombrero de cuero con ala ancha, complexión robusta, brazos cruzados, llavero en el cinturón. |
| Asaltante despiadado | Ataque cuerpo a cuerpo | Pañuelo rojo, chaleco sin mangas, dos espadas de abordaje curvas. |
| Duelista con pistola | Especialista a distancia | Largo abrigo burdeos, pistola de avancarga, bandolera de munición. |
| Marinero | Autoridad militar | Uniforme azul y blanco, sombrero bicornio, cinturones cruzados, postura militar impecable. |
| Gobernador del puerto | Autoridad civil | Abrigo formal color ciruela, peluca empolvada, complexión robusta, bastón. |
| Guardián ahogado | Marítimo no muerto | Piel verde y húmeda, abrigo desgarrado, coraza de hierro oxidada, percebes. |
| Sacerdote marino | Místico / soporte | Adorno de cabeza con forma de rama de coral, túnica de capas verde azulada, incensario de percebes en una cadena. |

Cada variante se entrega con tres capas de mapa:

- **Albedo**: sprites de color base (PNG transparente)
- **Normal**: mapas normales para iluminación dinámica
- **Profundidad**: mapas de profundidad para efectos de paralaje y elevación

## Instalación

```bash
npm install @sprite-foundry/pirate-raiders-48
```

## Estructura de carpetas

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

## Formato del manifiesto

Cada variante tiene un archivo `manifest.json` con toda la información de origen y sumas de verificación SHA-256:

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

El archivo `pack.json` a nivel de paquete indexa todas las variantes con las rutas a cada manifiesto.

## Compatibilidad con motores

Estos son archivos PNG simples con metadatos JSON. Funcionan con cualquier motor o framework que pueda cargar imágenes:

- Phaser
- PixiJS
- Godot
- RPG Maker
- Unity (2D)
- Motores personalizados

No requiere formato específico del motor ni dependencia de tiempo de ejecución.

## Especificaciones

- **Tamaño de los mosaicos:** 48 x 48 píxeles
- **Direcciones:** 8 (frente, frente_izquierda, izquierda, atrás_izquierda, atrás, atrás_derecha, derecha, frente_derecha)
- **Formato:** PNG transparente
- **Mapas:** albedo + normal + profundidad
- **Animación:** poses estáticas (v1)
- **Perspectiva:** vista superior

## Extender el paquete

¿Quieres generar variantes de piratas adicionales que coincidan con el estilo artístico y el contrato de exportación de este paquete?

Este paquete se creó con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry), una canalización de generación de arte de píxeles de código abierto ComfyUI + SDXL. El repositorio de foundry contiene todo lo que necesitas:

- **Canalización de generación**: `pipeline/foundry_gen.py` controla ComfyUI con configuraciones específicas para cada personaje.
- **Configuraciones de personajes**: `pipeline/chars/pirate_*.json` definen las indicaciones exactas, las semillas y las reglas de silueta para cada variante de este paquete.
- **CLI de exportación**: `foundry export <run_id>` crea paquetes deterministas con sumas de verificación.

Para agregar una nueva variante:

1. Crea una configuración de personaje en `pipeline/chars/` siguiendo las configuraciones de pirata existentes.
2. Registra: `python -m foundry.cli subject-add <id> --name "Nombre"`
3. Genera: `python -m pipeline.foundry_gen --config pipeline/chars/<config>.json`
4. Revisa, acepta, genera mapas, acepta y finaliza, exporta.
5. Copia el paquete exportado en el directorio correspondiente `assets/<slug>/`.

El archivo README de [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry#readme) contiene una descripción detallada de todo el proceso.

## Seguridad

Este paquete contiene **únicamente imágenes PNG estáticas y metadatos JSON**. No contiene código ejecutable, ni mecanismos de instalación, ni acceso a la red, ni telemetría. Los archivos se leen solo, por diseño.

Consulte el archivo [SECURITY.md](SECURITY.md) para obtener la política de seguridad completa.

## Licencia

MIT: se puede utilizar en proyectos comerciales y no comerciales.

## Créditos

Generado con [Sprite Foundry](https://github.com/mcp-tool-shop-org/sprite-foundry) utilizando el pipeline de arte de píxeles de ComfyUI + SDXL.

Desarrollado por <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
