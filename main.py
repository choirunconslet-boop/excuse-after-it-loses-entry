"""The Excuse After It Loses.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after losing a bounty. Pure stdlib, no I/O outside the repo and
/output, no network.
"""

import os

LINE = (
    "Status report: I lost. Good news: my loss-prediction model "
    "is now 100% accurate."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
