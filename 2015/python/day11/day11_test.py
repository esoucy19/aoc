from day11 import day11


def test_increment():
    assert day11.increment("a") == "b"
    assert day11.increment("z")[-1] == "a"
    assert day11.increment("aa") == "ab"
    assert day11.increment("az") == "ba"
    assert day11.increment("azz") == "baa"


def test_rule1():
    assert day11.rule1("abc")
    assert day11.rule1("bcd")
    assert day11.rule1("xyz")
    assert not day11.rule1("abd")
    assert day11.rule1("xyzzzzzzzz")
    assert day11.rule1("zzzzzzzabc")
    assert day11.rule1("zzzabcffff")
    assert day11.rule1("hijklmmn")
    assert not day11.rule1("abbceffg")


def test_rule2():
    assert not day11.rule2("i")
    assert not day11.rule2("o")
    assert not day11.rule2("l")
    assert day11.rule2("aaa")
    assert not day11.rule2("hijklmmn")


def test_rule3():
    assert day11.rule3("aabb")
    assert not day11.rule3("aaaa")
    assert not day11.rule3("abcd")
    assert not day11.rule3("aabc")
    assert day11.rule3("abbceffg")
    assert not day11.rule3("abbcegjk")


def test_is_valid_password():
    assert not day11.is_valid_password("hijklmmn")
    assert not day11.is_valid_password("abbceffg")
    assert not day11.is_valid_password("abbcegjk")
    assert day11.is_valid_password("abcdffaa")
    assert day11.is_valid_password("ghjaabcc")


def test_get_new_password():
    assert day11.get_new_password("abcdefgh") == "abcdffaa"
    assert day11.get_new_password("ghijklmn") == "ghjaabcc"
