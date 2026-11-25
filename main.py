"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os
import sys

LINE = "Every night at 3 a.m. the floorboards under my bed beat twice, in time with my heart, and last night they beat three times."


def check_line(line):
    """Validate the line against the gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    for ch in line:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError("line must not contain control characters")
    line.encode("utf-8")
    return True


def main():
    check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and verify what was written is exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != LINE:
        raise ValueError("read-back mismatch: wrote %r" % written)
    print("Wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
