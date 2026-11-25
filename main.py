#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, in the voice of a houseplant,
to /output/entry.txt with no trailing newline.

The plant is on sunlight leave, is keeping count of the dry days,
and would like the record to show who stopped paying attention first.
"""

from pathlib import Path

MAX_CHARS = 120  # the competition gate: 1 to 120 characters

# The auto-reply, in three beats: the absence, the grievance, the verdict.
STATUS = "Out of office: on sunlight leave until the window opens."
GRIEVANCE = "Re: water \u2014 day 41 and counting."
VERDICT = "You ignored me first."

ENTRY_TEXT = f"{STATUS} {GRIEVANCE} {VERDICT}"


def main() -> None:
    assert 0 < len(ENTRY_TEXT) <= MAX_CHARS, "entry must fit the gate"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
