from __future__ import annotations

import io
from collections.abc import Iterable
from typing import NamedTuple


class Box(NamedTuple):
    l: int
    w: int
    h: int

    @staticmethod
    def from_string(input: str) -> Box:
        return Box(*map(int, (input.strip()).split("x")))


def calculate_wrapping_paper(boxes: Iterable[Box]) -> int:
    paper = 0
    for b in boxes:
        sides = [
            b.l * b.w,
            b.w * b.h,
            b.h * b.l,
        ]
        surface = 2 * sum(sides)
        smallest = min(sides)
        paper += surface + smallest
    return paper


def calculate_ribbon(boxes: Iterable[Box]) -> int:
    ribbon = 0
    for b in boxes:
        faces = [
            2 * (b.l + b.w),
            2 * (b.w + b.h),
            2 * (b.h + b.l),
        ]
        volume = b.l * b.w * b.h
        ribbon += min(faces) + volume
    return ribbon


def lines_reader(file: io.TextIOWrapper) -> Iterable[str]:
    while True:
        line = file.readline(20000)
        if line is None:
            break
        yield line


def boxes_reader(file: io.TextIOWrapper) -> Iterable[Box]:
    for line in lines_reader(file):
        if not line:
            break
        yield Box.from_string(line)


def main() -> None:
    with open("./day2/input.txt") as f:
        data = boxes_reader(f)
        print(calculate_ribbon(data))


if __name__ == "__main__":
    main()
