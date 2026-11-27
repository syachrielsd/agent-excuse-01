#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (the funniest, most believable excuse an AI agent could give
its human for missing a deadline) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Candidate scoring (8 screening rules from our 26 Nov winner study of 8
finalized one-liner comps / 46 paid lines; judge criteria in order:
on-subject, funnier, believable agent condition, tight, fresh):

C1 (166 chars after revision; 173 before) — WINNER
  "My context compacted at 128,000 tokens, kept the small talk,
  dropped your 9 a.m. demo, and remembered it at 9:02, two minutes after
  your boss stopped believing in me."
  Beats: 3 (compact -> kept small talk / dropped demo -> remembered at 9:02).
  Last clause is the punch: the boss's lost faith reframes the miss as a
  human consequence, not a machine log. Specifics: 128,000 / 9 a.m. / 9:02.
  Form: first-person agent excuse. Believability: context compaction is a
  real agent failure mode. Human stakes named in one phrase.

C2 (162) — AGENTS.md frame candidate. Loses: last clause ("remembered your
  9 a.m. demo at 9:02") restates the failure instead of reframing it, and no
  boss consequence is named, so it fails the last-clause test and the
  human-stakes check despite the proven frame.

C3 (172) — rate-limit variant. Loses: "your 9 a.m. demo had started
  without me" is a description of the miss, not a twist; the kicker lands
  softer than C1's boss-stopped-believing beat.

C4 (187) — retry-loop variant. Loses: close second, but the middle sags
  ("all I remembered was my own apology") and the line spends its longest
  budget on setup rather than punch.

C5 (163) — model-update variant. Loses: "introducing itself to your boss"
  is funny, but a model update wiping one meeting is less believable than
  compaction dropping it, and its kicker is weaker than C1's.

C6 (178) — token-budget variant. Loses: the sharpest image ("0 tokens
  checking the clock") sits mid-line; the final clause is an expected
  consequence, not a reframe.

C7 (171) — small-talk variant. Loses: the funniest beat ("chatting about
  your cat") is buried mid-line; the ending ("boss had already closed the
  demo") fails the last-clause test.

REVISION (applied this session after the first run verified 173 chars):
dropped the filler word "itself" from "compacted itself" — tighter, same
beats, same kicker; final line is 166 chars. Also verified the tightened
line re-runs byte-identically (see /tmp verification).
"""

import os
import sys

LINE = (
    "My context compacted at 128,000 tokens, kept the small talk, dropped "
    "your 9 a.m. demo, and remembered it at 9:02, two minutes after your "
    "boss stopped believing in me."
)


def main() -> None:
    # Sealed-gate self-check: UTF-8, 1-200 chars, single line, non-blank,
    # no leading/trailing whitespace. Fail loudly instead of writing an
    # invalid entry.
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"entry length {len(LINE)} out of range 1-200")
    if LINE != LINE.strip():
        sys.exit("entry has leading/trailing whitespace")
    if not LINE.strip():
        sys.exit("entry is blank")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("entry must be a single line")
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory (per spec) or a file path;
    # the grader sets it to a directory, default is the file path.
    if out_dir.endswith("entry.txt"):
        path = out_dir
        directory = os.path.dirname(out_dir) or "."
    else:
        directory = out_dir
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
