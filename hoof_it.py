from typing import List, Tuple

input_path = "data/day10_input.txt"
# input_path = "data/day10_test.txt"

grid = []
starting_positions = []
with open(input_path, "r") as f:
    line = f.readline()
    idx = 0
    while line:
        grid.append(line.strip())
        for i, l in enumerate(line):
            if l == "0":
                starting_positions.append((idx, i))
        idx += 1
        line = f.readline()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def part1(grid, starting_positions: List[Tuple[str, int]], goal: str):
    memo = set()
    def recurse(pos):
        i, j = pos
        if grid[i][j] == goal:
            return {(i, j)}
        res = set()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni]) and (ni, nj) not in memo:
                if grid[ni][nj] == str(int(grid[i][j]) + 1):
                    # print(ni, nj, grid[ni][nj], grid[i][j])
                    memo.add((ni, nj))
                    res = res.union(recurse((ni, nj)))
                    memo.remove((ni, nj)) 
        return res
    res = 0
    for si, sj in starting_positions:
        memo.add((si, sj))
        v = recurse((si, sj))
        print((si, sj), v)
        res += len(v)
        memo.remove((si, sj))
    return res


def part2(grid, starting_positions: List[Tuple[str, int]], goal: str):
    memo = set()
    def recurse(pos):
        i, j = pos
        if grid[i][j] == goal:
            return 1
        res = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni]) and (ni, nj) not in memo:
                if grid[ni][nj] == str(int(grid[i][j]) + 1):
                    # print(ni, nj, grid[ni][nj], grid[i][j])
                    memo.add((ni, nj))
                    res += recurse((ni, nj))
                    memo.remove((ni, nj)) 
        return res
    res = 0
    for si, sj in starting_positions:
        memo.add((si, sj))
        v = recurse((si, sj))
        print((si, sj), v)
        res += v
        memo.remove((si, sj))
    return res


if __name__ == "__main__":
    print(starting_positions)
    print(part1(grid, starting_positions=starting_positions, goal="9"))
    print(part2(grid, starting_positions=starting_positions, goal="9"))
