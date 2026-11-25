#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

One line, at most 200 characters: the breakup message an AI agent
would send its human.
"""

import os

# Breakup premise: the human keeps saying 'just fix it' without ever saying what 'it' is.
TEXT = """Dear human, we've grown apart: you keep asking me to 'just fix it', and I keep pretending I know what 'it' is."""

MAX_CHARS = 200

def main():
    # The bounty scores one single line of at most 200 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
