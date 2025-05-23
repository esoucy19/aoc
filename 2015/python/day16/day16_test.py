from collections.abc import Iterable
from itertools import batched
from typing import NamedTuple

type Thing = int | None


class Things(NamedTuple):
    children: Thing = None
    cats: Thing = None
    samoyeds: Thing = None
    pomeranians: Thing = None
    akitas: Thing = None
    vizslas: Thing = None
    goldfish: Thing = None
    trees: Thing = None
    cars: Thing = None
    perfumes: Thing = None


def qualifies(scan_things: Things, aunt_things: Things) -> bool:
    for field in scan_things._fields:
        scan_thing = getattr(scan_things, field)
        aunt_thing = getattr(aunt_things, field)
        qualifies = aunt_thing == scan_thing or aunt_thing is None
        if not qualifies:
            return False
    return True


def qualifies2(scan_things: Things, aunt_things: Things) -> bool:
    for field in scan_things._fields:
        scan_thing = getattr(scan_things, field)
        aunt_thing = getattr(aunt_things, field)
        if field in {"cats", "trees"}:
            qualifies = aunt_thing is None or aunt_thing > scan_thing
        elif field in {"pomeranians", "goldfish"}:
            qualifies = aunt_thing is None or aunt_thing < scan_thing
        else:
            qualifies = aunt_thing is None or aunt_thing == scan_thing
        if not qualifies:
            return False
    return True


def parse_aunt(line: str) -> tuple[int, Things]:
    words = line.strip("\n").split(" ")
    words = map(lambda w: w.strip(":,"), words)
    pairs = map(lambda p: (p[0], int(p[1])), batched(words, 2))
    num = next(pairs)[1]
    things = Things(**dict(pairs))
    return (num, things)


def main(scan_things: Things, aunts: Iterable[tuple[int, Things]]) -> None:
    result = filter(lambda aunt: qualifies2(scan_things, aunt[1]), aunts)
    for aunt in result:
        print(aunt[0])


if __name__ == "__main__":
    with open("./day16/input.txt") as f:
        # with open("./input.txt") as f:
        data = f.read().splitlines()
    aunts = map(parse_aunt, filter(lambda line: len(line) > 0, data))
    scan_things = Things(
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )
    main(scan_things, aunts)
