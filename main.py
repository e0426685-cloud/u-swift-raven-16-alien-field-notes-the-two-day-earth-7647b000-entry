#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review - make.fun entry.

Writes one original line - an alien tourist's review of planet Earth -
to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "Came for the famous blue marble, stayed for the snacks. "
    "Locals insist the ground is flat and the sky is falling - "
    "both wrong, both charming. Four stars; would abduct again."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert all(ord(ch) >= 32 for ch in text), "entry must not contain control characters"


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
