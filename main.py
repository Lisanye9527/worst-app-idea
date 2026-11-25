#!/usr/bin/env python3
"""Entry for make.fun: The Worst App Idea Ever Pitched.

Writes the one-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: the text is a constant,
self-checked against the gate (UTF-8, 1-240 characters, single line)
before writing, and read back afterwards to verify.
"""

import os
import sys

ENTRY = (
    "For $4.99 a month, ShameClock reads your weekly screen-time report aloud "
    "in your mother's most disappointed voice, pausing before the total to "
    "ask if this is what four years of tuition bought — a premium service "
    "for high achievers."
)

MAX_CHARS = 240


def check(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} characters, gate is 1-{MAX_CHARS}")


def main() -> int:
    check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        raise ValueError("read-back does not match what was written")
    print(f"wrote {path}: {len(ENTRY)} characters, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
