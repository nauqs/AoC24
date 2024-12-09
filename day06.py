from utils import get_input

DIRS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def turn_right(dir):
    if dir == ">": return "v"
    if dir == "v": return "<"
    if dir == "<": return "^"
    if dir == "^": return ">"

def part1(grid):
    m, n = len(grid), len(grid[0])
    visited = [[0]*n for x in range(m)]
    
    def in_bounds(x, y):
        return (0 <= x < m) and (0 <= y < n)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] in DIRS:
                x, y = i, j
                d = grid[i][j]
                break
    
    while in_bounds(x, y):
        visited[x][y] = 1
        new_x, new_y = x + DIRS[d][0], y + DIRS[d][1]
        if in_bounds(new_x, new_y):
            if grid[new_x][new_y] == "#":
                d = turn_right(d)
            else:
                x, y = new_x, new_y
        else:
            break
    
    return sum(sum(row) for row in visited)




def part2(grid):
    m, n = len(grid), len(grid[0])
    
    def in_bounds(x, y):
        return (0 <= x < m) and (0 <= y < n)

    for i in range(m):
        for j in range(n):
            if grid[i][j] in DIRS:
                start_x, start_y = i, j
                start_d = grid[i][j]
                break

    def check_loop(grid, x, y, d):
        visited = {d: [[0]*n for x in range(m)] for d in DIRS}
        while in_bounds(x, y):
            if visited[d][x][y]:
                return True
            visited[d][x][y] = 1
            new_x, new_y = x + DIRS[d][0], y + DIRS[d][1]
            if in_bounds(new_x, new_y):
                if grid[new_x][new_y] == "#":
                    d = turn_right(d)
                else:
                    x, y = new_x, new_y
            else:
                break
        return False

    # brute force, try each spot
    c = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                new_grid = [list(row) for row in grid]
                new_grid[i][j] = "#"
                if check_loop(new_grid, start_x, start_y, start_d):
                    c += 1
    return c


if __name__ == "__main__":
    day = 6
    example_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()
    data = get_input(day)
    #data = example_data
    print(part1(data.copy()))
    print(part2(data.copy()))

