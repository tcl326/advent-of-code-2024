import collections
import copy
from typing import Dict, Set, Tuple, List

input_path = "data/day8_input.txt"

grid = []
with open(input_path, "r") as f:
    line = f.readline()
    while line:
        grid.append(line.strip())
        line = f.readline()


antenna_coords: Dict[str, Set[Tuple[int, int]]] = collections.defaultdict(set)

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c != ".":
            antenna_coords[c].add((i, j))

def generate_antinodes(antenna: str, coords: List[Tuple[int, int]], repeat: bool = False, grid: List[str] = grid):
    antinodes = set()
    for i, (ci, cj) in enumerate(coords):
        for ni, nj in coords[i + 1:]:
            di, dj = ci - ni, cj - nj
            antinodes.add((ci + di, cj + dj))
            n = 0
            ai, aj = ci + n * di, cj + n * dj
            while repeat and ai >= 0 and ai < len(grid) and aj >= 0 and aj < len(grid[0]):
                antinodes.add((ai, aj))
                n += 1
                ai, aj = ci + n * di, cj + n * dj
            antinodes.add((ni - di, nj - dj))
            n = 0
            ai, aj = ni - n * di, nj - n * dj
            while repeat and ai >= 0 and ai < len(grid) and aj >= 0 and aj < len(grid[0]):
                antinodes.add((ai, aj))
                n += 1
                ai, aj = ni - n * di, nj - n * dj

    return antinodes


def part1(antenna_coords: Dict[str, Set[Tuple[int, int]]], grid: List[str]):
    m = len(grid)
    n = len(grid[0])
    antinodes = set()
    res = 0
    for antenna, coords in antenna_coords.items():
        antinodes = antinodes.union(generate_antinodes(antenna, list(coords)))
    for node in antinodes:
        ni, nj = node
        if ni >= 0 and ni < m and nj >= 0 and nj < n:
            res += 1
    return res

def part2(antenna_coords: Dict[str, Set[Tuple[int, int]]], grid: List[str]):
    m = len(grid)
    n = len(grid[0])
    antinodes = set()
    res = 0
    for antenna, coords in antenna_coords.items():
        antinodes = antinodes.union(generate_antinodes(antenna, list(coords), repeat=True, grid=grid))
    for node in antinodes:
        ni, nj = node
        if ni >= 0 and ni < m and nj >= 0 and nj < n:
            res += 1
    debug_grid = copy.deepcopy(grid)
    return res


if __name__ == "__main__":
    print(part1(antenna_coords=antenna_coords, grid=grid))
    print(part2(antenna_coords=antenna_coords, grid=grid))
