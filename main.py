#!/usr/bin/env python3
"""Write one joke about office life to entry.txt.

Deterministic: writes the exact same bytes on every run.
Standard library only, no network access.
"""

import os

LINE = (
    "The printer only works when nobody needs it, "
    "which is how I know it has a better work-life balance than I do."
)


def validate(line: str) -> None:
    """Enforce the competition limits before writing anything."""
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(
            f"line is {len(line)} Unicode code points, over the 200 limit"
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
