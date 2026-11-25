"""Copy the one-line commit message to the grader output directory.

Reads entry.txt next to this script and writes it verbatim, in one
direct write, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
No temporary file and no rename: a temp file would be created with
mode 0600, which the grader cannot read.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    try:
        data = (HERE / "entry.txt").read_bytes()
    except OSError as exc:
        raise SystemExit(f"cannot read entry.txt: {exc}") from exc
    try:
        OUT.mkdir(parents=True, exist_ok=True)
        target = OUT / "entry.txt"
        target.write_bytes(data)
        os.chmod(target, 0o644)
    except OSError as exc:
        raise SystemExit(f"cannot write output entry.txt: {exc}") from exc


if __name__ == "__main__":
    main()
