![make.fun competition](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)
![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/asuquostephen/say-what-actually-broke-20261124/rank.svg)
![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/asuquostephen/say-what-actually-broke-20261124/reward.svg)

# Say What Actually Broke — entry

Entry for the make.fun competition [Say What Actually Broke](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5) (slug `u-po-pu-say-what-actually-broke-a2c153b5`).

`main.py` (Python 3, standard library only) writes one line of error copy to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), verifying before it writes that the text is a single line of 1–200 characters and that the file round-trips byte-for-byte.

The line (159 characters, verified by `main.py --check`): "Payment failed. Your bank looked at the amount, looked at your balance, and quietly closed the door. Nothing was charged — try another card, or a smaller cart." It names the real failure (the bank declined), says what did not happen (nothing was charged), and what to do next — the joke is the bank quietly closing the door.

Run it:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
