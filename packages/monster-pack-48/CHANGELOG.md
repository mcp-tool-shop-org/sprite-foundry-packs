# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-03-27

### Added

- 16 monster variants across 6 body classes (humanoid, arthropod, wide/squat, tall/thin, amorphous, winged)
- Each variant: 8 directions × 3 layers (albedo, normal, depth) = 384 sprites
- Pack-level `pack.json` with variant index and body class metadata
- Per-variant `manifest.json` with layer paths and direction list
