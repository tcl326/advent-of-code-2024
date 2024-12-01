import collections

input_path = "data/day1_input.txt"

left_list = []
right_list = []
with open(input_path, "r") as f:
    line = f.readline()
    while line:
        l, r = line.split()
        left_list.append(int(l))
        right_list.append(int(r))
        line = f.readline()

def part1(left_list, right_list):
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    return sum([abs(l - r) for l, r in zip(left_list, right_list)])

def part2(left_list, right_list):
    right_count = collections.Counter(right_list)
    sim_score = 0
    for l in left_list:
        sim_score += l * right_count.get(l, 0)
    return sim_score


if __name__ == "__main__":
    print(part1(left_list, right_list))
    print(part2(left_list, right_list))
