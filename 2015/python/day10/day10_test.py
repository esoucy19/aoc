from day10.day10 import (
    _parse,
    _split_groups,
    _count_groups,
    _concat_counts,
    look_and_say,
)


def test_look_and_says():
    assert look_and_say("1") == "11"
    assert look_and_say("11") == "21"
    assert look_and_say("21") == "1211"
    assert look_and_say("1211") == "111221"
    assert look_and_say("111221") == "312211"


def test__parse():
    assert _parse("1") == ((1, "1"),)
    assert _parse("11") == ((2, "1"),)
    assert _parse("21") == ((1, "2"), (1, "1"))
    assert _parse("1211") == ((1, "1"), (1, "2"), (2, "1"))
    assert _parse("111221") == ((3, "1"), (2, "2"), (1, "1"))


def test__split_groups():
    assert _split_groups("1") == ("1",)
    assert _split_groups("11") == ("11",)
    assert _split_groups("21") == ("2", "1")
    assert _split_groups("1211") == ("1", "2", "11")
    assert _split_groups("111221") == ("111", "22", "1")


def test__count_groups():
    assert _count_groups(("1",)) == ((1, "1"),)
    assert _count_groups(("11",)) == ((2, "1"),)
    assert _count_groups(("2", "1")) == ((1, "2"), (1, "1"))
    assert _count_groups(("1", "2", "11")) == ((1, "1"), (1, "2"), (2, "1"))
    assert _count_groups(("111", "22", "1")) == ((3, "1"), (2, "2"), (1, "1"))


def test__concat_counts():
    assert _concat_counts(((1, "1"),)) == "11"
    assert _concat_counts(((2, "1"),)) == "21"
    assert _concat_counts(((1, "2"), (1, "1"))) == "1211"
    assert _concat_counts(((1, "1"), (1, "2"), (2, "1"))) == "111221"
    assert _concat_counts(((3, "1"), (2, "2"), (1, "1"))) == "312211"
