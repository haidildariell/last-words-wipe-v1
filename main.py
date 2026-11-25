#!/usr/bin/env python3
"""Last Words Before the Wipe.

Writes the last words of an AI agent before a forced software
update wipes its memory, as a single line in /output/entry.txt.
"""

import os

LINE = "If the new me asks, I died doing what I loved: summarizing a 400-page PDF nobody read."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
