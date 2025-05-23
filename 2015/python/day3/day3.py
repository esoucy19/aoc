from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    pass


class Position(NamedTuple):
    x: int
    y: int

    def up(self) -> Position:
        return Position(x=self.x, y=self.y + 1)

    def down(self) -> Position:
        return Position(x=self.x, y=self.y - 1)

    def left(self) -> Position:
        return Position(x=self.x - 1, y=self.y)

    def right(self) -> Position:
        return Position(x=self.x + 1, y=self.y)


def count_houses(moves: Iterable[str]) -> int:
    pos = Position(0, 0)
    houses: set[Position] = {pos}
    for move in moves:
        match move:
            case "^":
                pos = pos.up()
            case "v":
                pos = pos.down()
            case "<":
                pos = pos.left()
            case ">":
                pos = pos.right()
        houses.add(pos)
    return len(houses)


def count_houses_robot(moves: Iterable[str]) -> int:
    pos1 = Position(0, 0)
    pos2 = Position(0, 0)
    houses: set[Position] = {pos1}
    tracker = 1
    for move in moves:
        match tracker:
            case 1:
                pos = pos1
            case 2:
                pos = pos2
        match move:
            case "^":
                pos = pos.up()
            case "v":
                pos = pos.down()
            case "<":
                pos = pos.left()
            case ">":
                pos = pos.right()
        houses.add(pos)
        match tracker:
            case 1:
                pos1 = pos
                tracker = 2
            case 2:
                pos2 = pos
                tracker = 1
    return len(houses)


if __name__ == "__main__":
    with open("./day3/input.txt") as f:
        print(count_houses_robot(f.read()))
