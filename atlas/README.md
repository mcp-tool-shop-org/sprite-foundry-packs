# sprite-foundry-packs: how it works

Mapped at 2026-09-30 from commit aae7ad5 by Atlas 1.24.0.

## What this is

19 parts, mostly images (6651 files); code in CSS (2), JavaScript (2), TypeScript (2), Astro (1) and Python (1). Work enters through 3 doors; CI and Deploy site to GitHub Pages each reach 1 part, and CI is followed because a pull request goes through it. It publishes one of the 14 packages under packages/ to npm, chosen by the tag. It deploys a site to GitHub Pages.

## What changed since 2026-09-24 (09f49ca)

- packages/ is now written by scripts/gen_previews.py.
- packages/ is now also read by scripts/gen_previews.py.
- packages/fantasy-heroes-48/assets/artificer/albedo/ is now read by packages/fantasy-heroes-48/assets/artificer/manifest.json.
- And 5803 more new writers and readers of places.
- 408 files changed content, across 19 parts.

## What comes in

1. **CI.** On a pull request touching 8 paths; on a push to main touching 8 paths; or by hand. Runs tooling/verify-all.mjs.
2. **Deploy site to GitHub Pages.** On a push to main touching 2 paths; or by hand. Runs site/astro.config.mjs and site/src/.
3. **Release.** When a tag matching `*-v[0-9]*.[0-9]*.[0-9]*` is pushed; or by hand. Runs no file this map can see.

## What happens through CI

1. The workflow runs tooling/verify-all.mjs in tooling.

## Who reads the results

CI writes nothing this map can see.

## The other doors

**Deploy site to GitHub Pages** runs site/astro.config.mjs and site/src/, and deploys the site.

**Release** runs no file this map can see, publishes one of the 14 packages under packages/ to npm, chosen by the tag, and creates a GitHub release.

## What breaks what

No part is imported by another part, and no part sits on the path of two doors.

## What tends to change together

No two source files changed together often enough to name.

Window: 180 days; a pair counts from 3 shared commits, since the window holds fewer than 30 qualifying commits.

## What no test touches

No test files were found by name.

## Written but never read

No place this map can see is written, so none goes unread.

## Helpers that look duplicated

No two parts export a helper that looks alike.

## Generated, never hand-edited

Nothing in this repository writes to a tracked place this map can see.

## Hand-authored

People write .github/, packages/fantasy-heroes-48/, packages/fantasy-heroes-hd/, packages/fantasy-villains-48/, packages/fantasy-villains-hd/, packages/goblin-warband-48/, packages/goblin-warband-hd/, packages/monster-pack-48/, packages/pirate-raiders-3d-2/, packages/pirate-raiders-3d/, packages/pirate-raiders-48/, packages/pirate-raiders-hd/, packages/townsfolk-48/, packages/townsfolk-hd/, packages/undead-patrol-48/, the repository root and site/. Nothing in this repository writes to them.

## Where to start

CI runs no code this map can follow, so there is no path of files to read in order.

## What this map cannot see

- Statistics confidence is low: fewer than 30 qualifying commits in the window, and fewer than 25 source files reach 10 revisions.

Regenerate with `npx --yes @dogfood-lab/atlas map`.
