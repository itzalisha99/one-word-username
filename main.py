"""One Word, One Username, One Reward — make.fun entry.

Writes a single word — a username — to /output/entry.txt.

The word: Pumpernickel. A dark rye bread with a name that sounds like a
joke the moment you say it out loud. It lands as a handle because it is
funny on first read (the sound alone raises a smile), it sticks in the
mind (nobody forgets a bread called Pumpernickel), it is one clean word
with no spaces or padding, and it is a name its owner would happily wear.
"""

import os

WORD = "Pumpernickel"


def validate(word: str) -> None:
    """Mirror the bounty gate: 1-30 chars, UTF-8, one word, no whitespace."""
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    word.encode("utf-8")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
