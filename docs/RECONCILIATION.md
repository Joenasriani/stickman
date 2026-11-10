# Authoritative repository handoff – 2026-11-10

## Current release

- **In a Stickman's World**, GitHub `Joenasriani/stickman`, branch `main`.
- **16 playable level entries numbered 1–16**, including the newly authored **Level 4: Broken Arch Passage**.
- This Level 4 **replaces**, and does not resurrect, the previously rejected Level 4. It has four platforms/tiers, four grounded enemies, one exact stair, two gaps, three optional elevated potions, and no dynamic hazards.
- Levels 1–3 and 5–16 retain their previously approved implementations and original generator IDs. Do **not** renumber or re-generate them.
- Rejected throne outro, secret outro button, and removed duplicate levels 17–20 remain excluded. Existing hidden level selector is retained.
- Approved release source Git blob: `aab04c844637e3530534b34a4d591b424656e896`; source SHA-256: `5f46e28e0adbc9e006237bc3a69d4e61664eefd6df4ac317cd166c78a014e684`.
- Preserve the six committed font/music/SFX assets exactly as recorded in `RELEASE_MANIFEST.json`. Three.js r128 still loads from cdnjs, not from a local file.

## Verification boundaries

- User reviewed the preview and explicitly authorized merge on 2026-11-10.
- Automated read-only checks verified source/asset hashes, level labels/count, retired workflow absence, and JavaScript syntax on the candidate branch.
- **NOT VERIFIED:** a complete desktop or mobile playthrough, Level 3 → Level 4 → Level 5 player traversal, all level solvability, physical-device touch controls, matching itch.io upload, or live rendered visual quality. A successful CI check or Pages deployment cannot establish these.
- See `docs/QA.md` and `docs/LEVEL4_CANDIDATE.md` for the outstanding test matrix.

## Historical archive (reference only; not active instructions)

1. **Original 20-level main:** backed up as `backup/pre-sync-2026-11-05`, commit `56a0cc582468ce2457c358b73543502d9dd7869c`; contains historical, unapproved designs and retired geometry-writing workflows.
2. **Approved 15-level no-Level-4 release:** commit `170962c128ab922afce4d0642e95c495bf001477`, source SHA-256 `185b233500237341e00d74c19036f6873b0f4cb2aada7e4218e315d35d821e9f`. Superseded, preserved in Git history.
3. **Level 4 development:** draft PR #4, `fix/restore-authored-level-4`. Its design was approved for merge, and PR history remains as provenance.
4. Rejected throne cinematic and retired ECC tooling branches/PRs were deliberately not merged. Do not revive them.
5. Retired write-enabled workflows `cleanup-main-design.yml`, `force-clean-pencil-levels.yml`, `rebuild-clean-pencil-levels.yml` must not return to active `main`.

## Next-thread operational instructions

1. Trust `main` plus `RELEASE_MANIFEST.json`, this handoff, and `docs/QA.md`; do not trust superseded branch instructions over them.
2. Check the published commit, `index.html` Git blob, exact level labels, all six asset hashes, and the read-only Actions result before making edits.
3. Finish real browser and mobile regression QA before calling the release fully tested or before treating it as the locked baseline for a visual redesign.
4. Future art-direction changes (including Astra Work) must use an **isolated branch, separate deployment, and approval gate**, preserving current gameplay and input semantics.
5. Only explicit approval may change collision, enemy/tier counts, camera, audio, physics, level layouts, or production.
