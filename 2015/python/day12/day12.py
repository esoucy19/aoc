import json

type Json = str | int | list[Json] | dict[str, Json]


def add_all_numbers(input: Json, ignore_red=False) -> int:
    total = 0
    match input:
        case str():
            pass
        case int():
            total += input
        case list():
            if input:
                total += sum(add_all_numbers(item, ignore_red) for item in input)
        case dict():
            if ignore_red:
                if "red" in input.values():
                    return 0
            if input and not (ignore_red and "red" in input.values()):
                total += sum(
                    add_all_numbers(value, ignore_red) for value in input.values()
                )
    return total


def main():
    with open("./day12/input.txt") as f:
        input = json.load(f)
    print(add_all_numbers(input))
    print(add_all_numbers(input, ignore_red=True))


if __name__ == "__main__":
    main()

