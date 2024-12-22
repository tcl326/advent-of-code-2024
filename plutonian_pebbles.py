from typing import List
import collections

input_path = "data/day11_input.txt"

stones = [125, 17]
with open(input_path, "r") as f:
    stones = [int(l) for l in f.readline().strip().split()]


def part1(stones: List[int], steps: int = 25) -> int:
    for i in range(steps):
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif len(str(s)) % 2 == 0:
                str_s = str(s)
                new_stones.append(int(str_s[:len(str_s)//2]))
                new_stones.append(int(str_s[len(str_s)//2:]))
            else:
                new_stones.append(s * 2024)
        stones = new_stones
    return len(new_stones)


def part2(stones: List[int], steps: int = 25) -> int:
    stone_collection = collections.Counter(stones)
    for i in range(steps):
        new_stone_collection = collections.Counter()
        for s, c in stone_collection.items():
            if s == 0:
                new_stone_collection[1] += c
            elif len(str(s)) % 2 == 0:
                str_s = str(s)
                new_stone_collection[int(str_s[:len(str_s)//2])] += c
                new_stone_collection[int(str_s[len(str_s)//2:])] += c
            else:
                new_stone_collection[s * 2024] += c
        stone_collection = new_stone_collection
    return sum(list(new_stone_collection.values()))


if __name__ == "__main__":
    print(part1(stones, steps=25))
    print(part2(stones, steps=75))
