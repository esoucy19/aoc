from day12 import day12


def test_add_all_numbers():
    assert day12.add_all_numbers([1, 2, 3]) == 6
    assert day12.add_all_numbers({"a": 2, "b": 4}) == 6
    assert day12.add_all_numbers([[[3]]]) == 3
    assert day12.add_all_numbers({"a": {"b": 4}, "c": -1}) == 3
    assert day12.add_all_numbers({"a": [-1, 1]}) == 0
    assert day12.add_all_numbers([-1, {"a": 1}]) == 0
    assert day12.add_all_numbers([]) == 0
    assert day12.add_all_numbers({}) == 0
