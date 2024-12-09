from utils import get_input

def part1(pairs, updates):
    s = 0
    for update in updates:
        complies = True
        L = len(update)
        for a, b in pairs:
            if a in update and b in update:
                found_a, found_b = False, False
                for i in range(L):
                    if update[i] == a:
                        found_a = True
                    if update[i] == b:
                        found_b = True
                    if found_a and not found_b:
                        break
                    if found_b and not found_a:
                        complies = False
                        break
        if complies:
            s += update[L//2]
    return s

def part2(pairs, updates):
    s = 0
    for update in updates:
        complies = True
        L = len(update)
        for a, b in pairs:
            if a in update and b in update:
                found_a, found_b = False, False
                for i in range(L):
                    if update[i] == a:
                        found_a = True
                    if update[i] == b:
                        found_b = True
                    if found_a and not found_b:
                        break
                    if found_b and not found_a:
                        complies = False
                        break
            if not complies:
                break
        if not complies:
            moved = True
            while moved:
                moved = False
                for a, b in pairs:
                    if a in update and b in update:
                        i = update.index(a)
                        j = update.index(b)
                        if i > j:
                            update[i], update[j] = update[j], update[i]
                            moved = True
            s += update[L//2]
    return s

def process_input(data):
    pairs_raw, updates_raw = data.split("\n\n")
    pairs = [list(map(int, x.split("|"))) for x in pairs_raw.split("\n")]
    updates = [list(map(int, x.split(","))) for x in updates_raw.split("\n")]
    return pairs, updates


if __name__ == "__main__":
    day = 5
    data = get_input(day, splitlines=False)
    pairs, updates = process_input(data)
    print(part1(pairs, updates))
    print(part2(pairs, updates))

