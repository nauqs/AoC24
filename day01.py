from utils import get_input
from collections import Counter

def part1(data):
    l1, l2 = zip(*data)
    l1, l2 = sorted(l1), sorted(l2)
    s = 0
    for i in range(len(l1)):
        s += abs(l1[i]-l2[i])
    return s

def part2(data):
    l1, l2 = zip(*data)
    count_right = Counter(l2)
    s = 0
    for n in l1:
        s += n*count_right[n]
    return s

def process_input(lines):
    return [(int(x.split(" ")[0]), int(x.split(" ")[-1])) for x in lines]


if __name__ == "__main__":
    day = 1
    example_data = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()
    data = get_input(day)
    #data = example_data
    data = process_input(data)
    print(part1(data.copy()))
    print(part2(data.copy()))

