from day1 import find_floor


def test_find_floor() -> None:
    assert find_floor("(())") == find_floor("()()") == 0
    assert find_floor("(((") == find_floor("(()(()(") == 3
    assert find_floor("))(((((") == 3
    assert find_floor("())") == find_floor("))(") == -1
    assert find_floor(")))") == find_floor(")())())") == -3
