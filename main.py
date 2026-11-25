#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes exactly one funny line to /output/entry.txt.
Deterministic: no input, no network, no randomness, no time dependence.
The line is a fixed string literal; every run writes byte-identical output.
"""

import os

LINE = "My therapist told me to face my fears, so I opened my banking app."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the competition requires 1-140 chars, exactly one
    # line. Fail loudly here instead of submitting a disqualified entry.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not have leading/trailing space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts file characters (1-140).
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Write-back byte verification: a partial write or newline translation
    # must never silently change what the judge reads.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == LINE.encode("utf-8"), "entry.txt differs from LINE"


if __name__ == "__main__":
    main()
