from utils import get_input

M, N = 103, 101
#M, N = 7, 11

def simulate(robots, seconds, find_tree=False):

    grid = [["." for _ in range(N)] for _ in range(M)]
    qs = [0,0,0,0]

    for p, v in robots:
        new_p = [0,0]
        new_p[0] = (p[0] + v[0] * seconds) % N
        new_p[1] = (p[1] + v[1] * seconds) % M

        left = (N - 1) / 2 < new_p[0]
        right = (N - 1) / 2 > new_p[0]
        up = (M - 1) / 2 < new_p[1]
        down = (M - 1) / 2 > new_p[1]

        if left and up: qs[0] += 1
        elif right and up: qs[1] += 1
        elif left and down: qs[2] += 1
        elif right and down: qs[3] += 1

        grid[new_p[1]][new_p[0]] = "X"
    
    if find_tree:
        #print(seconds)
        for i in range(M):
            # Tried to find a line with many X's
            if grid[i].count("X") > 30:
                print(seconds, grid[i].count("X"))
            # Found 8006 and printed
            if seconds == 8006:
                print("".join(grid[i]))
            
    return qs[0] * qs[1] * qs[2] * qs[3]

def part1(robots):
    SECONDS = 100
    return simulate(robots, SECONDS)

def part2(robots):
    for s in range(100000):
        simulate(robots, s, find_tree=True)
    return "Easter Egg"

def process_input(data):
    robots = []
    for line in data:
        p, v = line.split()
        p = list(map(int, p.split("=")[1].split(",")))
        v = list(map(int, v.split("=")[1].split(",")))
        robots.append((p,v))
    return robots


if __name__ == "__main__":
    day = 14
    example_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()
    data = get_input(day)
    #data = example_data
    processed = process_input(data)
    print(part1(processed))
    # process again to reset
    processed = process_input(data)
    print(part2(processed))

