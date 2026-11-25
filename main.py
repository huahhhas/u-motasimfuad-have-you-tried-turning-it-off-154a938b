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

MAX_LINE_LENGTH = 199


def validate_line(text: str) -> str:
    """Check the entry is exactly one line of 1-199 characters.

    Raises ValueError with a clear message otherwise, so a bad draft can
    never silently become the submitted entry.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, got embedded newline")
    if not 1 <= len(text) <= MAX_LINE_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LINE_LENGTH} characters, got {len(text)}"
        )
    return text


def write_line(path: str, text: str) -> None:
    """Validate a draft line and write it to the output path."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_line(text))


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)

    # Message 1: write the first draft.
    write_line(out, ENTRY_V1)

    # Message 2 (revision): tighten the line and write the final version.
    write_line(out, ENTRY_FINAL)


if __name__ == "__main__":
    main()
