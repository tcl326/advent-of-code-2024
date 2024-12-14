from typing import List


input_path = "data/day4_input.txt"

grid = []
with open(input_path, "r") as f:
    line = f.readline()
    while line:
        grid.append(line.strip())
        line = f.readline()

directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
def search(i, j, grid, word):
    res = 0
    for di, dj in directions:
        c = 0
        ci, cj = i, j
        while ci >= 0 and ci < len(grid) and cj >= 0 and cj < len(grid[i]) and c < len(word):
            if grid[ci][cj] == word[c]:
                c += 1
                ci += di
                cj += dj
            else:
                break
        if c == len(word):
            res += 1
    return res


def part1(grid: List[str], word="XMAS"):
    res = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == word[0]:
                res += search(i, j, grid, word)
    return res

def search_x(i, j, grid):
    word = sorted("MAS")
    res = 0
    d1 = ([1, 1], [-1, -1])
    d2 = ([-1, 1], [1, -1])
    if i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[i]) - 1:
        if sorted(["A", grid[i + d1[0][0]][j + d1[0][1]], grid[i + d1[1][0]][j + d1[1][1]]]) == word:
            if sorted(["A", grid[i + d2[0][0]][j + d2[0][1]], grid[i + d2[1][0]][j + d2[1][1]]]) == word:
                res += 1
    return res


def part2(grid: List[str]):
    res = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "A":
                res += search_x(i, j, grid)
    return res


if __name__ == "__main__":
    print(part1(grid))
    print(part2(grid))