import re


def get_data():
    with open('input') as f:
        data = []
        for line in f:
            op = re.findall(r'([a-zA-Z]+)', line)
            values = list(map(int, re.findall(r'(\d+)', line)))
            data.append(op + values)
        return data


def init(data):
    registers = [0] * 6
    ops = {
        'addr': lambda regs, a, b: regs[a] + regs[b],
        'addi': lambda regs, a, b: regs[a] + b,
        'mulr': lambda regs, a, b: regs[a] * regs[b],
        'muli': lambda regs, a, b: regs[a] * b,
        'banr': lambda regs, a, b: regs[a] & regs[b],
        'bani': lambda regs, a, b: regs[a] & b,
        'borr': lambda regs, a, b: regs[a] | regs[b],
        'bori': lambda regs, a, b: regs[a] | b,
        'setr': lambda regs, a, b: regs[a],
        'seti': lambda regs, a, b: a,
        'gtir': lambda regs, a, b: int(a > regs[b]),
        'gtri': lambda regs, a, b: int(regs[a] > b),
        'gtrr': lambda regs, a, b: int(regs[a] > regs[b]),
        'eqir': lambda regs, a, b: int(a == regs[b]),
        'eqri': lambda regs, a, b: int(regs[a] == b),
        'eqrr': lambda regs, a, b: int(regs[a] == regs[b]),
        }
    ip = data[0][1]

    return registers, ops, ip


def part_1(data):
    registers, ops, ip = init(data)
    data = data[1:]
    while registers[ip] < len(data):
        op, a, b, c = data[registers[ip]]
        registers[c] = ops[op](registers, a, b)
        registers[ip] += 1

    return registers[0] - 1 if ip == 0 else registers[0]


def part_2(data):
    registers, ops, ip = init(data)
    registers[0] = 1
    data = data[1:]
    while registers[ip] < len(data):
        op, a, b, c = data[registers[ip]]
        registers[c] = ops[op](registers, a, b)
        registers[ip] += 1
        if registers[1] == 1:
            return 'Sum of factors of {0}'.format(registers[-1])


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data))


if __name__ == '__main__':
    main()
