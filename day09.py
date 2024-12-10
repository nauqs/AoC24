from utils import get_input


def get_checksum(digits):
    return sum((i * int(digit)) for i, digit in enumerate(digits) if digit.isdigit())


def get_disk(data):

    disk = []
    idx, free_space = 0, False

    for digit in data:
        if not digit.isdigit(): continue
        if free_space:
            disk += (["."] * int(digit))
        else:
            disk += ([str(idx)] * int(digit))
            idx += 1
        free_space = not free_space

    return disk


def part1(data):

    disk = get_disk(data)

    i, j = 0, len(disk) - 1
    while i < j:
        while disk[i] != ".":
            i += 1
        while disk[j] == ".":
            j -= 1
        if i < j:
            disk[i], disk[j] = disk[j], disk[i]

    return get_checksum(disk[:i])


def get_leftmost_space(disk, length):
    # Optimizable
    for i in range(len(disk)):
        seq = disk[i:i+length+1]
        if all(x == "." for x in disk[i:i+length+1]):
            return i
    return -1


def part2(data):
    disk = get_disk(data)

    max_id = disk[-1]
    i = len(disk) - 1

    for idx in range(int(max_id), 0, -1):
        max_idx, min_idx = -1, -1
        while str(idx) != disk[i]:
            i -= 1
        max_idx = i
        while str(idx) == disk[i]:
            i -= 1
        min_idx = i + 1
        length = max_idx-min_idx
        swap_idx = get_leftmost_space(disk, length) # brute force, optimizable

        if swap_idx != -1 and swap_idx < min_idx:
            disk[swap_idx:swap_idx+length+1], disk[min_idx:max_idx+1] = disk[min_idx:max_idx+1], disk[swap_idx:swap_idx+length+1]

    return get_checksum(disk)


if __name__ == "__main__":
    day = 9
    example_data = "2333133121414131402"
    data = get_input(day, splitlines=False)
    #data = example_data
    print(part1(data))
    print(part2(data))

