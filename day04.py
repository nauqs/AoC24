from utils import get_input

dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
word = "XMAS"

def part1(grid):
    count = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == word[0]:
                for dir_i, dir_j in dirs:
                    if find_word(grid, i, j, dir_i, dir_j):
                        count += 1

    return count

def find_word(grid, start_x, start_y, dir_x, dir_y):
    found = False
    m, n = len(grid), len(grid[0])
    x, y = start_x, start_y
    count_letter = 0
    while x < m and x >= 0 and y >= 0 and y < n:
        if word[count_letter] == grid[x][y]:
            count_letter += 1
            if count_letter == len(word):
                return True
            x += dir_x
            y += dir_y
        else:
            break
    return False


def part2(grid):
    count = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "A":
                if find_xmas(grid, i, j):
                    count += 1

    return count

def find_xmas(grid, start_x, start_y):
    found = False
    m, n = len(grid), len(grid[0])
    x, y = start_x, start_y
    if x < m-1 and x > 0 and y > 0 and y < n-1:
        square = [line[y-1:y+2] for line in grid[x-1:x+2]]
        # Check 4 rotations (very ugly)
        o1 = (grid[x-1][y-1] == "M" and grid[x-1][y+1] == "M" and grid[x+1][y+1] == "S" and grid[x+1][y-1] == "S")
        o2 = (grid[x-1][y-1] == "S" and grid[x-1][y+1] == "M" and grid[x+1][y+1] == "M" and grid[x+1][y-1] == "S")
        o3 = (grid[x-1][y-1] == "S" and grid[x-1][y+1] == "S" and grid[x+1][y+1] == "M" and grid[x+1][y-1] == "M")
        o4 = (grid[x-1][y-1] == "M" and grid[x-1][y+1] == "S" and grid[x+1][y+1] == "S" and grid[x+1][y-1] == "M")
        return (o1 or o2 or o3 or o4)
    return False

def process_input(lines):
    return lines


if __name__ == "__main__":
    day = 4
    example_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()
    data = get_input(day)
    #data = example_data
    data = process_input(data)
    print(part1(data.copy()))
    print(part2(data.copy()))

