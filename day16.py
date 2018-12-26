import re


def get_data():
    with open('input') as f:
        data = []
        test = []
        data_text, test_text = f.read().split('\n\n\n\n')

        for line in data_text.splitlines():
            if not line.strip():
                continue
            values = list(map(int, re.findall(r'(\d+)', line)))
            if line.startswith('Before'):
                data.append([values])
            else:
                data[-1].append(values)

        for line in test_text.splitlines():
            values = list(map(int, re.findall(r'(\d+)', line)))
            test.append(values)

        return data, test


def init():
    registers = [0] * 4
    ops = [
        lambda regs, a, b, c: regs[a] + regs[b],  # addr
        lambda regs, a, b, c: regs[a] + b,  # addi
        lambda regs, a, b, c: regs[a] * regs[b],  # mulr
        lambda regs, a, b, c: regs[a] * b,  # muli
        lambda regs, a, b, c: regs[a] & regs[b],  # banr
        lambda regs, a, b, c: regs[a] & b,  # bani
        lambda regs, a, b, c: regs[a] | regs[b],  # borr
        lambda regs, a, b, c: regs[a] | b,  # bori
        lambda regs, a, b, c: regs[a],  # setr
        lambda regs, a, b, c: a,  # seti
        lambda regs, a, b, c: int(a > regs[b]),  # gtir
        lambda regs, a, b, c: int(regs[a] > b),  # gtri
        lambda regs, a, b, c: int(regs[a] > regs[b]),  # gtrr
        lambda regs, a, b, c: int(a == regs[b]),  # eqir
        lambda regs, a, b, c: int(regs[a] == b),  # eqri
        lambda regs, a, b, c: int(regs[a] == regs[b]),  # eqrr
    ]

    return registers, ops


def part_1(data):
    _, ops = init()

    result = 0
    for inputs in data:
        before, line, after = inputs
        _, a, b, c = line
        cnt = 0
        for op in ops:
            registers = before[:]
            registers[c] = op(registers, a, b, c)
            if registers == after:
                cnt += 1
        if cnt >= 3:
            result += 1

    return result


def part_2(data, test):
    _, ops = init()

    repeats = {}
    for inputs in data:
        before, line, after = inputs
        opcode, a, b, c = line

        for i, op in enumerate(ops):
            registers = before[:]
            registers[c] = op(registers, a, b, c)
            if registers == after:
                repeats.setdefault(opcode, set()).add(i)

    found = set()
    table = {}
    for i in range(16):
        for k, v in repeats.items():
            if len(v - found) == 1:
                table[k] = next(iter(v-found))
                found.update(v)

    registers = [0] * 4
    for inputs in test:
        opcode, a, b, c = inputs
        op = ops[table[opcode]]
        registers[c] = op(registers, a, b, c)

    return registers[0]


def main():
    data, test = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data, test))


if __name__ == '__main__':
    main()
