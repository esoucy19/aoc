from __future__ import annotations

import asyncio

from collections.abc import Awaitable, Callable
from collections import deque
from dataclasses import dataclass

simple_circuit = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

simple_circuit_output = """d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
"""


async def wire(input: asyncio.Task[int]) -> int:
    return await input


async def binary_gate(
    input1: Awaitable[int] | int,
    input2: Awaitable[int] | int,
    f: Callable[[int, int], int],
) -> int:
    if isinstance(input1, Awaitable):
        input1 = await input1
    if isinstance(input2, Awaitable):
        input2 = await input2
    return f(input1, input2)


async def param_gate(
    input: Awaitable[int] | int, param: int, f: Callable[[int, int], int]
) -> int:
    if isinstance(input, Awaitable):
        input = await input
    return f(input, param)


async def unary_gate(input: Awaitable[int] | int, f: Callable[[int], int]) -> int:
    if isinstance(input, Awaitable):
        input = await input
    return f(input)


def AND(x: int, y: int) -> int:
    res = x & y
    if res < 0:
        res = res + 2**16
    return res


def OR(x: int, y: int) -> int:
    res = x | y
    if res < 0:
        res = res + 2**16
    return res


def LSHIFT(x: int, n: int) -> int:
    res = x << n
    if res < 0:
        res = res + 2**16
    return res


def RSHIFT(x: int, n: int) -> int:
    res = x >> n
    if res < 0:
        res = res + 2**16
    return res


def NOT(x: int) -> int:
    res = ~x
    if res < 0:
        res = res + 2**16
    return res


def VALUE(x: int) -> int:
    return x


@dataclass
class Connection:
    inputs: list[int | str]
    gate: Callable
    output: str


def _try_int(s: str) -> str | int:
    if s.isdigit():
        return int(s)
    return s


def parse_input_data(input_data: list[str]) -> list[Connection]:
    connections = []
    for line in input_data:
        if not line:
            continue
        left, right = line.split("->")
        left = (left.strip()).split(" ")

        inputs = []
        gate = VALUE
        match len(left):
            case 1:
                inputs.append(_try_int(left[0]))
                gate = VALUE
            case 2:
                gate = NOT
                inputs.append(_try_int(left[1]))
            case 3:
                match left[1]:
                    case "AND":
                        gate = AND
                    case "OR":
                        gate = OR
                    case "LSHIFT":
                        gate = LSHIFT
                    case "RSHIFT":
                        gate = RSHIFT
                inputs.append(_try_int(left[0]))
                inputs.append(_try_int(left[2]))

        output = right.strip()
        connections.append(Connection(inputs, gate, output))
    return connections


async def main():
    with open("./day7/input.txt") as f:
        input_data = f.read().splitlines()
    connections = parse_input_data(input_data)
    async with asyncio.TaskGroup() as tg:
        wires: dict[str, asyncio.Task[int]] = {}
        stack = deque(connections)
        while len(stack) != 0:
            conn = stack.popleft()
            if conn.output == "b":
                conn.inputs = [3176]
            inputs_in_wires = True
            gate_inputs: list[Awaitable[int] | int] = []
            for input in conn.inputs:
                match input:
                    case str(s):
                        if s not in wires.keys():
                            inputs_in_wires = False
                            break
                        else:
                            gate_inputs.append(wires[s])
                    case int(i):
                        gate_inputs.append(i)
            if not inputs_in_wires:
                stack.append(conn)
                continue
            match len(conn.inputs):
                case 1:
                    wires[conn.output] = tg.create_task(
                        unary_gate(gate_inputs[0], conn.gate)
                    )
                case 2:
                    wires[conn.output] = tg.create_task(
                        binary_gate(gate_inputs[0], gate_inputs[1], conn.gate)
                    )
    results = {k: v.result() for k, v in sorted(wires.items())}
    print(results["a"])


if __name__ == "__main__":
    asyncio.run(main())
