from typing import TypedDict, Set, Tuple, Dict
import copy

class WareHouse(TypedDict):
    wall: Set[Tuple[int, int]]
    boxes: Set[Tuple[int, int]]
    robot: Tuple[int, int]

class WareHouseV2(TypedDict):
    wall: Set[Tuple[int, int]]
    boxes: Dict[int, Tuple[Tuple[int, int], Tuple[int, int]]]
    boxes_location: Dict[Tuple[int, int], int]
    robot = Tuple[int, int]


movements: str = ""
warehouse: WareHouse = {"wall": set(), "boxes": set(), "robot": (-1, -1)}

input_path = "data/day15_input.txt"
# input_path = "data/day15_test_s.txt"

with open(input_path, "r") as r:
    line = r.readline()
    parse_movement = False
    y = 0

    while line:
        if line == "\n":
            parse_movement = True
        elif not parse_movement:
            for x, c in enumerate(line):
                if c == "#":
                    warehouse["wall"].add((x, y))
                elif c == "O":
                    warehouse["boxes"].add((x, y))
                elif c == "@":
                    warehouse["robot"] = (x, y)
            y += 1
        else:
            movements += line.strip()
        line = r.readline()

move_map = {
    "<": (-1, 0),   # [x, y]
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
}

def visualize(warehouse: WareHouse):
    max_y = max([y for _, y in warehouse["wall"]])
    max_x = max([x for x, _ in warehouse["wall"]])
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for wx, wy in warehouse["wall"]:
        grid[wy][wx] = "#"
    for bx, by in warehouse["boxes"]:
        grid[by][bx] = "O"
    rx, ry = warehouse["robot"]
    grid[ry][rx] = "@"
    for line in grid:
        print("".join(line))


def part1(warehouse: WareHouse, movements: str) -> int:
    print(movements)
    for m in movements:
        rx, ry = warehouse["robot"]
        dx, dy = move_map[m]
        nx, ny = rx + dx, ry + dy
        if (nx, ny) not in warehouse["wall"] and (nx, ny) not in warehouse["boxes"]:
            warehouse["robot"] = (nx, ny)
        elif (nx, ny) in warehouse["wall"]:
            pass
        else:
            stack = []
            bx, by = nx, ny
            while (bx, by) in warehouse["boxes"]:
                stack.append((bx, by))
                bx, by = bx + dx, by + dy
            if (bx, by) in warehouse["wall"]:
                pass
            else:
                warehouse["robot"] = (nx, ny)
                while stack:
                    bx, by = stack.pop()
                    warehouse["boxes"].remove((bx, by))
                    warehouse["boxes"].add((bx + dx, by + dy))
        # print(f"move {m}")
        # visualize(warehouse)
    res = 0
    for bx, by in warehouse["boxes"]:
        res += bx + 100 * by
    return res

def v2_transform(warehouse: WareHouse) -> WareHouseV2:
    wall = set()
    for wx, wy in warehouse["wall"]:
        wall.add((wx * 2, wy))
        wall.add((wx * 2 + 1, wy))
    boxes = {}
    boxes_location = {}
    for idx, (bx, by) in enumerate(warehouse["boxes"]):
        boxes[idx] = ((bx * 2, by), (bx * 2 + 1, by))
        boxes_location[(bx * 2, by)] = idx
        boxes_location[(bx * 2 + 1, by)] = idx
    rx, ry = warehouse["robot"]
    return WareHouseV2(
        wall=wall,
        boxes=boxes,
        boxes_location=boxes_location,
        robot=(rx * 2, ry)
    )

def visualizev2(warehouse: WareHouseV2):
    max_y = max([y for _, y in warehouse["wall"]])
    max_x = max([x for x, _ in warehouse["wall"]])
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for wx, wy in warehouse["wall"]:
        grid[wy][wx] = "#"
    for b1, b2 in warehouse["boxes"].values():
        grid[b1[1]][b1[0]] = "["
        grid[b2[1]][b2[0]] = "]"
    rx, ry = warehouse["robot"]
    print(f"robot {rx, ry}")
    grid[ry][rx] = "@"
    for line in grid:
        print("".join(line))    


def part2(warehouse=warehouse, movements=movements):
    visualize(warehouse)
    warehousev2 = v2_transform(warehouse)
    print(movements)
    visualizev2(warehousev2)
    for m in movements:
        rx, ry = warehousev2["robot"]
        dx, dy = move_map[m]
        nx, ny = rx + dx, ry + dy
        if (nx, ny) not in warehousev2["wall"] and (nx, ny) not in warehousev2["boxes_location"]:
            warehousev2["robot"] = (nx, ny)
        elif (nx, ny) in warehousev2["wall"]:
            pass
        else:
            stack = [(rx, ry)]
            seen_boxes = []
            while stack:
                bx, by = stack.pop()
                if (bx + dx, by + dy) in warehousev2["boxes_location"]:
                    box_id = warehousev2["boxes_location"][(bx + dx, by + dy)]
                    if box_id in seen_boxes:
                        continue
                    for nbx, nby in warehousev2["boxes"][box_id]:
                        stack.append((nbx, nby))
                    seen_boxes.append(box_id)
                elif (bx + dx, by + dy) in warehousev2["wall"]:
                    break
            if (bx + dx, by + dy) in warehousev2["wall"]:
                pass
            else:
                print(f"seen boxes {seen_boxes}")
                warehousev2["robot"] = (nx, ny)
                new_locations = []
                while seen_boxes:
                    box_id = seen_boxes.pop()
                    box_location = warehousev2["boxes"][box_id]
                    new_box_location = tuple([(bx + dx, by + dy) for (bx, by) in box_location])
                    warehousev2["boxes"][box_id] = new_box_location
                    new_locations.append((new_box_location, box_id))
                    for bx, by in box_location:
                        warehousev2["boxes_location"].pop((bx, by))
                for new_boxes, box_id in new_locations:
                    for nbx, nby in new_boxes:
                        warehousev2["boxes_location"][(nbx, nby)] = box_id
                    print(f"{box_id} old location: {box_location} new location: {warehousev2["boxes"][box_id]}, {[warehousev2['boxes_location'][b] for b in warehousev2["boxes"][box_id]]}")
        print(f"move {m}")
        visualizev2(warehousev2)
        # input(f"Press Enter to continue...")
    res = 0
    for bcoords in warehousev2["boxes"].values():
        print(bcoords)
        c1, c2 = bcoords
        bx, by = c1
        res += bx + 100 * by
    return res


if __name__ == "__main__":
    print(part1(warehouse=copy.deepcopy(warehouse), movements=movements))
    print(part2(warehouse=copy.deepcopy(warehouse), movements=movements))
