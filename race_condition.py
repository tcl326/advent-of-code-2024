from typing import List, Tuple, Set, Dict
import copy


input_path = "data/day20_input.txt"

maze: List[str] = []
start_position: Tuple[int, int] = (-1, -1)
end_position: Tuple[int, int] = (-1, -1)

with open(input_path, "r") as f:
    line = f.readline()
    i = 0
    while line:
        maze.append(line.strip())
        if "S" in line:
            j = line.find("S")
            start_position = (i, j)
        if "E" in line:
            j = line.find("E")
            end_position = (i, j)
        line = f.readline()
        i += 1

headings = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def part1(maze: List[str], start: Tuple[int, int], end: Tuple[int, int]):

    def visualize(score_map):
        viz_maze = copy.deepcopy(maze)
        for (i, j), score in score_map.items():
            viz_maze[i] = viz_maze[i][:j] + str(score % 10) + viz_maze[i][j+1:]
        for line in viz_maze:
            print(line)
        print()

    def bfs(start, maze):
        seen = {}
        stack = [(0, *start)]
        while stack:
            score, ci, cj = stack.pop()
            if (ci, cj) in seen:
                continue
            seen[(ci, cj)] = score
            for di, dj in headings:
                ni, nj = ci + di, cj + dj
                if ni >= 0 and ni < len(maze) and nj >= 0 and nj < len(maze[ni]) and maze[ni][nj] != "#" and (ni, nj) not in seen:
                    stack.append((score + 1, ni, nj))
        return seen
        

    score_map = bfs(end, maze)

    def find_cheats(score_map, maze):
        cheats = {}
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "#":
                    for di, dj in headings:
                        pi, pj = i - di, j - dj
                        ni, nj = i + di, j + dj
                        if (pi, pj) in score_map and (ni, nj) in score_map:
                            if score_map[(pi, pj)] - score_map[(ni, nj)] > 0:
                                cheats[(pi, pj, ni, nj)] = score_map[(pi, pj)] - score_map[(ni, nj)] - 1
        return cheats
    
    cheats = find_cheats(score_map, maze)
    return len([s for s in cheats.values() if s >= 100])

def part2(maze: List[str], start: Tuple[int, int], end: Tuple[int, int]):
    def visualize(score_map):
        viz_maze = copy.deepcopy(maze)
        for (i, j), score in score_map.items():
            viz_maze[i] = viz_maze[i][:j] + str(score % 10) + viz_maze[i][j+1:]
        for line in viz_maze:
            print(line)
        print()

    def bfs(start, maze):
        seen = {}
        stack = [(0, *start)]
        while stack:
            score, ci, cj = stack.pop()
            if (ci, cj) in seen:
                continue
            seen[(ci, cj)] = score
            for di, dj in headings:
                ni, nj = ci + di, cj + dj
                if ni >= 0 and ni < len(maze) and nj >= 0 and nj < len(maze[ni]) and maze[ni][nj] != "#" and (ni, nj) not in seen:
                    stack.append((score + 1, ni, nj))
        return seen
        

    score_map = bfs(end, maze)

    def find_cheats(score_map: Dict[Tuple[int, int], int], max_distance: int):
        cheats = {}
        for (si, sj), s_score in score_map.items():
            for (ei, ej), e_score in score_map.items():
                if s_score > e_score:
                    # this is a cheat
                    if (abs(si - ei) + abs(sj - ej)) <= (max_distance):
                        # ensure the hamilton distance is less than or equal to max_distance
                        cheats[(si, sj, ei, ej)] = s_score - e_score - (abs(si - ei) + abs(sj - ej))
        return cheats
    
    cheats = find_cheats(score_map, 20)
    return len([s for s in cheats.values() if s >=100])


if __name__ == "__main__":
    print(part1(maze, start_position, end_position))
    print(part2(maze, start_position, end_position))
