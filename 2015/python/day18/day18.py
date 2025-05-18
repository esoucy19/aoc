import sys
from collections import Counter
from copy import copy
from itertools import chain, product

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        input_data = list(map(list, filter(None, f.read().splitlines())))
    grid_size = len(input_data[0])
    end_idx = grid_size - 1
    cur_grid = copy(input_data)
    cur_grid[0][0] = "#"
    cur_grid[0][end_idx] = "#"
    cur_grid[end_idx][0] = "#"
    cur_grid[end_idx][end_idx] = "#"
    for _ in range(grid_size):
        nxt_grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
        for x, y in product(range(grid_size), repeat=2):
            light = cur_grid[x][y]
            neighbors_coord = [
                (x + a, y + b)
                for a in (-1, 0, 1)
                for b in (-1, 0, 1)
                if (a, b) != (0, 0)
            ]
            neighbors = []
            for i, j in neighbors_coord:
                if i < 0 or j < 0 or i >= len(cur_grid) or j >= len(cur_grid[0]):
                    neighbors.append(".")
                else:
                    neighbors.append(cur_grid[i][j])
            counts = Counter(neighbors)
            if light == "#":
                if 2 <= counts["#"] <= 3:
                    nxt_grid[x][y] = "#"
            elif counts["#"] == 3:
                nxt_grid[x][y] = "#"
            # part 2
            nxt_grid[0][0] = "#"
            nxt_grid[0][end_idx] = "#"
            nxt_grid[end_idx][0] = "#"
            nxt_grid[end_idx][end_idx] = "#"
        cur_grid = nxt_grid
    print(Counter(chain(*cur_grid)))
