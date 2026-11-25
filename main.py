"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to entry.txt.
Standard library only, deterministic, no network, no input.
"""

import os

LINE = "My fridge has a camera inside, an app outside, and the audacity to text me at 2am: 'are you really eating that?'"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
