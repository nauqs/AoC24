from utils import get_input

# (1) Na * a1 + Nb * b1 = p1
# (2) Na * a2 + Nb * b2 = p2
# <=> Na = (p1 - Nb * b1) / a1
# <=> Nb = (p2 * a1 - p1 * a2) / (b2 * a1 - b1 * a2)

def part1(data):
    tokens = 0
    for a, b, prize in data:
        count_b = ( prize[1] * a[0] - prize[0] * a[1] ) / ( b[1] * a[0] - b[0] * a[1] )
        count_a = ( prize[0] - count_b * b[0] ) / a[0]
        if float(count_a) != int(float(count_a)) or float(count_b) != int(float(count_b)):
            continue
        tokens += int(3 * count_a + count_b)
    return tokens

def part2(data):
    N = 10000000000000
    new_data = []
    for a, b, prize in data:
        new_prize = (N+prize[0], N+prize[1])
        new_data.append((a, b, new_prize))
    return part1(new_data)

def process_input(data):
    machines_raw = [g.splitlines() for g in data.split("\n\n")]
    machines = []
    for m in machines_raw:
        a = (
            int(m[0].split("X+")[1].split(",")[0].strip()),
            int(m[0].split("Y+")[1].strip())
        )
        b = (
            int(m[1].split("X+")[1].split(",")[0].strip()),
            int(m[1].split("Y+")[1].strip())
        )
        prize = (
            int(m[2].split("X=")[1].split(",")[0].strip()),
            int(m[2].split("Y=")[1].strip())
        )
        machines.append((a, b, prize))
    return machines


if __name__ == "__main__":
    day = 13
    example_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    data = get_input(day, splitlines=False)
    #data = example_data
    data = process_input(data)
    print(part1(data))
    print(part2(data))

