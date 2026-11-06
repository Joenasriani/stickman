# in a stickman's world

Game: https://joenasriani.github.io/stickman/

Public game: https://joenasr.itch.io/in-a-stickmans-world

This repository contains the browser build for In a Stickman's World.

Created by Joe Nasr:
https://joe-nasr-signals.vercel.app/

## Approved release

The current authorized `main` build contains **15 playable levels**, internally numbered **1–3 and 5–16**. **Level 4 is intentionally removed**. Level identifiers are deliberately not renumbered because progression, enemy counts, and tiers use those IDs.

The king's throne outro and its secret-menu trigger are **not included** in this release. Experimental branches and historical versions must not be merged without review.

- [Release manifest](RELEASE_MANIFEST.json) – authoritative hashes, level IDs, release provenance, and test scope.
- [Reconciliation and handoff](docs/RECONCILIATION.md) – completed decisions, archive locations, conflicts, and recovery guidance.
- [Verification guide](docs/QA.md) – automated checks versus manual playtesting.

The game loads Three.js r128 from cdnjs. Browser playback and mobile controls require independent runtime testing; passing the build checks alone does not establish playability.
