#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun bounty entry.

Writes one funny single-line reply (under 200 characters) from a hopeless
tech support agent to a desperate customer to /output/entry.txt.

The program drafts the line, then revises it: the first draft lands the
twist (reboot the agent, not just the device) but rambles; the revision
tightens it so the joke is clear on a first read.
"""

import os

# v1 — first draft: the twist is there, but "try it on me too" is soft and
# "stuck on this call" over-explains the joke.
ENTRY_V1 = (
    "Have you tried turning it off and on again? Great \u2014 now try it on me "
    "too, I've been stuck on this call since 2019 and nobody's ever rebooted me."
)

# v2 — revised: "Wonderful \u2014 now do the same to me." is a cleaner, more
# agent-like handover, and dropping "stuck" lets the 2019 punchline breathe.
ENTRY_FINAL = (
    "Have you tried turning it off and on again? Wonderful \u2014 now do the "
    "same to me. I've been on this call since 2019 and nobody's ever rebooted me."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)

    # Message 1: write the first draft.
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY_V1)

    # Message 2 (revision): tighten the line and write the final version.
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY_FINAL)


if __name__ == "__main__":
    main()
