import itertools


def main():
    with open("./day9/input.txt") as f:
        lines = f.read().splitlines()
        lines_words = (line.split(" ") for line in lines if line)
        triples = [(words[0], words[2], int(words[4])) for words in lines_words]
        dataset = dict()
        for triple in triples:
            begin, end, distance = triple
            if begin not in dataset:
                dataset[begin] = dict()
            if end not in dataset:
                dataset[end] = dict()
            dataset[begin][end] = distance
            dataset[end][begin] = distance
        locations = dataset.keys()
        routes = list(itertools.permutations(locations))
        routes_pairs = [list(itertools.pairwise(route)) for route in routes]
        routes_distances = [
            [dataset[pair[0]][pair[1]] for pair in route] for route in routes_pairs
        ]
        routes_sums = [sum(route) for route in routes_distances]
        print(max(routes_sums))


if __name__ == "__main__":
    main()
