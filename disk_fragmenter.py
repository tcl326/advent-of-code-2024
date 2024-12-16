

input_path = "data/day9_input.txt"

disk_map = "2333133121414131402"

with open(input_path, "r") as f:
    disk_map = f.readline().strip()


def part1(disk_map: str) -> int:
    expanded_disk = []
    for i, d in enumerate(disk_map):
        if i % 2 == 0:
            expanded_disk.extend([i // 2] * int(d))
        else:
            expanded_disk.extend([None] * int(d))
    # print(expanded_disk)
    idx, lidx = 0, len(expanded_disk) - 1
    while idx < lidx: 
        if expanded_disk[lidx] is None:
            lidx -= 1
        elif expanded_disk[idx] is not None:
            idx += 1
        elif expanded_disk[idx] is None:
            v = expanded_disk[lidx]
            expanded_disk[idx] = v
            expanded_disk[lidx] = None
            idx += 1
            lidx -= 1
        else:
            break
    checksum = 0
    for idx, c in enumerate(expanded_disk):
        if c is None:
            continue
        checksum += idx * c

    return checksum


def part2(disk_map=disk_map):
    expanded_disk = []
    s_idx = 0
    e_idx = 0
    for i, d in enumerate(disk_map):
        e_idx = s_idx + int(d)
        if i % 2 == 0:
            expanded_disk.append((i // 2, int(d), s_idx, e_idx))
        else:
            expanded_disk.append((None, int(d), s_idx, e_idx))
        s_idx = e_idx
    for i in range(len(expanded_disk) - 1, 0, -1):
        d_idx, size, start, end = expanded_disk[i]
        if d_idx is None:
            continue
        for c in range(i):
            f_idx, f_size, f_start, f_end = expanded_disk[c]
            if f_idx is not None:
                continue
            if f_size < size:
                continue
            expanded_disk[i] = (None, size, start, end)
            if size == f_size:
                expanded_disk[c] = (d_idx, f_size, f_start, f_end)
            else:
                expanded_disk = expanded_disk[:c] + [(d_idx, size, f_start, f_end - (f_size - size)), (f_idx, f_size - size, f_end - (f_size - size), f_end)] + expanded_disk[c + 1:]
            break
    checksum = 0
    for d_idx, size, start, end in expanded_disk:
        if d_idx is None:
            continue
        for i in range(start, end):
            checksum += i * d_idx
    return checksum


if __name__ == "__main__":
    print(part1(disk_map=disk_map))
    print(part2(disk_map=disk_map))