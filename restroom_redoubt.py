from typing import TypedDict, List
import collections

input_path = "data/day14_input.txt"

class Robot(TypedDict):
    px: int
    py: int
    vx: int
    vy: int

def parse_line(line: str) -> Robot:
    pos, velocity = line.split(" ")
    def get_xy(v: str):
        syb, xy = v.split("=")
        x, y = xy.split(",")
        return int(x), int(y)
    px, py = get_xy(pos)
    vx, vy = get_xy(velocity)
    return Robot(
        px=px, py=py, vx=vx, vy=vy
    )

robots: List[Robot] = []

with open(input_path, "r") as r:
    line = r.readline()
    while line:
        robots.append(parse_line(line))
        line = r.readline()


def part1(robots: List[Robot], wide: int, tall: int) -> int:
    steps = 100
    q = [[0, 0],[0, 0]]
    for r in robots:
        x = r["px"] + steps * r["vx"]
        y = r["py"] + steps * r["vy"]
        x = x % wide
        y = y % tall
        if x == wide // 2 or y == tall // 2:
            continue
        qx = int(x > (wide // 2))
        qy = int(y > (tall // 2))
        q[qx][qy] += 1
    res = 1
    for qx in q:
        for v in qx:
            res *= v
    return res


def part2(robots: List[Robot], wide: int, tall: int) -> int:
    step = 1
    while True:
        c_x = collections.Counter()
        c_y = collections.Counter()
        for r in robots:
            x = r["px"] + step * r["vx"]
            y = r["py"] + step * r["vy"]
            x = x % wide
            y = y % tall
            c_x[x] += 1
            c_y[y] += 1

        if max(c_x.values()) > 20 or max(c_y.values()) > 20:
            grid = [["." for _ in range(wide)] for _ in range(tall)]
            for r in robots:
                x = r["px"] + step * r["vx"]
                y = r["py"] + step * r["vy"]
                x = x % wide
                y = y % tall
                c_x[x] += 1
                c_y[y] += 1
                grid[y][x] = "X"
            for line in grid:
                print("".join(line))

            input(f"Step {step}, Press Enter to continue...")
        print(step)
        step += 1


if __name__ == "__main__":
    print(part1(robots, wide=101, tall=103))
    part2(robots=robots, wide=101, tall=103)

