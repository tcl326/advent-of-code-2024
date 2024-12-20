from typing import List, Tuple, Set

input_path = "data/day12_input.txt"
# input_path = "data/day12_test.txt"

grid = []
with open(input_path, "r") as f:
    line = f.readline()
    while line:
        grid.append(line.strip())
        line = f.readline()


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_group(pos: Tuple[int, int], grid: List[str]) -> Tuple[int, int, Set[Tuple[int, int]]]:
    area = set()
    perimeter = 0
    stack = []
    stack.append(pos)
    area.add(pos)
    symbol = grid[pos[0]][pos[1]]
    while stack:
        ci, cj = stack.pop()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if (ni, nj) not in area:
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni]):
                    if grid[ni][nj] == symbol:
                        area.add((ni, nj))
                        stack.append((ni, nj))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
    return len(area), perimeter, area


def part1(grid: List[str]):
    seen = set()
    res = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if (i, j) in seen:
                continue
            area, perimeter, seen_ = find_group((i, j), grid)
            res += area * perimeter
            seen = seen.union(seen_)
            print(f"garden {c} at {(i, j)} has area {area} and perimeter {perimeter}")

    return res


corner_map = {
    ((0, True), (1, True), (2, True), (3, True)): 0,    # surrounded
    # """
    # a a
    #  x
    # a a
    # """
    ((0, False), (1, True), (2, True), (3, True)): 1, 
    ((0, True), (1, False), (2, True), (3, True)): 1, 
    ((0, True), (1, True), (2, False), (3, True)): 1, 
    ((0, True), (1, True), (2, True), (3, False)): 1, 
    # """
    # a b
    #  x 
    # a a
    # """
    ((0, False), (1, False), (2, True), (3, True)): 0,   # bottom right corner
    ((0, True), (1, False), (2, False), (3, True)): 0,   # bottom right corner
    ((0, True), (1, True), (2, False), (3, False)): 0,   # bottom right corner
    ((0, False), (1, True), (2, True), (3, False)): 0,   # bottom right corner
    # """
    # a b
    #  x
    # a b
    # """
    ((0, False), (1, True), (2, False), (3, True)): 2,   # bottom left corner
    ((0, True), (1, False), (2, True), (3, False)): 2,   # bottom left corner
    # """
    # a b
    #  x
    # b a
    # """
    ((0, False), (1, False), (2, False), (3, True)): 1,   # top left corner
    ((0, True), (1, False), (2, False), (3, False)): 1,   # bottom right corner
    ((0, False), (1, True), (2, False), (3, False)): 1,   # bottom right corner
    ((0, False), (1, False), (2, True), (3, False)): 1,   # bottom right corner
    # """
    # a b
    #  x
    # b b
    # """
    ((0, False), (1, False), (2, False), (3, False)): 0,   # top right/bottom right corner
    # """
    # b b
    #  x
    # b b
    # """
}

corner_coords = [
    ((-1, 1), (0, 1), (0, 0), (-1, 0)),     # top right corner
    ((0, 1), (1, 1), (1, 0), (0, 0)),       # bottom right corner
    ((0, 0), (1, 0), (1, -1), (0, -1)),
    ((0, -1), (0, 0), (-1, 0), (-1, -1))
]

def find_corners(coord_set: Set[Tuple[int, int]]):
    corners = set()
    count = 0
    for i, j in coord_set:
        for corner_coord in corner_coords:
            corner_idx = tuple((h, (i + di, j + dj) in coord_set) for h, (di, dj) in enumerate(corner_coord))
            seen = tuple(sorted([(i + di, j + dj) for di, dj in corner_coord]))
            if seen in corners:
                continue
            val = corner_map[corner_idx]
            count += val
            if val:
                corners.add(seen)
    max_i = max(i for i, _ in coord_set)
    min_i = min(i for i, _ in coord_set)
    max_j = max(j for _, j in coord_set)
    min_j = min(j for _, j in coord_set)
    grid = [["." for _ in range(max_j - min_j + 1)] for _ in range(max_i - min_i + 1)]
    for ci, cj in coord_set:
        grid[ci - min_i][cj - min_j] = "X"
    if count > 90:
        for line in grid:
            print("".join(line))
    return count



def part2(grid: List[str]):
    seen = set()
    res = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if (i, j) in seen:
                continue
            area, perimeter, seen_ = find_group((i, j), grid)
            side = find_corners(seen_)
            res += area * side
            seen = seen.union(seen_)
            print(side, (i, j))
            # print(f"garden {c} at {(i, j)} has area {area} and side {side}")

    return res


if __name__ == "__main__":
    print(part1(grid))
    print(part2(grid))
