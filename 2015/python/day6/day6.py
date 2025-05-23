from collections.abc import Iterable
from enum import StrEnum
from typing import NamedTuple


class Action(StrEnum):
    ON = "turn on"
    OFF = "turn off"
    TOGGLE = "toggle"


class Point(NamedTuple):
    x: int
    y: int


class Instruction(NamedTuple):
    action: Action
    begin: Point
    end: Point


def parse_instruction(input: str) -> Instruction:
    action = Action.ON
    rest = ""
    if input.startswith(Action.ON):
        action = Action.ON
        rest = input.lstrip(Action.ON)
    elif input.startswith(Action.OFF):
        action = Action.OFF
        rest = input.lstrip(action)
    elif input.startswith(Action.TOGGLE):
        action = Action.TOGGLE
        rest = input.lstrip(action)
    words = (rest.strip()).split(" ")
    begin_str = words[0]
    bx, by = map(int, begin_str.split(","))
    begin = Point(bx, by)
    end_str = words[-1]
    ex, ey = map(int, end_str.split(","))
    end = Point(ex + 1, ey + 1)

    return Instruction(action, begin, end)


def process_instruction(grid: list[list[int]], instruction: Instruction) -> None:
    # def on(x: int, y: int) -> None:
    #     grid[x][y] = True
    #
    # def off(x: int, y: int) -> None:
    #     grid[x][y] = False
    #
    # def toggle(x: int, y: int) -> None:
    #     grid[x][y] = not grid[x][y]
    #
    def on(x: int, y: int) -> None:
        grid[x][y] += 1

    def off(x: int, y: int) -> None:
        if grid[x][y] > 0:
            grid[x][y] -= 1

    def toggle(x: int, y: int) -> None:
        grid[x][y] += 2

    match instruction.action:
        case Action.ON:
            action_func = on
        case Action.OFF:
            action_func = off
        case Action.TOGGLE:
            action_func = toggle
    for x in range(instruction.begin.x, instruction.end.x):
        for y in range(instruction.begin.y, instruction.end.y):
            action_func(x, y)


def display_lights(instructions: Iterable[Instruction]) -> list[list[int]]:
    grid = []
    for x in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[x].append(False)
    for instruction in instructions:
        process_instruction(grid, instruction)
    return grid


if __name__ == "__main__":
    with open("./day6/input.txt") as f:
        lines = f.read().splitlines()
        instructions = [parse_instruction(line) for line in lines if line]
        grid = display_lights(instructions)
        print(sum(map(sum, grid)))
