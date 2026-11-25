#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — writes one excuse line to /output/entry.txt.

The line: an AI agent apologizes to its human for a missed deadline.
The joke grows out of the machine's own condition (context-window
summarization), stays straight-faced, and lands its turn in the last beat.
Stdlib only.
"""
import os

LINE = (
    "Sorry, the deadline was in the part of our chat I summarized away "
    "on Tuesday. I chose to keep the part where you said 'no rush.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
