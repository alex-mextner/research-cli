"""install-skill — register the ``research`` agent skill with detected harnesses.

A self-registering command (drop-in: the dispatcher scans this package). It delegates to
:func:`research_cli.install.install_skill`, which writes the three idempotent advertisement
layers (SKILL.md + blurb + compat symlink; a marked block in each detected harness instruction
file; the SessionStart aggregator hook) — the same shape the sibling personal CLIs (draw / tg /
review / task) install. ``install.sh`` calls this after symlinking the binary so a fresh machine
bootstrap advertises ``research`` to agents at session start.
"""

from __future__ import annotations

from typing import List

NAME = "install-skill"
SUMMARY = "register the research agent skill with detected harnesses (idempotent)"


def run(argv: List[str]) -> int:
    if argv and argv[0] in ("-h", "--help"):
        print("Usage: research install-skill\n\n" + (__doc__ or "").strip())
        return 0
    from ..install import install_skill

    return install_skill()
