from utils import get_input

def part1(text):
    i = 0
    pairs = []
    x, y = None, None
    while i < len(text):
        started = text[i:i+4] == "mul("
        x, y = None, None
        start_y, start_x = None, None
        if started:
            i += 4
            start_x = i # start of x
        # while digits, keep on reading
            while text[i].isdigit():
                i += 1
            if text[i] == ",":
                x = int(text[start_x:i])
                i += 1
                start_y = i
            if start_y:
                while text[i].isdigit():
                    i += 1
                if text[i] == ")":
                    y = int(text[start_y:i])
                    i += 1
        if x is not None and y is not None:
            pairs.append((x, y))
        else:
            i += 1

    return sum(x*y for x, y in pairs)

def part2(text):
    i = 0
    pairs = []
    x, y = None, None
    activated = True
    while i < len(text):
        started = text[i:i+4] == "mul("
        if text[i:i+4] == "do()":
            activated = True
        if text[i:i+7] == "don't()":
            activated = False
        if not activated:
            i += 1
            continue
        x, y = None, None
        start_y, start_x = None, None
        if started:
            i += 4
            start_x = i # start of x
        # while digits, keep on reading
            while text[i].isdigit():
                i += 1
            if text[i] == ",":
                x = int(text[start_x:i])
                i += 1
                start_y = i
            if start_y:
                while text[i].isdigit():
                    i += 1
                if text[i] == ")":
                    y = int(text[start_y:i])
                    i += 1
        if x is not None and y is not None:
            pairs.append((x, y))
        else:
            i += 1

    return sum(x*y for x, y in pairs)


if __name__ == "__main__":
    day = 3
    example_data_1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    data = get_input(day, splitlines=False)
    #data = example_data_1
    print(part1(data))
    example_data_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    #data = example_data_2
    print(part2(data))

