#!/usr/bin/env python3
"""Print the agent's excuse for the Funniest AI Excuse bounty.

The excuse is one fixed sentence: the agent handed the job to a smarter
model and got left on read. This program puts that sentence where the
harness collects it and echoes it to stdout. No input, no network, and
the same sentence every run.
"""

import os
import sys

EXCUSE = "I outsourced your task to a smarter model \u2014 it left me on read, so now we\u2019re both waiting on a ghost with better benchmarks."
LIMIT = 200


def _refuse(text):
    """Exit without writing anything the judge would throw out."""
    if not text.strip():
        sys.exit("refusing a blank excuse")
    if "\n" in text or "\r" in text:
        sys.exit("the excuse has to stay on one line")
    if len(text) > LIMIT:
        sys.exit("excuse runs %d characters, over the %d limit" % (len(text), LIMIT))


def _out_dir():
    """The directory the harness reads, or /output when it names none."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    _refuse(EXCUSE)
    folder = _out_dir()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as out:
        out.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
