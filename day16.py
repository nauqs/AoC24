from utils import get_input

BIG_N = 999999
STEP_COST = 1
TURN_COST = 1000

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def turn_left(dir):
    x, y = dir
    return (-y, x)

def turn_right(dir):
    x, y = dir
    return (y, -x)

def in_bounds_not_wall(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "#"

def part1(data, return_best_paths=False):
    grid, start, end = process_input(data)
    start_dir = (0, 1)
    stack = [([start], start_dir, 0)]
    best_scores = [[BIG_N for _ in range(len(grid[0]))] for _ in range(len(grid))]
    best_paths = set()

    while stack:
        curr_path, curr_dirr, steps = stack.pop()
        pos = curr_path[-1]
        if steps > best_scores[pos[0]][pos[1]]:
            continue
        if pos == end:
            if steps == best_scores[pos[0]][pos[1]]:
                best_paths.update(set(curr_path))
            else:
                best_paths = set(curr_path)
        best_scores[pos[0]][pos[1]] = steps
        x, y = pos
        new_x, new_y = x + curr_dirr[0], y + curr_dirr[1]
        if in_bounds_not_wall(grid, new_x, new_y):
            stack.append((
                curr_path + [(new_x, new_y)],
                 curr_dirr,
                 steps + STEP_COST
            ))
        for turn in [turn_left, turn_right]:
            new_dir = turn(curr_dirr)
            new_x, new_y = x + new_dir[0], y + new_dir[1]
            if in_bounds_not_wall(grid, new_x, new_y):
                stack.append((
                    curr_path + [(new_x, new_y)],
                    new_dir,
                    steps + STEP_COST + TURN_COST
                ))
    if return_best_paths:
        return best_paths
    return best_scores[end[0]][end[1]]

def part2(data):
    return len(part1(data, return_best_paths=True))

def process_input(data):
    grid = []
    for line in data:
        grid.append(list(line))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)
    return grid, start, end

if __name__ == "__main__":
    day = 16
    example_data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()
    data = get_input(day)
    #data = example_data
    print(part1(data.copy()))
    print(part2(data.copy()))

