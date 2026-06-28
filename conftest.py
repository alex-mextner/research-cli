"""Pytest path setup for research-cli (standalone repo).

WHAT this does: puts the repo root (so ``research_cli`` imports) and the vendored libs dir
(so ``agenttools_providers`` / ``agenttools_errors`` import) on ``sys.path`` before any test
module is collected. pytest auto-loads the nearest ``conftest.py`` at session start, so a
test can ``import research_cli...`` and ``import agenttools_providers`` from a clean checkout
WITHOUT an install step — the same self-contained guarantee the runtime ``bin/research`` and
the package shims give. (After an editable install, both are importable anyway; this just
keeps the suite runnable straight from the tree.)
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
for _p in (_ROOT, _ROOT / "vendor"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
