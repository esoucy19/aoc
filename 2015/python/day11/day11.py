def increment(string: str) -> str:
    chars = list(string)
    ln = len(chars)
    idx = -1
    while True:
        cur = chars[idx]
        if cur == "z":
            chars[idx] = "a"
            if ln + idx == 0:
                break
            idx -= 1
        else:
            chars[idx] = chr(ord(cur) + 1)
            break
    return "".join(chars)


def rule1(string: str) -> bool:
    for idx in range(len(string) - 2):
        fst = string[idx]
        snd = string[idx + 1]
        if ord(snd) - ord(fst) == 1:
            trd = string[idx + 2]
            if ord(trd) - ord(snd) == 1:
                return True
    return False


def rule2(string: str) -> bool:
    return "i" not in string and "o" not in string and "l" not in string


def rule3(string: str) -> bool:
    pairs = set()
    npairs = 0
    for idx in range(len(string) - 1):
        cur = string[idx]
        nxt = string[idx + 1]
        if cur == nxt and cur not in pairs:
            pairs.add(cur)
            npairs += 1
            if npairs >= 2:
                break
    return npairs >= 2


def is_valid_password(string: str) -> bool:
    return all((rule1(string), rule2(string), rule3(string)))


def get_new_password(pwd: str) -> str:
    new = increment(pwd)
    while not is_valid_password(new):
        new = increment(new)
    return new


def main():
    print(get_new_password("vzbxxyzz"))


if __name__ == "__main__":
    main()
