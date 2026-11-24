"""makefun-commuter-forecast: one line of weather forecast for a city
that does not exist, written for make.fun's "Charm the Commuter" bounty.

The program writes exactly one line of text to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "Good morning, Nibberwick: 72 and sunny, with a 100% chance the bus "
    "arrives exactly when you do. Bring coffee, not an umbrella."
)

assert 1 <= len(LINE) <= 140 and LINE.strip(), "line must be 1-140 chars, not only whitespace"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
