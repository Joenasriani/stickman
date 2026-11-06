# Repository reconciliation – 2026-11-07

## Authority and completed work

- Project: **In a Stickman's World**, repository `Joenasriani/stickman`.
- Approved product: reverted, no-outro, 15-level stability-lock ZIP. `main/index.html` matches its HTML **byte-for-byte**.
- Active level IDs: **1, 2, 3, 5–16**. This is **15 playable entries**. Level 4 was intentionally removed for its unwanted obstacles. Deleted late duplicate levels 17–20 stay excluded.
- **Do not silently renumber levels**. Enemy counts and tier/difficulty rules depend on the underlying numeric level IDs. Display-label renumbering, or reintroducing Level 4, needs explicit approval and regression testing.
- The previously attempted throne ending and secret-menu trigger were reverted. Do **not** revive them via old attachments or branches.
- Six gameplay assets (`fonts`, `music`, `sfx`) remain unchanged; check `RELEASE_MANIFEST.json` for SHA-256 values.
- The game source remains intentionally frozen under SHA-256 `185b233500237341e00d74c19036f6873b0f4cb2aada7e4218e315d35d821e9f`, Git blob `c17b919453dd4ae646bd045ef0678cc2a78df32f`.

## Git synchronization history

- Original GitHub 20-level `main` preserved at branch `backup/pre-sync-2026-11-05`, commit `56a0cc582468ce2457c358b73543502d9dd7869c`.
- 2026-11-05 commit `259b846afe592e3ed2fa641512d9dbf98effdf18` synchronized the approved 15-level HTML and six original media assets without gameplay changes.
- Three legacy workflows `cleanup-main-design.yml`, `force-clean-pencil-levels.yml`, and `rebuild-clean-pencil-levels.yml` were removed from active `main`: they modified geometry/collisions automatically and could undo approved gameplay. Their contents remain available in history/backup.
- GitHub Pages Actions reported **success** on the 2026-11-05 approved commit. This is deployment status, **not** browser-playback proof.
- The experimental cinematic and optional ECC tooling branches retain history. Neither is authoritative for game behavior.

## Current maintenance constraints

1. Preserve `index.html` exactly unless the user explicitly approves a gameplay, UI, input, camera, state, or dependency change.
2. Keep Level 4 deleted and skip it during normal level progression. Levels 1–3 and 5–16 must remain as approved.
3. Do not merge old cinematic, outro, ECC tooling, or export experiments automatically.
4. Never restore retired write-enabled geometry workflows. Only read-only verification should run on pushes or PRs.
5. Three.js r128 still loads from cdnjs. Local bundling remains **not done**, and altering the script tag should be reviewed as a separate compatibility change.
6. Do not mistake successful `node --check`, ZIP checks, hashes, or a Pages deployment for playtesting.

## Unverified / still open

- Live game start, audio, controls, secret menu, exit transitions, and all 15 levels in a browser.
- Mobile portrait/landscape interactions and controls.
- Solvability, hazards, reachability, physics, enemy counts/tier counts in runtime.
- CDN availability for end users; no local Three.js is bundled.
- Published itch.io build version has **not** been matched against this commit.

## Operational handoff

- Read `README.md`, `RELEASE_MANIFEST.json`, and `docs/QA.md` first.
- Run `python3 tools/validate_release.py` and inspect the read-only Actions check.
- Verify `main/index.html` has the manifest Git blob SHA before editing.
- For a rollback, inspect `backup/pre-sync-2026-11-05`, but note this backup is **not** the approved current release.
- The approved ZIP's SHA-256 is listed in the manifest. The ZIP is a historical local deliverable, **not** a GitHub release asset.
