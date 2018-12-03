from collections import Counter


def part_1():
    with open('input') as f:
        threes = 0
        twos = 0

        for line in f:
            cnt = Counter(line)
            flag2 = True
            flag3 = True
            for val in cnt.values():
                if val == 2 and flag2:
                    twos += 1
                    flag2 = False
                if val == 3 and flag3:
                    threes += 1
                    flag3 = False

        return threes * twos


def part_2():
    with open('input') as f:
        lines = f.read().split()
        for n, i in enumerate(lines):
            for j in lines[n:]:
                cnt = 0
                same = ''
                for sym_1, sym_2 in zip(i, j):
                    if sym_1 != sym_2:
                        cnt += 1
                    else:
                        same += sym_1
                    if cnt > 1:
                        break
                if cnt == 1:
                    return same

    return None


def main():
    print('1:', part_1())
    print('2:', part_2())


if __name__ == '__main__':
    main()
