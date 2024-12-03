
input_path = "data/day2_input.txt"

reports = []

with open(input_path, "r") as f:
    line = f.readline()
    while line:
        report = [int(a) for a in line.split()]
        reports.append(report)
        line = f.readline()


def is_safe(report, min_diff: int = 1, max_diff: int = 3):
    pos_diff_count = 0
    neg_diff_count = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff > 0:
            pos_diff_count += 1
        if diff < 0:
            neg_diff_count += 1
        if abs(diff) < min_diff or abs(diff) > max_diff:
            return False
    return pos_diff_count == (len(report) - 1) or neg_diff_count == (len(report) - 1)


def part1(reports):
    safe_count = 0
    for report in reports:
        safe = is_safe(report)
        safe_count += int(safe)
    return safe_count


def part2(reports):
    safe_count = 0
    for report in reports:
        safe = is_safe(report)
        if not safe:
            for i in range(len(report)):
                safe = is_safe(report[:i] + report[i + 1:])
                if safe:
                    break
        safe_count += int(safe)
    return safe_count


if __name__ == "__main__":
    print(part1(reports))
    print(part2(reports))
