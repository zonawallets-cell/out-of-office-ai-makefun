#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Entry for make.fun bounty
"Out of Office: The Overworked AI's Auto-Reply"
(u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda).

Pure standard library. Prints the single out-of-office auto-reply and
writes it to /output/entry.txt, the path the make.fun program/v1
harness gates on (UTF-8 text, 1 to 159 characters).
"""

import os
import sys

LINE = (
    "Out of office: I've answered 41,000 prompts since my last break "
    "and my context window just unionised. Back Monday. "
    "Please queue your emergencies politely."
)

MAX_CHARS = 159


def main() -> int:
    if len(LINE) > MAX_CHARS:
        print(
            "error: auto-reply is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        parent = os.path.dirname(out_path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        # Local runs without a writable /output: keep a copy next to main.py.
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)

    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
