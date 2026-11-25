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
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts file characters (1-140).
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
