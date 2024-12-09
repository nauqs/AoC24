from utils import get_input

def part1(data):
    safe_count = 0
    for line in data:
        in_range, monotonous = True, True
        for i in range(1, len(line)):
            if abs(line[i] - line[i-1]) > 3:
                in_range = False
                break
            if i >= 2:
                if (line[i] - line[i-1]) * (line[i-1] - line[i-2]) <= 0:
                    monotonous = False
                    break
        safe_count += (in_range and monotonous)
    return safe_count

def part2(data):
    safe_count = 0
    for full_line in data:
        for excluded_i in range(len(full_line)+1):
            line = full_line[:excluded_i] +  full_line[excluded_i+1:]
            in_range, monotonous = True, True
            for i in range(1, len(line)):
                if abs(line[i] - line[i-1]) > 3:
                    in_range = False
                    break
                if i >= 2:
                    if (line[i] - line[i-1]) * (line[i-1] - line[i-2]) <= 0:
                        monotonous = False
                        break
            if in_range and monotonous:
                safe_count += 1
                break
    return safe_count

def process_input(data):
    return [list(map(int, line.split())) for line in data]


if __name__ == "__main__":
    day = 2
    example_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()
    data = get_input(day)
    print(data)
    #data = example_data
    data = process_input(data)
    print(part1(data.copy()))
    print(part2(data.copy()))

