from __future__ import annotations

import argparse
import os
from typing import Sequence

import pytest

HERE = os.path.dirname(__file__)
INPUT = os.path.join(os.path.dirname(HERE), "input.txt")


def compute(s: str) -> int:
    values = [0]
    for line in s.splitlines():
        if line:
            values[-1] += int(line)
        else:
            values.append(0)

    return max(values)


@pytest.mark.parametrize(
    ("value", "expected"),
    (("2\n3\n\n3\n3\n", 6),),
)
def test(value: str, expected: int) -> None:
    assert compute(value) == expected


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", nargs="?", default=INPUT)
    args = parser.parse_args(argv)

    with open(args.inputfile) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
