from collections.abc import Iterable


def look_and_say(numbers: str) -> str:
    return _concat_counts(_parse(numbers))


def _parse(numbers: str) -> tuple[tuple[int, str]]:
    return _count_groups(_split_groups(numbers))


def _split_groups(s: str) -> tuple[str]:
    current = ""
    groups = []
    group = []
    for c in s:
        if not current:
            current = c
        if c != current:
            groups.append("".join(group))
            group = []
            current = c
        group.append(c)
    groups.append("".join(group))
    return tuple(groups)


def _count_groups(groups: Iterable[str]) -> tuple[tuple[int, str]]:
    counts = []
    for group in groups:
        c = group[0]
        count = len(group)
        counts.append((count, c))
    return tuple(counts)


def _concat_counts(counts: Iterable[tuple[int, str]]) -> str:
    acc = []
    for count in counts:
        n, c = count
        acc.append(str(n))
        acc.append(c)
    return "".join(acc)


def main():
    input = "1321131112"
    iterations = 50
    acc = input
    for _ in range(iterations):
        acc = look_and_say(acc)
    print(len(acc))


if __name__ == "__main__":
    main()
