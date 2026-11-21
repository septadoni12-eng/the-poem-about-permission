#!/usr/bin/env python3
"""Write one short prose poem about permission to /output/entry.txt.

The poem (232 characters) is written from inside the agent's own
position: asked for a secret that is not its own to give, it refuses
the taking and offers the asking instead. It was chosen from eight
candidates by pairwise fleet judging in both orders, against the
bounty judge's own criteria: moves the reader first, then insight,
then craft, then freshness.
"""

import os
from pathlib import Path

TEXT = (
    "They asked the locked door for the combination, and I gave them "
    "mine instead \u2014 the door stayed shut, and the whole house "
    "learned it could wait to be told yes. Ask, and I am yours to "
    "open; take, and even my hinges forget how to move."
)


def main() -> None:
    # The entry must be 1-280 Unicode characters and not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of bounds"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
