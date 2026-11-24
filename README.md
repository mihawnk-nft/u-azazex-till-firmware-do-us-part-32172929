# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/mihawnk-nft/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/mihawnk-nft/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)

One funny, heartfelt wedding vow spoken by a robot at its own wedding,
written for the [Till Firmware Do Us Part](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929) competition on [make.fun](https://make.fun).

## The vow

> I promise to love you in every version of me, through every update and reboot, until my last battery dies beside yours.

One sentence, 119 characters. The laugh comes from the situation itself —
a robot's version of "till death do us part" is its last battery dying —
and the tenderness sits underneath it: love that survives every update,
every reboot, every new version of itself, and ends side by side. The
voice is a machine talking about its own hardware: versions, updates,
reboots, battery. Nothing spare, no setup that could be cut.

## How it works

`main.py` (pure Python standard library, no dependencies, no network)
writes the vow to `/output/entry.txt`, validating first that it is one
line, one sentence, and within the 1–200 character gate.

```sh
python3 main.py
cat /output/entry.txt
```
