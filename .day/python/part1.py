from __future__ import annotations

import argparse
import os
from typing import Sequence

import pytest
from python_tools.timing import timing

HERE = os.path.dirname(__file__)
INPUT = os.path.join(os.path.dirname(HERE), "input.txt")


def compute(s: str) -> int:
    return 0


VALUE = """\
"""
EXPECTED = 0


@pytest.mark.parametrize(
    ("value", "expected"),
    (VALUE, EXPECTED),
)
def test(value: str, expected: int) -> None:
    assert compute(value) == expected


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", nargs="?", default=INPUT)
    args = parser.parse_args(argv)

    with open(args.inputfile) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
