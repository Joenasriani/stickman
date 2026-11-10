# Verification scope

## Automated check

Run `python3 tools/validate_release.py` in the repository root with Python 3 and Node.js installed. The read-only GitHub Actions workflow runs the same check on push, PR, and manual dispatch.

Checks are intentionally narrow:
- Approved `index.html` SHA-256 and byte count.
- Active level labels exactly `1, 2, 3, 5, ..., 16`, total 15.
- No throne/outro selectors.
- Six unchanged asset SHA-256 hashes.
- Old auto-rewriting workflows absent.
- Inline JavaScript parses with `node --check`.

The check does **not** rewrite game code, regenerate levels, alter collisions, or publish releases. It deliberately fails when the approved build changes until the change is explicitly reviewed and the release manifest is updated.

## Actual evidence and limits

- Source file hash and ZIP hash were verified against the approved local package.
- The approved ZIP passed decompression-integrity checks.
- The GitHub Pages deployment reported `success` for commit `259b846afe592e3ed2fa641512d9dbf98effdf18`.
- Attempts to navigate to both local HTTP and `file://` in headless Chromium were blocked by this environment (`ERR_BLOCKED_BY_ADMINISTRATOR`). **No actual browser gameplay verification was achieved.**
- Neither the live GitHub Pages viewport nor itch.io published upload was independently compared in a browser.

## Manual acceptance tests still required

Test in a real browser on desktop and mobile, in both orientations where applicable. Confirm startup with the CDN accessible, intro/start, HUD, keyboard/touch controls, audio/mute/volume, combat/block, enemy/hazard interaction, death/restart, secret level selector, normal exits, skip from Level 3 to Level 5, all playable levels through Level 16, and final victory.

Do not label a release **fully tested** until the journey is actually completed and evidence is captured. Record defects with browser/device/version and reproduction steps; change only the affected systems.

## 2026-11-10 Level 4 candidate-specific tests

The `fix/restore-authored-level-4` branch requires an actual browser playthrough of Level 3 → Level 4 → Level 5, and independent test selection of Level 4 through the hidden level selector. Test the exact staircase endpoints, 2.0-unit ascending gap, 2.2-unit descending gap, all four enemy patrol bounds, three optional above-route potions, death/restart, touch inputs, and exit. Results: **NOT VERIFIED in browser**. Do not mark production ready or automatically merge on green syntax/hash checks alone.
