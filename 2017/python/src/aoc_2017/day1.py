from collections.abc import Sequence
from functools import partial, reduce
from itertools import chain, starmap
from operator import eq

from toolz import compose, first, sliding_window, take

digits = partial(map, int)
head = partial(take, 1)


def cycle[T](seq: Sequence[T]) -> list[T]:
    return list(chain(seq, head(seq)))


pairs = partial(sliding_window, 2)
is_matching_pair = partial(reduce, eq)
matching_pairs = partial(filter, is_matching_pair)
item = partial(map, first)
captcha = compose(
    sum,
    partial(map, first),
    partial(filter, is_matching_pair),
    pairs,
    cycle,
    partial(map, int),
)
