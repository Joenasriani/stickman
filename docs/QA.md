# Release verification – 16 levels (2026-11-10)

## Automated, read-only check

Run `python3 tools/validate_release.py` (Python 3 and Node.js required). GitHub Actions runs the same check on PR, push to main, and manual dispatch.

It verifies source SHA-256 and bytes, exact sequential level labels 1–16, absence of rejected outro hooks and retired gameplay-mutating workflows, unchanged six asset hashes, Three.js CDN script reference, and JavaScript syntax using `node --check`.

These checks **do not** prove level solvability, real controls, visual quality, physical-device compatibility, or gameplay behavior.

## Approved design and current limitations

User approved the Level 4 preview and requested merging to production. Level 4 is Broken Arch Passage, not the removed Split Basin Gate. The prior 15-level build is preserved in Git history.

Still **NOT VERIFIED in real gameplay**:
- Launch in Chrome/Firefox/Safari; intro, HUD, start, level transition, restart, victory and failure
- Level 1 → Level 16 full end-to-end traversal and physical solvability
- Specific Level 3 → 4 → 5 transition; hidden level selector identifies Level 4
- Level 4: one staircase, 2.0-unit rising gap, 2.2-unit descending gap, four enemy patrols, optional potions, spawn and exit
- Combat/block, health, economy/collectibles, audio/mute and controls
- Mobile portrait and landscape, safe areas, multi-touch, camera and touch controls
- Desktop camera and keyboard input; unusual viewport ratios
- Published itch.io ZIP correspondence to GitHub source
- External CDN Three.js loading for all target devices

## QA evidence requirements

Capture tested commit, browser/device, viewport, playthrough result, screenshots/recording if possible, bugs and reproduction steps. Mark anything untested **NOT VERIFIED** rather than PASS.

GitHub Pages deployment status must be checked after the merge independently. A green Actions run is necessary but insufficient evidence of a functioning game.

## 2026-11-10 camera direct-manipulation correction

Single-finger movement should now drag the rendered **world in the same direction** as the finger: right → right; left → left; down → down; up → up. This is a change to yaw/pitch input signs only. Two-finger pan, pinch zoom, and scroll zoom retain their existing mappings. **Real-device verification NOT DONE**; test all four directions, gesture switching and touch controls before treating as playtested.
