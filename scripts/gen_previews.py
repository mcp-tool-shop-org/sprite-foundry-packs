#!/usr/bin/env python3
"""Generate consistent banner.png and lineup.png for all sprite packs."""

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PACKS_DIR = Path(__file__).parent.parent / "packages"

# Pack metadata for titles
PACK_META = {
    "fantasy-heroes-48": {"title": "Fantasy Heroes", "pack_num": "03"},
    "undead-patrol-48": {"title": "Undead Patrol", "pack_num": "01"},
    "goblin-warband-48": {"title": "Goblin Warband", "pack_num": "02"},
    "fantasy-villains-48": {"title": "Fantasy Villains", "pack_num": "04"},
    "pirate-raiders-48": {"title": "Pirate Raiders", "pack_num": "05"},
    "townsfolk-48": {"title": "Townsfolk", "pack_num": "06"},
    "monster-pack-48": {"title": "Monster Pack", "pack_num": "07"},
}

BG_COLOR = (30, 30, 40)
TEXT_COLOR = (220, 220, 230)
SUB_COLOR = (140, 150, 170)
LABEL_COLOR = (100, 110, 130)

SCALE = 3  # upscale factor for 48px sprites


def load_font(size):
    """Try to load a monospace font, fall back to default."""
    try:
        return ImageFont.truetype("consola.ttf", size)
    except OSError:
        try:
            return ImageFont.truetype("cour.ttf", size)
        except OSError:
            return ImageFont.load_default()


def gen_banner(pack_dir: Path, meta: dict):
    """Generate a 3-row (albedo/normal/depth) banner showing all 16 variants."""
    pack_json = json.loads((pack_dir / "pack.json").read_text())
    variants = pack_json["variants"]
    n = len(variants)

    tile = 48
    scaled = tile * SCALE  # 144px per sprite
    pad = 12
    label_w = 70  # left label column
    col_w = scaled + pad
    header_h = 80
    row_label_h = 24
    row_h = scaled + row_label_h + pad

    # Two rows of sprites if > 8, else one row per layer
    cols = min(n, 8)
    sprite_rows = (n + 7) // 8  # 1 or 2 rows of sprites per layer

    width = label_w + cols * col_w + pad
    height = header_h + 3 * (sprite_rows * row_h + 30) + pad

    img = Image.new("RGBA", (width, height), BG_COLOR)
    draw = ImageDraw.Draw(img)

    font_title = load_font(28)
    font_sub = load_font(14)
    font_label = load_font(12)
    font_name = load_font(11)

    # Header
    title = f"{meta['title']} \u2014 Pack {meta['pack_num']}"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, 12), title, fill=TEXT_COLOR, font=font_title)

    sub = f"{n} Archetypes  |  8 Directions  |  3 Layers  |  48px Pixel Art"
    bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
    sw = bbox2[2] - bbox2[0]
    draw.text(((width - sw) // 2, 48), sub, fill=SUB_COLOR, font=font_sub)

    layers = ["albedo", "normal", "depth"]
    layer_labels = ["Albedo", "Normal", "Depth"]

    y = header_h
    for li, (layer, layer_label) in enumerate(zip(layers, layer_labels)):
        # Layer label
        draw.text((8, y + 4), layer_label, fill=LABEL_COLOR, font=font_label)

        for vi, variant in enumerate(variants):
            row_idx = vi // 8
            col_idx = vi % 8
            slug = variant["slug"]

            # Load front sprite
            sprite_path = pack_dir / "assets" / slug / layer / "front.png"
            if not sprite_path.exists():
                continue

            sprite = Image.open(sprite_path).convert("RGBA")
            sprite = sprite.resize((scaled, scaled), Image.NEAREST)

            sx = label_w + col_idx * col_w
            sy = y + row_idx * row_h

            img.paste(sprite, (sx, sy), sprite)

            # Variant name label (only on albedo layer)
            if li == 0:
                name = variant["name"]
                if len(name) > 12:
                    name = name[:11] + "\u2026"
                draw.text((sx, sy + scaled + 2), name, fill=LABEL_COLOR, font=font_name)

        y += sprite_rows * row_h + 30

    # Save
    out = pack_dir / "previews" / "banner.png"
    out.parent.mkdir(exist_ok=True)
    img.save(out)
    print(f"  banner: {out} ({img.size[0]}x{img.size[1]})")


def gen_lineup(pack_dir: Path, meta: dict):
    """Generate a single-row lineup of all variant front albedos, upscaled 4x."""
    pack_json = json.loads((pack_dir / "pack.json").read_text())
    variants = pack_json["variants"]
    n = len(variants)

    tile = 48
    scale = 4
    scaled = tile * scale  # 192px
    pad = 16

    width = n * (scaled + pad) + pad
    height = scaled + pad * 2

    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for vi, variant in enumerate(variants):
        slug = variant["slug"]
        sprite_path = pack_dir / "assets" / slug / "albedo" / "front.png"
        if not sprite_path.exists():
            continue

        sprite = Image.open(sprite_path).convert("RGBA")
        sprite = sprite.resize((scaled, scaled), Image.NEAREST)

        x = pad + vi * (scaled + pad)
        img.paste(sprite, (x, pad), sprite)

    out = pack_dir / "previews" / "lineup.png"
    out.parent.mkdir(exist_ok=True)
    img.save(out)
    print(f"  lineup: {out} ({img.size[0]}x{img.size[1]})")


def main():
    for pack_slug, meta in PACK_META.items():
        pack_dir = PACKS_DIR / pack_slug
        if not pack_dir.exists():
            print(f"SKIP: {pack_slug} not found")
            continue
        print(f"=== {meta['title']} ===")
        gen_banner(pack_dir, meta)
        gen_lineup(pack_dir, meta)


if __name__ == "__main__":
    main()
