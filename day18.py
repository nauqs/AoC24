from utils import get_input

N = 71
FIRST_BITS = 1024
BIG_N = 99999999
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_grid(data):
    grid = [["." for _ in range(N)] for _ in range(N)]
    for line in data:
        x, y = map(int, line.split(","))
        grid[y][x] = "#"
    return grid

def part1(data, first_bits=FIRST_BITS):
    grid = get_grid(data[:first_bits])
    start, exit = (0, 0), (N - 1, N - 1)
    queue = [(start, 0)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = True
    while queue:
        pos, steps = queue.pop(0)
        x, y = pos
        if pos == exit:
            return steps
        for dx, dy in DIRS:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y] and grid[new_x][new_y] != "#":
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), steps + 1))
    return -1

def part2(data):
    # binary search between FIRST_BITS and len(data)
    left, right = FIRST_BITS, len(data)
    result = FIRST_BITS - 1
    while left <= right:
        mid = (left + right) // 2
        req_steps = part1(data, first_bits=mid)
        if req_steps != -1:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return data[result]

if __name__ == "__main__":
    day = 18
    example_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".splitlines()
    data = get_input(day)
    #data = example_data
    print(part1(data))
    print(part2(data))

