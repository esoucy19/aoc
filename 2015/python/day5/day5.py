import itertools


def contains_double_letter(string: str) -> bool:
    for pair in itertools.pairwise(string):
        if pair[0] == pair[1]:
            return True
    return False


def contains_three_vowels(string: str) -> bool:
    vowels = {"a", "e", "i", "o", "u"}
    vowels_found = 0
    for character in string:
        if character in vowels:
            vowels_found += 1
            if vowels_found >= 3:
                return True
    return False


def contains_naughty_pairs(string: str) -> bool:
    naughty = {"ab", "cd", "pq", "xy"}
    for pair in itertools.pairwise(string):
        if "".join(pair) in naughty:
            return True
    return False


def is_nice_string(string: str) -> bool:
    return (
        contains_double_letter(string)
        and contains_three_vowels(string)
        and not contains_naughty_pairs(string)
    )


# --- day2 ---
def contains_two_pairs(string: str) -> bool:
    for i in range(len(string)):
        # if only 3 letters remain, it is impossible to find a non-overlapping pair
        if i == len(string) - 3:
            break
        pair = string[i : i + 2]
        if pair in string[i + 2 :]:
            return True
    return False


def contains_repeating_letter(string: str) -> bool:
    for i in range(len(string)):
        # if only 2 letters remain, stop
        if i == len(string) - 2:
            break
        if string[i] == string[i + 2]:
            return True
    return False


def is_nice_string2(string: str) -> bool:
    return contains_two_pairs(string) and contains_repeating_letter(string)


if __name__ == "__main__":
    with open("./day5/input.txt") as f:
        nice_strings = 0
        while True:
            line = (f.readline()).strip()
            if not line:
                break
            if is_nice_string2(line):
                nice_strings += 1
    print(nice_strings)

