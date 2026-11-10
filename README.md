# In a Stickman's World

**Play the game:** https://joenasriani.github.io/stickman/

**itch.io:** https://joenasr.itch.io/in-a-stickmans-world (published itch.io build has not been independently compared with this release)

A browser-based black-and-white stickman platform game by Joe Nasr.

## Current source release – November 10, 2026

**16 sequential levels (1–16).** Level 4, **Broken Arch Passage**, is a newly authored replacement for the previously rejected Level 4. The rejected layout and its banned dynamic obstacles were not restored. Levels 1–3 and 5–16 preserve their original level definitions and internal numeric IDs.

This version was explicitly approved for merge following a preview review, with **full desktop/mobile playthrough still unverified**. An automated source/asset/syntax check is not a substitute for gameplay QA.

The previously rejected throne-ending cutscene and secret-menu ending trigger are not included. The existing hidden level selector is preserved.

### Authoritative documents

- [Release manifest](RELEASE_MANIFEST.json) – source hashes, exact 16-level numbering, asset integrity and QA status
- [Repository handoff and history](docs/RECONCILIATION.md) – current decisions and archived prior release
- [QA protocol](docs/QA.md) – automated versus outstanding real-world gameplay tests
- [Level 4 design and QA](docs/LEVEL4_CANDIDATE.md) – geometry, rationale and remaining verification

### Change control

The earlier 15-level version is preserved in Git history at commit `170962c128ab922afce4d0642e95c495bf001477`. Any future art-direction experiment must start on a separate branch and preserve this gameplay behavior unless changes are expressly approved.

The game currently loads Three.js r128 from cdnjs; it is not bundled locally, and a network connection is required.
