# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] — 2026-03-26

### Changed

- README rewritten to match Pack 01 (Undead Patrol) format with inline banner and lineup images

## [1.0.0] — 2026-03-26

### Added

- 8 goblin variants: Grunt, Archer, Shaman, Brute, Scout, Bomber, Warchief, Wolf-Rider
- 8 directions per variant (front, front_left, left, back_left, back, back_right, right, front_right)
- 3 layers per direction: albedo, normal map, depth map
- 192 total sprite assets (8 variants × 8 directions × 3 layers)
- Pack-level index (`pack.json`) and per-variant manifests
- Contact sheet previews per variant
- Asset verification script (`npm run verify`)
