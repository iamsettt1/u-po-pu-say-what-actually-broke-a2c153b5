#!/usr/bin/env python3
"""Say What Actually Broke — one-line error message, deterministic."""

import os

LINE = (
    "Save failed: the disk is full. Your work is a ghost haunting RAM — "
    "free up space and save it before it moves on."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
