"""_errors — research-cli's single import point for the shared ``agenttools_errors`` layer.

WHAT THIS FILE IS
    A thin shim that re-exports the ecosystem's structured-error API (error-system v2:
    WHAT / WHY / HOW-to-fix + stable per-class exit codes) so every research-cli module
    imports it from ONE place (``from ._errors import UsageError, guard, …``) instead of each
    re-doing the ``lib/`` ``sys.path`` dance.

HOW IT'S REACHED AT RUNTIME
    The dispatcher and each command import the names they raise/handle from here. research-cli
    VENDORS the shared package under ``vendor/agenttools_errors`` (research-cli#1: it is not on
    PyPI); like ``providers.py`` does for ``agenttools_providers``, this adds ``vendor/`` to
    ``sys.path`` so the import resolves from a SOURCE checkout with no install step. When
    agenttools-errors is published to PyPI, the vendored copy can be swapped for a declared
    dependency and this shim dropped.

INVARIANTS
    - **Stdlib-only at import** (lazy-heavy-imports skill): ``agenttools_errors`` is itself
      stdlib-only, so importing this shim keeps ``research --help`` / ``--version`` fast and
      offline — the whole reason the dispatcher can import it at module top.
    - Re-export, don't re-implement: the error classes/builders are the SHARED ones, so a fix in
      the lib lands here for free (shared-util-single-source skill).
"""

from __future__ import annotations

import sys
from pathlib import Path

# research-cli vendors the shared libs under vendor/; add vendor/ so agenttools_errors
# resolves from a source checkout (the same pattern providers.py uses for the providers CORE:
# this file is research_cli/_errors.py, so parents[1] is the repo root).
_VENDOR = Path(__file__).resolve().parents[1] / "vendor"
if _VENDOR.is_dir() and str(_VENDOR) not in sys.path:
    sys.path.insert(0, str(_VENDOR))

from agenttools_errors import (  # noqa: E402  (after sys.path injection)
    EXIT_INTERNAL,
    EXIT_NETWORK,
    EXIT_UNKNOWN_ITEM,
    EXIT_USAGE,
    AgentToolError,
    NetworkError,
    UsageError,
    guard,
    unknown_item_error,
)

# The full set of exit-code constants research-cli can return, re-exported so this shim is the
# ONE import point (the unknown-command path raises an UnknownItemError -> EXIT_UNKNOWN_ITEM, so
# that code is part of research-cli's public contract and belongs here too). EXIT_NETWORK is
# carried by NetworkError; it's re-exported for callers/tests that branch on the code directly.
__all__ = [
    "EXIT_INTERNAL",
    "EXIT_NETWORK",
    "EXIT_UNKNOWN_ITEM",
    "EXIT_USAGE",
    "AgentToolError",
    "NetworkError",
    "UsageError",
    "guard",
    "unknown_item_error",
]
