from day12 import day12


def test_add_all_numbers():
    assert 6 == day12.add_all_numbers([1, 2, 3])
    assert 6 == day12.add_all_numbers({"a": 2, "b": 4})
    assert 3 == day12.add_all_numbers([[[3]]])
    assert 3 == day12.add_all_numbers({"a": {"b": 4}, "c": -1})
    assert 0 == day12.add_all_numbers({"a": [-1, 1]})
    assert 0 == day12.add_all_numbers([-1, {"a": 1}])
    assert 0 == day12.add_all_numbers([])
    assert 0 == day12.add_all_numbers({})
