#!/usr/bin/env python3
"""Read-only verification for the approved Stickman release. Does not execute gameplay."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "RELEASE_MANIFEST.json"

def fail(message):
    raise SystemExit(f"FAIL: {message}")

m = json.loads(MANIFEST.read_text(encoding="utf-8"))
index = ROOT / m["source_file"]
if not index.exists(): fail("index.html absent")
raw = index.read_bytes()
if hashlib.sha256(raw).hexdigest() != m["source_sha256"]: fail("source SHA-256 differs from approved baseline")
if len(raw) != m["source_bytes"]: fail("source byte length differs")
source = raw.decode("utf-8")
levels = [int(x) for x in re.findall(r"name:\s*['\"]Level\s+(\d+)['\"]", source)]
if levels != m["playable_level_numbers"]: fail(f"playable level labels changed: {levels}")
if len(levels) != m["playable_level_count"]: fail("playable level count changed")
if "finalCutscene" in source or "cheatFinalButton" in source: fail("unapproved outro hook was restored")
if "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" not in source:
    fail("Three.js dependency changed; review before updating this check")
for rel, checksum in m["asset_sha256"].items():
    f = ROOT / rel
    if not f.is_file(): fail(f"asset missing: {rel}")
    if hashlib.sha256(f.read_bytes()).hexdigest() != checksum:
        fail(f"asset modified: {rel}")
for obsolete in m["retired_workflows"]:
    if (ROOT / obsolete).exists(): fail(f"legacy auto-rewriter unexpectedly active: {obsolete}")
js = [block for block in re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", source, flags=re.S) if block.strip()]
if len(js) != 1: fail(f"unexpected inline JS block count: {len(js)}")
with tempfile.TemporaryDirectory() as d:
    candidate = Path(d) / "game.js"
    candidate.write_text(js[0], encoding="utf-8")
    try:
        p = subprocess.run(["node", "--check", str(candidate)], capture_output=True, text=True)
    except FileNotFoundError:
        fail("Node.js required for JS syntax validation")
    if p.returncode: fail("inline JS syntax failed: " + p.stderr.strip())
print("PASS: source SHA-256, byte count, level IDs/count, assets, retired workflows, and JS syntax")
print("LIMIT: no browser rendering, physical gameplay, or mobile/touch verification in this validator")
