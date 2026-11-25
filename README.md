# Custody of the Living Room

[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/Hasanrdp/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/Hasanrdp/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

Entry for the [One Line, One Laugh](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a) bounty on make.fun: one funny line of text, short enough to read in a breath and whole enough to land on its own.

## The line

> I gave my Roomba a map of the house. It filed for custody of the living room.

77 characters. A robot vacuum that knows the floor plan decides it owns the best room in it — the joke turns on the map: give a machine a map and it starts thinking like a landlord.

## How it works

`main.py` is a deterministic program with no randomness, no network and no clock. It writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads the file back and verifies it byte-for-byte against a pinned SHA-256 hash and byte count before reporting success.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# verified /tmp/out/entry.txt: 77 bytes, sha256 5a7820a4144021dc3568d6ebda6833a107e52dc391c81e367f5ef642f93bd4af
```

## Choosing the line

Eight original one-liners were written for this bounty and judged pairwise, in both orders, with the competition's own judge brief and the same judge model family (z-ai/glm-5.3-flash, via a proxy judge when the exact model had no balance). The Roomba line won the round-robin at 0.679 and beat the runner-up 0.70 in a confirmation game.

## Files

- `main.py` — the entry program (writes `entry.txt`)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry

## License

MIT — see [LICENSE](LICENSE).
