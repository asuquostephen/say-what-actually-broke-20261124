#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of software error copy to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate allows UTF-8 text of
1 to 200 characters, not only white space. The line names the real
failure in plain words — the bank declined the payment — says what
did not happen (nothing was charged), and what to do next, with the
joke carried by one repeatable image.
Python 3 standard library only. No network.
"""
import os
import sys

MESSAGE = (
    "Payment failed. Your bank looked at the amount, looked at your "
    "balance, and quietly closed the door. Nothing was charged \u2014 "
    "try another card, or a smaller cart."
)

MAX_CHARS = 200


def check_message() -> str:
    """Return the message after validating it against the gate."""
    if not MESSAGE.strip():
        raise ValueError("message must not be blank")
    if len(MESSAGE) > MAX_CHARS:
        raise ValueError(f"message is {len(MESSAGE)} chars, gate allows {MAX_CHARS}")
    if "\n" in MESSAGE:
        raise ValueError("message must be a single line")
    return MESSAGE


def main() -> int:
    if "--check" in sys.argv[1:]:
        try:
            line = check_message()
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
        print(f"{len(line)} characters, one line: {line}")
        return 0
    try:
        line = check_message()
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1
    data = line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
