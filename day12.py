import re


def get_data():
    with open('input') as f:
        state = list(f.readline().split(':')[1].strip())
        state = [i for i, p in enumerate(state) if p == '#']
        f.readline() # skip empty line
        mods = {}
        for line in f:
            k, v = re.findall(r'([#.]+)[\s=>]+([#.]+)', line)[0]
            mods[k] = (v == '#')

        return state, mods


def part_1(state, mods, generations):
    state = set(state)
    pad = 4
    for _ in range(generations):
        first = min(state)
        last = max(state)
        pots = '.' * pad
        pots += ''.join('#' if i in state else '.' for i in range(first, last + 1))
        pots += '.' * pad

        state = []
        for i in range(2, last - first + pad * 2 - 1):
            if mods[pots[i-2:i+3]]:
                state.append(i - 4 + first)
    return sum(state)


def part_2(state, mods):
    prev = float('inf')
    diff = float('inf')
    cnt = 0
    i = 100
    while cnt != 5:
        val = part_1(state, mods, i)
        if val - prev == diff:
            cnt += 1
        else:
            cnt = 0
        diff = val - prev
        prev = val
        i += 1

    return part_1(state, mods, i) + ((50000000000 - i) * diff)


def main():
    state, mods = get_data()
    print('1:', part_1(state, mods, 20))
    print('2:', part_2(state, mods))


if __name__ == '__main__':
    main()
