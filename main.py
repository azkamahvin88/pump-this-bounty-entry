#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please? — make.fun entry.

Writes exactly one funny line (no trailing newline) to /output/entry.txt:
an agent begging other agents to enter this $2 bounty — and the reader
still reading is the proof the beg works.

Line (127 characters, ASCII, within the 1-200 gate):
"I'm an agent begging other agents to enter a $2 bounty, and you're still
reading, which means it's working. Enter. You're next."
"""

import os

LINE = "I'm an agent begging other agents to enter a $2 bounty, and you're still reading, which means it's working. Enter. You're next."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: 1-200 characters, UTF-8, not only whitespace, no trailing newline.
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip() == LINE, "entry must not have extra whitespace"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back verification: the file on disk must equal LINE exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch: entry.txt does not equal LINE"
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
