from typing import List
import collections

input_path = "data/day5_input.txt"

orders = []
updates = []

with open(input_path, "r") as f:
    line = f.readline()
    while line:
        line = line.strip()
        if "|" in line:
            orders.append(line.split("|"))
        elif line:
            updates.append(line.split(","))
        line = f.readline()


def part1(orders: List[List[str]], updates: List[List[str]]):
    order_dict = collections.defaultdict(set)
    rev_dict = collections.defaultdict(set)
    illegals = []
    for a, b in orders:
        order_dict[a].add(b)
        rev_dict[b].add(a)

    res = 0
    for update in updates:
        legal = True
        for i in range(1, len(update)):
            for j in range(i):
                if update[j] in rev_dict and update[i] in rev_dict[update[j]]:
                    legal = False
                    break
            if not legal:
                illegals.append(update)
                break
        else:
            res += int(update[len(update) // 2])
    return res, illegals

def part2(orders: List[List[str]], updates: List[List[str]], illegals: List[List[str]]):
    order_dict = collections.defaultdict(set)
    rev_dict = collections.defaultdict(set)
    for a, b in orders:
        order_dict[a].add(b)
        rev_dict[b].add(a)
    res = 0
    for illegal in illegals:
        for i in range(len(illegal) - 1, 0, -1):
            for j in range(i):
                if illegal[j] in rev_dict and illegal[i] in rev_dict[illegal[j]]:
                    illegal[i], illegal[j] = illegal[j], illegal[i]
        res += int(illegal[len(illegal) // 2])
    return res


if __name__ == "__main__":
    res, illegals = part1(orders, updates)
    print(res)
    print(part2(orders, updates, illegals))
