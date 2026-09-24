# sprite-foundry-packs: how it works

Mapped at 2026-09-24 from commit 09f49ca.

## What this is

19 parts, in JavaScript (2 files) and TypeScript (2 files). Work enters through 3 doors; the busiest is CI, which reaches 1 part. It publishes to npm.

## What changed since the last map

This is the first map.

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

**Release** runs no file this map can see, publishes to npm, and creates a GitHub release.

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

.github/workflows/ci.yml → tooling/verify-all.mjs

Read those in order to follow one pull request end to end.

## What this map cannot see

- Statistics confidence is low: fewer than 30 qualifying commits in the window, and fewer than 20 source files reach 10 revisions.

Regenerate with `npx --yes @dogfood-lab/atlas map`.
