from collections import defaultdict


def part_1():
    with open('input') as f:
        return sum(map(int, f.read().split()))


def part_2():
    with open('input') as f:
        data = f.read().splitlines()

    d = defaultdict(int)
    d[0] = 1
    result = 0

    while True:
        for line in data:
            val = int(line)
            result += val
            d[result] += 1

            if d[result] == 2:
                return result


def main():
    print('1:', part_1())
    print('2:', part_2())


if __name__ == '__main__':
    main()
