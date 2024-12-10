from utils import get_input

DIRS = [(1,0), (-1,0), (0,1), (0,-1)]


def find_trailheads(grid, th, m, n, use_visited=True):

    def in_bounds(x, y):
        return (0 <= x < m) and (0 <= y < n)

    c = 0
    stack = [[th]]
    visited = [[0]*n for _ in range(m)]
    while stack:
        path = stack.pop()
        if len(path) == 10:
            c += 1
            continue
        x, y = path[-1]
        for d in DIRS:
            new_x, new_y = x+d[0], y+d[1]
            if in_bounds(new_x, new_y) and grid[new_x][new_y] == grid[x][y] + 1 and not (visited[new_x][new_y] and use_visited):
                visited[new_x][new_y] = 1
                stack.append(path+[(new_x, new_y)])

    return c

def part1(grid):
    m, n = len(grid), len(grid[0])
    trailheads = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0]
    return sum([find_trailheads(grid, th, m, n) for th in trailheads])

def part2(grid):
    m, n = len(grid), len(grid[0])
    trailheads = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0]
    return sum([find_trailheads(grid, th, m, n, use_visited=False) for th in trailheads])

def process_input(data):
    return [list(map(int,row)) for row in data]


if __name__ == "__main__":
    day = 10
    example_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()
    data = get_input(day)
    #data = example_data
    grid = process_input(data)
    print(part1(grid))
    print(part2(grid))

