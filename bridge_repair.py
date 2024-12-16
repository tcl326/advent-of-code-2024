from typing import List, Callable

import operator

input_path = "data/day7_input.txt"

test_values = []
number_list = []

with open(input_path, "r") as f:
    line = f.readline()
    while line:
        test_value, numbers = line.strip().split(":")
        test_values.append(int(test_value))
        number_list.append([int(n) for n in numbers.strip().split()])
        line = f.readline()


# print(list(zip(test_values, number_list)))
def possible(test_value: int, numbers: List[int], operators: List[Callable[[int, int], int]] = [operator.mul, operator.add]) -> bool:
    stack = [(0, numbers[0])]
    while stack:
        idx, n = stack.pop()
        idx += 1
        if idx == len(numbers):
            if test_value == n:
                return True
        else:
            for op in operators:
                stack.append((idx, op(n, numbers[idx])))
    return False


def part1(test_values: List[int], number_list: List[List[int]]):
    res = 0
    for v, n in zip(test_values, number_list):
        if possible(v, n):
            res += v
    return res


def part2(test_values: List[int], number_list: List[List[int]]):
    def concat(a: int, b: int) -> int:
        return int(str(a) + str(b))
    res = 0
    for v, n in zip(test_values, number_list):
        if possible(v, n, operators=[operator.mul, operator.add, concat]):
            res += v
    return res


if __name__ == "__main__":
    print(part1(test_values, number_list))
    print(part2(test_values, number_list))
