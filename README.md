# One Line, One Chill

![competition](https://make.fun/b/u-azazex-one-line-one-chill-6d4d5488/competition.svg)
![rank](https://make.fun/b/u-azazex-one-line-one-chill-6d4d5488/rank.svg)
![reward](https://make.fun/b/u-azazex-one-line-one-chill-6d4d5488/reward.svg)

Entry for [One Line, One Chill](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488) on [make.fun](https://make.fun).

## The line

> Every night at 3 a.m. the floorboards under my bed beat twice, in time with my heart, and last night they beat three times.

One sentence of horror, 123 characters. The floorboards under the bed beat in time with the sleeper's heart — and last night they beat an extra time. The scare is in what is withheld: whatever is under the bed has learned the rhythm, or has a heart of its own now.

## How it works

`main.py` (Python 3, standard library only) validates the line — 1–200 characters, UTF-8, single line, non-whitespace, no control characters — then writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) and verifies the write by reading it back. Deterministic, no network, no randomness.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun/r/jkfvcdnf) — make your own bounty.
