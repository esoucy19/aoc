def find_floor(directions: str) -> int:
    floor = 0
    for d in directions:
        match d:
            case "(":
                floor += 1
            case ")":
                floor -= 1
    return floor


def first_basement(directions: str) -> int:
    position = 1
    floor = 0
    for d in directions:
        match d:
            case "(":
                floor += 1
            case ")":
                floor -= 1
        if floor <= -1:
            break
        position += 1
    return position


if __name__ == "__main__":
    with open("./day1/input.txt") as f:
        data = f.read()
    # print(find_floor(data))
    print(first_basement(data))
