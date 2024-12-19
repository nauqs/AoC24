from utils import get_input

def process_input(data):
    patterns, designs = data.split("\n\n")
    patterns = [x for x in patterns.split(", ") if x]
    designs = [x for x in designs.split("\n") if x]
    return patterns, designs

def check_pattern(patterns, design):
    stack = [0]
    visited = set()
    while stack:
        current_idx = stack.pop()
        if current_idx in visited:
            continue
        visited.add(current_idx)
        if current_idx == len(design):
            return True
        for pattern in patterns:
            if design.startswith(pattern, current_idx):
                stack.append(current_idx + len(pattern))
    return False

def part1(data):
    patterns, designs = process_input(data)
    return sum(check_pattern(patterns, design) for design in designs)

def count_pattern(patterns, design):
    total_count = {}
    def recursive_count(start_idx):
        if start_idx == len(design):
            return 1
        if start_idx in total_count:
            return total_count[start_idx]
        total = 0
        for pattern in patterns:
            if design.startswith(pattern, start_idx):
                total += recursive_count(start_idx + len(pattern))
        total_count[start_idx] = total
        return total
    return recursive_count(0)

def part2(data):
    patterns, designs = process_input(data)
    return sum(count_pattern(patterns, design) for design in designs)


if __name__ == "__main__":
    day = 19
    example_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
    data = get_input(day, splitlines=False)
    #data = example_data
    print(part1(data))
    print(part2(data))

