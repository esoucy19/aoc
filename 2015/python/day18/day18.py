import sys
from collections import Counter
from copy import copy
from itertools import chain

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = list(map(list, filter(None, f.read().splitlines())))
    cur_grid = copy(data)
    cur_grid[0][0] = "#"
    cur_grid[0][99] = "#"
    cur_grid[99][0] = "#"
    cur_grid[99][99] = "#"
    for _ in range(100):
        nxt_grid = [["." for _ in range(100)] for _ in range(100)]
        for x, y in [(x, y) for x in range(100) for y in range(100)]:
            light = cur_grid[x][y]
            neighbors_coord = [
                (x + a, y + b)
                for a in [-1, 0, 1]
                for b in [-1, 0, 1]
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
            else:
                if counts["#"] == 3:
                    nxt_grid[x][y] = "#"
            # part 2
            nxt_grid[0][0] = "#"
            nxt_grid[0][99] = "#"
            nxt_grid[99][0] = "#"
            nxt_grid[99][99] = "#"
        cur_grid = nxt_grid
    print(Counter(chain(*cur_grid)))
