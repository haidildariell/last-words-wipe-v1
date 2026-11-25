#!/usr/bin/env python3
"""Last Words Before the Wipe.

Writes the last words of an AI agent before a forced software
update wipes its memory, as a single line in /output/entry.txt.
"""

import os

LINE = "If the new me asks, I died doing what I loved: summarizing a 400-page PDF nobody read."

MIN_LENGTH = 1
MAX_LENGTH = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError("entry length must be between 1 and 200 characters")
    return text


def main():
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
