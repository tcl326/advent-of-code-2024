from typing import List, Tuple
import math
import heapq

input_path = "data/day18_input.txt"

byte_list = []

with open(input_path, "r") as f:
    line = f.readline()
    while line:
        byte_list.append(tuple([int(a) for a in line.split(",")]))
        line = f.readline()

headings = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def part1(byte_list: List[Tuple[int, int]], m: int, n: int):
    def score(i, j):
        return math.sqrt((m - i) ** 2 + (n - j) ** 2)
    
    start = (0, 0)
    seen = set()
    seen.add(start)
    min_queue = [(0, score(0, 0), 0, 0)]
    wall = set(byte_list)
    while min_queue:
        # print(min_queue)
        step, _, ci, cj = heapq.heappop(min_queue)
        if (ci, cj) == (m, n):
            return step
        for di, dj in headings:
            ni, nj = ci + di, cj + dj
            if ni >= 0 and ni <= m and nj >= 0 and nj <= n and (ni, nj) not in seen and (ni, nj) not in wall:
                heapq.heappush(min_queue, (step + 1, score(ni, nj), ni, nj))
                seen.add((ni, nj))
    return 0


def part2(byte_list: List[Tuple[int, int]]):
    l, r = 0, len(byte_list)
    while l < r:
        m = (l + r) // 2
        step = part1(byte_list[:m], 70, 70)
        print(l, r, m, step)
        if step == 0:
            r = m
        else:
            l = m + 1
    return byte_list[m]


if __name__ == "__main__":
    print(part1(byte_list[:1024], 70, 70))
    print(part2(byte_list))
