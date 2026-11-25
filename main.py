#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward robot small talk.

Writes a single line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, no tempfile, direct open("wb") + chmod 0644.
"""

import os

def build_line() -> str:
    # Awkward pause ("So…"), forced weather small talk about a firmware
    # update, then the robot's own sensor quietly logging the silence it
    # cannot politely escape — machine logic doing the awkwardness for it.
    return (
        "So\u2026 nice weather for a firmware update. "
        "My proximity sensor has logged eleven seconds of this silence, "
        "and it still hasn't found a polite way to end it."
    )


LINE = build_line()


def main() -> None:
    # Gate mirrors the server scorer: 1-200 UTF-8 chars, not only whitespace.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry line is {len(text)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
