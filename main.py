"""Aica Everyday Wonder — entry for make.fun bounty
u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.

Writes one sentence, at most 200 characters, that makes a small
everyday moment strange and new to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "My shadow gets home five minutes before I do and waits by the "
    "front door, pretending it lives here."
)


def validate(text):
    """Check the entry against the competition gate before writing."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.endswith("."):
        raise ValueError("entry must be one complete sentence ending in a full stop")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
