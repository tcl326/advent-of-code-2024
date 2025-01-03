from typing import List

input_path = "data/day19_input.txt"

towels = []
designs = []

with open(input_path, "r") as f:
    for p in f.readline().strip().split(","):
        towels.append(p.strip())
    _ = f.readline()
    line = f.readline()
    while line:
        designs.append(line.strip())
        line = f.readline()

# print(towels, designs)


def part1(towels: List[str], designs: List[str]):
    seen = {"": True}
    def is_possible(design: str):
        if design in seen:
            return seen[design]
        possible = False
        for towel in towels:
            if design[:len(towel)] == towel:
                future_possible = is_possible(design[len(towel):])
                possible = future_possible or possible
            if possible:
                seen[design] = possible
                return True
        seen[design] = False
        return False

    res = 0
    for d in designs:
        res += int(is_possible(d))
    return res


def part2(towels: List[str], designs: List[str]):
    seen = {"": 1}
    def is_possible(design: str):
        if design in seen:
            return seen[design]
        count = 0
        for towel in towels:
            if design[:len(towel)] == towel:
                future_count = is_possible(design[len(towel):])
                count += future_count
        seen[design] = count
        return count

    res = 0
    for d in designs:
        res += int(is_possible(d))
    return res



if __name__ == "__main__":
    print(part1(towels, designs))
    print(part2(towels, designs))
