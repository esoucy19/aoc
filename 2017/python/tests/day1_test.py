import pytest

from aoc_2017 import day1

examples = (
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9),
)


def test_digits():
    assert list(day1.digits("123")) == [1, 2, 3]


def test_cycle():
    assert day1.cycle([1, 2, 3]) == [1, 2, 3, 1]


def test_pairs():
    assert list(day1.pairs([1, 2, 3, 1])) == [(1, 2), (2, 3), (3, 1)]


def test_is_matching_pair():
    assert day1.is_matching_pair([1, 1]) == True
    assert day1.is_matching_pair([1, 2]) == False


@pytest.mark.parametrize(["giv", "exp"], examples)
def test_captcha(giv, exp):
    assert day1.captcha(giv) == exp
