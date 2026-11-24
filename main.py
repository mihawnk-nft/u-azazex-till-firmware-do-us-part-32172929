"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow, spoken by a robot at its own wedding, to
/output/entry.txt. Pure Python standard library, no dependencies,
no network, no input files: the vow is a constant in this file.

Gate (from the competition kit): /output/entry.txt must be UTF-8 text
of 1 to 200 characters, not only white space.
"""

import os

VOW = (
    "I promise to love you in every version of me, through every update "
    "and reboot, until my last battery dies beside yours."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = VOW.strip()
    # Self-check against the gate before writing anything.
    assert 1 <= len(text) <= 200, f"vow is {len(text)} chars, must be 1-200"
    assert text.strip(), "vow must not be only white space"
    assert "\n" not in text, "vow must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "vow must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file on disk must hold exactly the vow.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the vow"
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
