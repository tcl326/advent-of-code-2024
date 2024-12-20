import re
import math
from typing import TypedDict, List


input_path = "data/day13_input.txt"

class Coord(TypedDict):
    x: int
    y: int

class Game(TypedDict):
    a: Coord
    b: Coord
    prize: Coord

digits_pattern = re.compile(r'\d+')

games = []
with open(input_path, "r") as r:
    line_a = r.readline()
    while line_a:
        a, b = digits_pattern.findall(line_a)
        button_a = Coord(x=int(a), y=int(b))
        line_b = r.readline()
        a, b = digits_pattern.findall(line_b)
        button_b = Coord(x=int(a), y=int(b))
        line_p = r.readline()
        a, b = digits_pattern.findall(line_p)
        prize = Coord(x=int(a), y=int(b))
        line_s = r.readline()
        game = Game(a=button_a, b=button_b, prize=prize)
        games.append(game)
        line_a = r.readline()


def min_token(game: Game):
    token = None
    prize = game["prize"]
    for i in range(100):
        for j in range(100):
            if prize["x"] == (game["a"]["x"] * i + game["b"]["x"] * j) and prize["y"] == (game["a"]["y"] * i + game["b"]["y"] * j):
                if token is None:
                    token = i * 3 + j
                else:
                    token = min(token, i * 3 + j)
    return token if token else 0

def part1(games: List[Game]):
    token = 0
    for g in games:
        token += solve(g, 0)
    return token

"""
13a + 71b = 6289
42a + 29b = 6091
"""
def solve(game: Game, p_correction = 10000000000000):

    ax = game["a"]["x"]
    ay = game["a"]["y"]

    bx = game["b"]["x"]
    by = game["b"]["y"]

    cx = game["prize"]["x"] + p_correction
    cy = game["prize"]["y"] + p_correction

    b = (cy - ay * (cx / ax)) / (ay * (-bx / ax) + by)
    a = (cx - (bx * b)) / ax

    print(f"{ax}a + {bx}b = {cx}")
    print(f"{ay}a + {by}b = {cy}")
    print(f"a = {a}")
    print(f"b = {b}")
    if abs(round(a) - a) > 0.001 or abs(round(b) - b) > 0.001:
        print(round(a), a, round(b), b)
        print("not possible")
        return 0
    return 3 * a + b

def part2(games: List[Game]):
    token = 0
    for g in games:
        token += solve(g)
    return token



if __name__ == "__main__":
    print(part1(games))
    print(part2(games))