import type { SiteConfig } from '@mcptoolshop/site-theme';

export const config: SiteConfig = {
  title: 'Sprite Foundry Packs',
  description: '48px pixel-art sprite packs with albedo, normal, and depth maps for any game engine',
  logoBadge: 'SF',
  brandName: 'Sprite Foundry',
  repoUrl: 'https://github.com/mcp-tool-shop-org/sprite-foundry-packs',
  footerText: 'MIT Licensed — built by <a href="https://github.com/mcp-tool-shop-org" style="color:var(--color-muted);text-decoration:underline">mcp-tool-shop-org</a>',

  hero: {
    badge: 'Open source',
    headline: 'Sprite Foundry',
    headlineAccent: 'Packs.',
    description: '48px pixel-art sprite packs with albedo, normal, and depth maps. 5 packs, 40 characters, 960 sprites. Works with any engine.',
    primaryCta: { href: '#usage', label: 'Get started' },
    secondaryCta: { href: 'handbook/', label: 'Read the Handbook' },
    previews: [
      { label: 'Install', code: 'npm install @sprite-foundry/undead-patrol-48' },
      { label: 'Use', code: "const sprite = require('@sprite-foundry/undead-patrol-48/assets/shambler/manifest.json')" },
      { label: 'Verify', code: 'npm run verify' },
    ],
  },

  sections: [
    {
      kind: 'features',
      id: 'features',
      title: 'Features',
      subtitle: 'Production-ready sprite assets for game developers.',
      features: [
        { title: '3-Layer Maps', desc: 'Every sprite ships with albedo, normal, and depth maps for dynamic lighting and parallax effects.' },
        { title: '8 Directions', desc: 'Full directional coverage: front, back, left, right, and all diagonals.' },
        { title: 'Engine Agnostic', desc: 'Static PNGs with JSON manifests. Works with Godot, Phaser, PixiJS, RPG Maker, Unity, or raw canvas.' },
      ],
    },
    {
      kind: 'code-cards',
      id: 'usage',
      title: 'Usage',
      cards: [
        { title: 'Install a pack', code: 'npm install @sprite-foundry/fantasy-heroes-48' },
        { title: 'Load sprites', code: "// Node.js\nconst path = require('path');\nconst sprite = path.resolve(\n  'node_modules/@sprite-foundry/fantasy-heroes-48',\n  'assets/paladin/albedo/front.png'\n);" },
        { title: 'Read manifest', code: "const manifest = require(\n  '@sprite-foundry/fantasy-heroes-48/assets/paladin/manifest.json'\n);\n// → directions, checksums, provenance" },
      ],
    },
  ],
};
