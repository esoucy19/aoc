import day19


def test_hohoho() -> None:
    replacements = frozenset((("H", "HO"), ("H", "OH"), ("O", "HH")))
    input_string = "HOH"
    with open("test") as fd:
        print(fd.read())

    expected = frozenset(("HOOH", "HOHO", "OHOH", "HOOH", "HHHH"))
    received = frozenset(day19.make_new_molecules(input_string, replacements))
    assert received == expected
