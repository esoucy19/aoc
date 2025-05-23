import sys

from more_itertools import powerset

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = filter(None, f.read().splitlines())
    containers = list(map(int, data))
    valid_combinations = list(filter(lambda cs: sum(cs) == 150, powerset(containers)))
    min_containers = min(map(len, valid_combinations))
    num_min_containers = len(
        list(filter(lambda cs: len(cs) == min_containers, valid_combinations))
    )
    print(num_min_containers)
