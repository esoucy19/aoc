import contextlib
import pathlib
from collections.abc import Generator
from typing import Final, TextIO

from toolz import curry

DATA: Final = pathlib.Path("data/")


@contextlib.contextmanager
def open_(path: pathlib.Path) -> Generator[TextIO]:
    fd = path.open("r", encoding="utf8")
    try:
        yield fd
    finally:
        fd.close()


def read_file(file: pathlib.Path) -> str:
    with open_(file) as fd:
        return fd.read().strip()


def read_day_input(day: int) -> str:
    return read_file(DATA / f"day{day}.txt")
