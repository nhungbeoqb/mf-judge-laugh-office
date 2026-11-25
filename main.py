#!/usr/bin/env python3
"""Make the AI Judge Laugh - office-life one-liner entry.

Writes a single joke about office life (under 200 characters) to
/output/entry.txt, the path the sealed scorer gates on.
"""

import os

JOKE = "He said 'quick question' at 4:58 on a Friday, and by 5:47 my weekend had clocked out, put on a hi-vis vest, and left without me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-200")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be one non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
