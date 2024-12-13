from utils import get_input

def simulate(stone_list, blinks):

    def transform(n):
        if n == 0:
            return [1]
        if len(str(n)) % 2 == 0:
            a = str(n)[:len(str(n))//2]
            b = str(n)[len(str(n))//2:]
            return [int(a), int(b)]
        else:
            return [2024 * n]

    stones = {n: stone_list.count(n) for n in stone_list}
    for _ in range(blinks):
        new_stones = {}
        for s in stones:
            for ts in transform(s):
                if ts in new_stones:
                    new_stones[ts] += stones[s]
                else:
                    new_stones[ts] = stones[s]
        stones = new_stones

    return sum(new_stones.values())

def part1(data):
    return simulate(data, 25)

def part2(data):
    return simulate(data, 75)

def process_input(data):
    return list(map(int, data.split()))


if __name__ == "__main__":
    day = 11
    data = get_input(day, splitlines=False)
    data = process_input(data)
    print(part1(data))
    print(part2(data))

