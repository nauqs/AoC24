from utils import get_input

def evaluate_ltr(exp):
    result = int(exp[0])
    for i in range(1, len(exp), 2):
        if exp[i] == "*":
            result *= int(exp[i+1])
        elif exp[i] == "+":
            result += int(exp[i+1])
        else:
            result = int(str(result) + str(exp[i+1]))
    return result

def check_combination(target, numbers, part2=False):
    found = False
    stack = [[numbers[0]]]
    while stack and not found:
        exp = stack.pop()
        i = len(exp) // 2 + 1
        if i >= len(numbers):
            if evaluate_ltr(exp) == target:
                found = True
                return found, exp
            continue
        new_exp_list = [exp + ["*", numbers[i]], exp + ["+", numbers[i]]]
        if part2:
            new_exp_list.append(exp + ["||", numbers[i]])
        for new_exp in new_exp_list:
            if evaluate_ltr(new_exp) <= target:
                stack.append(new_exp)
    return found, ""
    
def part1(data):
    return sum(t for t, ns in data if check_combination(t, ns)[0])
    
def part2(data):
    return sum(t for t, ns in data if check_combination(t, ns, part2=True)[0])

def process_input(data):
    lines = [x.split(": ") for x in data]
    return [(int(x[0]), x[1].split()) for x in lines]


if __name__ == "__main__":
    day = 7
    example_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()
    data = get_input(day)
    #data = example_data
    data = process_input(data)
    print(part1(data.copy()))
    print(part2(data.copy()))

