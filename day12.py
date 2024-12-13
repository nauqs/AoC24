from utils import get_input

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
CORNER_DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def part1(grid):
    m, n = len(grid), len(grid[0])

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    visited = [[False for _ in range(n)] for _ in range(m)]

    price = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True

            stack = [(i, j)]
            area, perimeter = 0, 0
            while stack:
                x, y = stack.pop()
                area += 1
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if in_bounds(nx, ny) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                    elif not in_bounds(nx, ny) or grid[nx][ny] != grid[x][y]:
                        perimeter += 1
            price += area * perimeter

    return price


def part2(grid):
    m, n = len(grid), len(grid[0])

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    visited = [[False for _ in range(n)] for _ in range(m)]

    price = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True

            stack = [(i, j)]
            region = set()
            while stack:
                x, y = stack.pop()
                region.add((x, y))
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if in_bounds(nx, ny) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

            def get_corners(x, y):
                corners = set()
                for dx, dy in CORNER_DIRS:
                    cx, cy = x + dx, y + dy #corner neighbour
                    vx, vy = x + dx, y #vertical neighbour
                    hx, hy = x, y + dy #horizontal neighbour
                    # internal corner: v and h in, c out
                    if (vx, vy) in region and (hx, hy) in region and (cx, cy) not in region:
                        corners.add((vx, vy, hx, hy))
                    # external corner: v and h out
                    elif (vx, vy) not in region and (hx, hy) not in region:
                        corners.add((vx, vy, hx, hy))
                return corners

            corners = set()
            for x, y in region:
                corners |= get_corners(x, y)

            price += len(corners) * len(region)

    return price

if __name__ == "__main__":
    day = 12
    example_data = """AAAA
BBCD
BBCC
EEEC""".splitlines()
    data = get_input(day)
    #data = example_data
    grid = list(map(list, data))
    print(part1(grid))
    print(part2(grid))

