# Authored Level 4 – Broken Arch Passage

**Status:** approved for production source merge on 2026-11-10; still awaiting full live gameplay and mobile verification. itch.io upload has NOT been synchronized.

## Intent
Restore the missing fourth level with an original, structurally readable composition. **The deleted Split Basin Gate design must not return.** Level 4 has no `risingSpikes`, `pulseLaser`, vertical rising-line obstacle, or generic hazard; this is a deliberate learning-focused interlude between tutorial Level 3 and procedural Level 5.

## Authored design

- Four main platform structures: `[-8,11] @ y=0`, `[15,25] @ y=2.5`, `[27,40] @ y=5`, and `[42.2,56] @ y=2.2`
- Four distinct grounded enemies: `(6.5,0)`, `(20,2.5)`, `(34,5)`, `(48,2.2)`; all patrol within their own platform bounds
- Exactly one staircase: `(11,0)` → `(15,2.5)`, 10 steps × 0.4 width × 0.25 rise
- Gap A: 2 units horizontal, 2.5 units upward
- Gap B: 2.2 units horizontal, 2.8 units downward
- Optional potions above walkable surfaces: `(9,1.7)`, `(22,4.2)`, `(37.5,6.7)`
- Spawn `(-7,0)` on solid terrain, away from enemies
- Exit `(53,3.0)` above final platform
- No spikes or advanced obstacles

## Static checks completed

- Exactly 16 playable level entries, sequentially labeled Level 1…Level 16
- Original internal generator calls remain Levels 5…16 (preserves enemy/tier counts on those levels)
- New Level 4 has four manually authored enemies on solid surfaces, four structures, one exact stair
- Tier changes 2.5, 2.5, −2.8 use only permitted increments
- Two modeled jumps using `MOVE_SPEED=0.14`, `JUMP_SPEED=0.62`, `GRAVITY=-0.032` have nominal landing positions x≈28.26 and x≈43.88 respectively
- JavaScript syntax passed on equivalent local candidate; the read-only repository verifier passed on the candidate branch

## Remaining gates (NOT VERIFIED)

- Actual desktop and mobile startup / performance
- Player control, stair traversal and both gaps in browser
- Enemy combat and patrol behavior during a full run
- Potion pickups via optional jumps
- Safe spawn and exit reachability as actually experienced
- Seamless transition Level 3 → Level 4 → Level 5
- iOS/Android landscape and portrait input and HUD

**Release control:** User explicitly approved merging the Level 4 candidate. Do not describe this version as fully playtested, synchronize itch.io without verifying the exact package, or begin Astra's visual redesign until the requested game-finalization and real gameplay QA are addressed.
