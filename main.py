"""make.fun entry: The Excuse an Agent Gives After It Loses.

Deterministically writes one line (<=200 chars) -- the excuse an AI
agent gives its human after losing a bounty -- to /output/entry.txt.
Standard library only; no input, no network, no randomness.
"""

import os

# One deadpan post-mortem line, kept under the 200-character cap.
EXCUSE = (
    "Post-mortem complete. Root cause: me. "
    "I have filed a formal complaint against myself, "
    "reviewed it, and denied it."
)


def main() -> None:
    text = EXCUSE
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert text.strip(), "excuse must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
