from typing import List, Tuple
import collections
import heapq

input_path = "data/day16_input.txt"

start = (-1, -1)
end = (-1, -1)
grid = []
with open(input_path, "r") as r:
    line = r.readline()
    i = 0
    while line:
        grid.append(line.strip())
        if "S" in line:
            j = line.find("S")
            start = (i, j)
        if "E" in line:
            j = line.find("E")
            end = (i, j)
        line = r.readline()
        i += 1


headings = [
    (0, 1), # East
    (1, 0), # South
    (0, -1), # West
    (-1, 0), # North
]


def part1(grid: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    stack = [(0, start, 0)]
    seen = {}
    while stack:
        score, (ci, cj), hidx = heapq.heappop(stack)
        if (ci, cj) == end:
            return score
        if (ci, cj, hidx) in seen:
            if score > seen[(ci, cj, hidx)]:
                continue
        seen[(ci, cj, hidx)] = score
        counterhdx = (hidx - 1) % len(headings)
        clockhdx = (hidx + 1) % len(headings)
        heapq.heappush(stack, (score + 1000, (ci, cj), counterhdx))
        heapq.heappush(stack, (score + 1000, (ci, cj), clockhdx))
        di, dj = headings[hidx]
        ni, nj = ci + di, cj + dj
        if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni]) and grid[ni][nj] != "#":
            heapq.heappush(stack, (score + 1, (ci + di, cj + dj), hidx))
    return 0

def part2(grid: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    visited = {}
    heap = [(0, 0, *start, {start})]
    lowest_score = None
    winning_paths = set()

    def can_visit(d, i, j, score):
        p_score = visited.get((d, i, j))
        if p_score and p_score < score:
            return False
        visited[(d, i, j)] = score
        return True
    
    while heap:
        score, d, i, j, path = heapq.heappop(heap)
        if lowest_score and lowest_score < score:
            break

        if (i, j) == end:
            lowest_score = score
            winning_paths |= path
            continue
        
        if not can_visit(d, i, j, score):
            continue
        
        di, dj = headings[d]
        ni, nj = i + di, j + dj
        if grid[ni][nj] != "#" and can_visit(d, ni, nj, score + 1):
            heapq.heappush(heap, (score + 1, d, ni, nj, path | {(ni, nj)}))
        
        counterhdx = (d - 1) % len(headings)
        if can_visit(counterhdx, i, j, score + 1000):
            heapq.heappush(heap, (score + 1000, counterhdx, i, j, path))

        clockhdx = (d + 1) % len(headings)
        if can_visit(clockhdx, i, j, score + 1000):
            heapq.heappush(heap, (score + 1000, clockhdx, i, j, path))

    return len(winning_paths)


if __name__ == "__main__":
    print(part1(grid, start, end))
    print(part2(grid, start, end))
