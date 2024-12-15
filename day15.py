from utils import get_input

DIRS = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

def get_grid_info(grid):
    robot, walls, boxes = None, [], []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                robot = (x, y)
            elif cell == "#":
                walls.append((x, y))
            elif cell == "O":
                boxes.append((x, y))
    return robot, walls, boxes


def draw_grid(robot, walls, boxes, M, N):
    grid = [["." for _ in range(N)] for _ in range(M)]
    x, y = robot
    grid[y][x] = "@"
    for x, y in walls:
        grid[y][x] = "#"
    for x, y in boxes:
        grid[y][x] = "O"
    return grid

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def push_boxes(robot, boxes, walls, dx, dy):
    x, y = robot
    i = 1
    boxes_to_move = []
    while (x + i*dx, y + i*dy) in boxes:
        boxes_to_move.append((x + i*dx, y + i*dy))
        i += 1
    # if walls, it cannot be pushed
    if (x+i*dx, y+i*dy) in walls:
        return robot, boxes
    # if free space, move the robot and the boxes
    new_robot = (x+dx, y+dy)
    new_boxes = []
    for box in boxes:
        if box in boxes_to_move:
            new_boxes.append((box[0]+dx, box[1]+dy))
        else:
            new_boxes.append(box)
    return new_robot, new_boxes

def part1(grid, moves):
    M, N = len(grid), len(grid[0])
    robot, walls, boxes = get_grid_info(grid)
    #print_grid(grid)
    for move in moves:
        dx, dy = DIRS[move]
        new_x, new_y = robot[0] + dx, robot[1] + dy
        if (new_x, new_y) in walls:
            continue
        if (new_x, new_y) not in boxes:
            robot = (new_x, new_y)
        else:
            robot, boxes = push_boxes(robot, boxes, walls, dx, dy)

        grid = draw_grid(robot, walls, boxes, M, N)
        #print_grid(grid)
    gps = 0
    for box in boxes:
        gps += box[0] + 100*box[1]
        
    return gps

def get_wider_grid_info(grid):
    M, N = len(grid), 2*len(grid[0])
    robot, walls, boxes = None, [], []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                robot = (2*x, y)
            elif cell == "#":
                walls.append((2*x, y))
                walls.append((2*x+1, y))
            elif cell == "O":
                boxes.append((2*x, y))

    return M, N, robot, walls, boxes

def draw_wider_grid(robot, walls, boxes, M, N):
    grid = [["." for _ in range(N)] for _ in range(M)]
    x, y = robot
    grid[y][x] = "@"
    for x, y in walls:
        grid[y][x] = "#"
    for x, y in boxes:
        grid[y][x] = "["
        grid[y][x+1] = "]"
    return grid

def push_wider_boxes(robot, boxes, walls, dx, dy):
    x, y = robot
    i = 1
    boxes_to_move = []
    if dx != 0:
        while (x + i*dx, y + i*dy) in boxes or (x + i*dx - 1, y + i*dy) in boxes:
            if (x + i*dx, y + i*dy) in boxes:
                boxes_to_move.append((x + i*dx, y + i*dy))
            if (x + i*dx - 1, y + i*dy) in boxes:
                boxes_to_move.append((x + i*dx - 1, y + i*dy))
            i += 2 # move 2 if x-direction, 1 if y-direction
        # if walls, it cannot be pushed
        if dx == 1 and (x+i*dx, y+i*dy) in walls:
            return robot, boxes
        if dx == -1 and (x+i*dx, y+i*dy) in walls:
            return robot, boxes
    else:
        stack = []
        if (x + i*dx, y + i*dy) in boxes: stack.append((x + i*dx, y + i*dy))
        if (x + i*dx - 1, y + i*dy) in boxes: stack.append((x + i*dx - 1, y + i*dy))
        while stack:
            box = stack.pop()
            if box in boxes_to_move:
                continue
            if (box[0]+dx, box[1]+dy) in walls or (box[0]+dx+1, box[1]+dy) in walls:
                return robot, boxes
            boxes_to_move.append(box)
            pushable_boxes = [(box[0]+dx, box[1]+dy), (box[0]+dx+1, box[1]+dy), (box[0]+dx-1, box[1]+dy)]
            for b in pushable_boxes:
                if b in boxes:
                    stack.append(b)
    robot = (x+dx, y+dy)
    new_boxes = []
    for box in boxes:
        if box in boxes_to_move:
            new_boxes.append((box[0]+dx, box[1]+dy))
        else:
            new_boxes.append(box)
    return robot, new_boxes

def part2(grid, moves):
    M, N, robot, walls, boxes = get_wider_grid_info(grid)
    grid = draw_wider_grid(robot, walls, boxes, M, N)
    
    for move in moves:
        #print(move)
        dx, dy = DIRS[move]
        new_x, new_y = robot[0] + dx, robot[1] + dy
        if (new_x, new_y) in walls:
            continue
        if (new_x, new_y) not in boxes and (new_x-1, new_y) not in boxes:
            robot = (new_x, new_y)
        else:
            robot, boxes = push_wider_boxes(robot, boxes, walls, dx, dy)

        grid = draw_wider_grid(robot, walls, boxes, M, N)
        #print_grid(grid)

    gps = 0
    for box in boxes:
        gps += box[0] + 100*box[1]
    return gps

def process_input(data):
    grid, moves = data.split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    moves = [move for line in moves.splitlines() for move in line]
    return grid, moves



if __name__ == "__main__":
    day = 15
    example_data_1 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    example_data_2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    example_data_3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""
    example_data_4 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    data = get_input(day, splitlines=False)
    #data = example_data_4
    grid, moves = process_input(data)
    print(part1(grid, moves))
    print(part2(grid, moves))

