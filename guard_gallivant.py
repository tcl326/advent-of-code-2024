from typing import List, Tuple, Set
import copy

input_path = "data/day6_input.txt"

grid = []
guard_position = None

with open(input_path, "r") as f:
    line = f.readline()
    i = 0
    while line:
        grid.append([l for l in line.strip()])
        if "^" in line:
            guard_position = (i, line.find("^"))
        i += 1
        line = f.readline()

headings = [
    (-1, 0),    # up
    (0, 1),     # right
    (1, 0),     # down
    (0, -1),    # left
]

def part1(grid: List[List[str]], guard_position: Tuple[int, int]):
    h_idx = 0
    ci, cj = guard_position
    new_grid = copy.deepcopy(grid)
    while ci >= 0 and ci < len(grid) and cj >= 0 and cj < len(grid[0]): # when the guard is in the map
        new_grid[ci][cj] = "X"
        di, dj = headings[h_idx % len(headings)]
        ni, nj = ci + di, cj + dj
        while ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == "#":
            # turn 90 degrees
            h_idx += 1
            di, dj = headings[h_idx % len(headings)]
            ni, nj = ci + di, cj + dj
        ci, cj = ni, nj

    res = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == "X":
                res += 1
    return res

def is_stuck(grid: List[List[str]], guard_position: Tuple[int, int], h_idx: int, debug_id: int):
    path_sets: Set[Tuple[int, int, int]] = set()
    ci, cj = guard_position
    while ci >= 0 and ci < len(grid) and cj >= 0 and cj < len(grid[0]): # when the guard is in the map
        if (ci, cj, h_idx) in path_sets:
            return True
        path_sets.add((ci, cj, h_idx))
        di, dj = headings[h_idx]
        ni, nj = ci + di, cj + dj
        while ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == "#":
            # turn 90 degrees
            h_idx += 1
            h_idx = h_idx % len(headings)
            di, dj = headings[h_idx]
            ni, nj = ci + di, cj + dj
        ci, cj = ni, nj
    return False

def part2(grid: List[List[str]], guard_position: Tuple[int, int]):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^" or grid[i][j] == "#":
                continue
            grid[i][j] = "#"
            res += int(is_stuck(grid, guard_position, 0, i * len(grid[i]) + j))
            grid[i][j] = "."
    return res



if __name__ == "__main__":
    print(part1(grid, guard_position))
    print(part2(grid, guard_position))
