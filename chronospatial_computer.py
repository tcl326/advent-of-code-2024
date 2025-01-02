from typing import TypedDict, List
import copy

class Program(TypedDict):
    register_a: int
    register_b: int
    register_c: int
    idx: int
    instruction: List[int]
    output: List[int]

input_path = "data/day17_input.txt"
# input_path = "data/day17_test.txt"

with open(input_path, "r") as r:
    register_a = int(r.readline().strip().split(":")[1].strip())
    register_b = int(r.readline().strip().split(":")[1].strip())
    register_c = int(r.readline().strip().split(":")[1].strip())
    r.readline()
    instruction = [int(i) for i in r.readline().strip().split(":")[1].strip().split(",")]
    program = Program(
        register_a=register_a,
        register_b=register_b,
        register_c=register_c,
        idx=0,
        instruction=instruction,
        output=[],
    )


def get_combo(operand: int, program: Program):
    if operand < 4:
        return operand
    elif operand == 4:
        return program["register_a"]
    elif operand == 5:
        return program["register_b"]
    elif operand == 6:
        return program["register_c"]
    raise ValueError(f"invalid value: {operand}")


def step(program: Program) -> bool:
    idx = program["idx"]
    if idx >= len(program["instruction"]):
        return True
    operator = program["instruction"][idx]
    operand = program["instruction"][idx + 1]

    nidx = idx + 2
    # print(f"operator: {operator} operand: {operand}")
    # print(program)
    if operator == 0:
        v = get_combo(operand, program)
        program["register_a"] = program["register_a"] // (2 ** v)
    elif operator == 1:
        program["register_b"] = program["register_b"] ^ operand
    elif operator == 2:
        v = get_combo(operand, program)
        program["register_b"] = v % 8
    elif operator == 3:
        if program["register_a"] != 0:
            nidx = operand
    elif operator == 4:
        program["register_b"] = program["register_b"] ^ program["register_c"]
    elif operator == 5:
        v = get_combo(operand, program) % 8
        program["output"].append(v)
    elif operator == 6:
        v = get_combo(operand, program)
        program["register_b"] = program["register_a"] // (2 ** v)
    elif operator == 7:
        v = get_combo(operand, program)
        program["register_c"] = program["register_a"] // (2 ** v)
    program["idx"] = nidx
    # print(program)
    return False


def part1(program: Program) -> str:
    done = False
    while not done:
        done = step(program)

    return ",".join([str(o) for o in program["output"]])


def part2(program: Program) -> int:
    def to_value(value: List[int]) -> int:
        return sum([a * 8 ** (len(value) - i - 1) for i, a in enumerate(value)])

    def recurse(idx: int, value: List[int]):
        if idx == len(program["instruction"]):
            return to_value(value)
        value.append(0)
        for i in range(8):
            op = copy.deepcopy(program)
            value[-1] = i
            op["register_a"] = to_value(value)
            part1(op)
            res = False
            print(op, value)
            if op["output"][0] == program["instruction"][len(program["instruction"]) - idx - 1]:
                res = recurse(idx + 1, value)
                if res:
                    # print(op, value, to_value(value))
                    return res
        value.pop()
        return False

    res = recurse(0, [])
    return res



if __name__ == "__main__":
    print(part1(copy.deepcopy(program)))
    print(part2(copy.deepcopy(program)))
