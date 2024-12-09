from utils import get_input


def part1(grid):
    m, n = len(grid), len(grid[0])
    
    def in_bounds(x, y):
        return (0 <= x < m) and (0 <= y < n)
    
    def get_antinodes(loc_1, loc_2):
        antinodes = []
        x_1, y_1 = loc_1
        x_2, y_2 = loc_2
        dif_x, dif_y = x_2 - x_1, y_2 - y_1
        antinode_1 = (x_1 - dif_x, y_1 - dif_y)
        antinode_2 = (x_2 + dif_x, y_2 + dif_y)
        if in_bounds(*antinode_1):
            antinodes.append(antinode_1)
        if in_bounds(*antinode_2):
            antinodes.append(antinode_2)
        return antinodes

    antennas = {}
    for i in range(m):
        for j in range(n):
            x = grid[i][j]
            if x.isdigit() or x.isalpha():
                if x in antennas:
                    antennas[x].append((i, j))
                else:
                    antennas[x] = [(i, j)]

    antinodes = set()
    for antenna, locations in antennas.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                for antinode in get_antinodes(locations[i], locations[j]):
                    antinodes.add(antinode)
    
    return len(antinodes)

def part2(grid):
    m, n = len(grid), len(grid[0])
    
    def in_bounds(x, y):
        return (0 <= x < m) and (0 <= y < n)
    
    def get_antinodes(loc_1, loc_2):
        antinodes = []
        x_1, y_1 = loc_1
        x_2, y_2 = loc_2
        dif_x, dif_y = x_2 - x_1, y_2 - y_1

        step_x, step_y = dif_x, dif_y
        x, y = x_1 + step_x, y_1 + step_y

        # points between loc_1 and loc_2
        while (x, y) != loc_2:
            antinodes.append((x, y))
            x, y = x + step_x, y + step_y

        # points beyond loc_1
        x, y = x_1 - step_x, y_1 - step_y
        while in_bounds(x, y):
            antinodes.append((x, y))
            x, y = x - step_x, y - step_y

        # points beyond loc_2
        x, y = x_2 + step_x, y_2 + step_y
        while in_bounds(x, y):
            antinodes.append((x, y))
            x, y = x + step_x, y + step_y

        return antinodes

    antennas = {}
    for i in range(m):
        for j in range(n):
            x = grid[i][j]
            if x.isdigit() or x.isalpha():
                if x in antennas:
                    antennas[x].append((i, j))
                else:
                    antennas[x] = [(i, j)]

    antinodes = set()
    for antenna, locations in antennas.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                for antinode in get_antinodes(locations[i], locations[j]):
                    antinodes.add(antinode)
    
    for antenna, locations in antennas.items():
        antinodes.update(locations)
    return len(antinodes)

if __name__ == "__main__":
    day = 8
    example_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()
    data = get_input(day)
    #data = example_data
    print(part1(data.copy()))
    print(part2(data.copy()))

