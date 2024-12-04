from typing import List
import re

input_path = "data/day3_input.txt"

num_pattern = re.compile(r'\d+')
mul_pattern = re.compile(r'mul\(\d+,\d+\)')

mul_do_dont_pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")


memories = []
with open(input_path, "r") as f:
    line = f.readline()
    while line:
        memories.append(line.strip())
        line = f.readline()

def get_val(mul: str):
    nums = num_pattern.findall(mul)
    res = 1
    for n in nums:
        res *= int(n)
    return res

def get_mul(memory: str, start: int, end: int):
    matches = mul_pattern.findall(memory, start, end)
    # print(matches)
    return sum([get_val(m) for m in matches])


def part1(memories: List[str]):
    res = 0
    for memory in memories:
        res += get_mul(memory, 0, len(memory))
    return res

def part2(memories: List[str]):
    res = 0
    flag = True
    for memory in memories:
        matches = mul_do_dont_pattern.findall(memory)
        for m in matches:
            if m == 'do()':
                flag = True
            elif m == "don't()": 
                flag = False
            else:
                if flag:
                    res += get_val(m)
    return res



if __name__ == "__main__":
    print(part1(memories))
    print(part2(memories))
