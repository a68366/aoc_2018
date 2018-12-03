import re


def part_1(fabric):
    splitter = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
    cnt = 0

    with open('input') as f:
        for line in f:
            line = line.strip()
            id, x, y, w, h = map(int, splitter.match(line).groups())
            for i in range(x, x+w):
                for j in range(y, y+h):
                    fabric[i][j] += 1
                    if fabric[i][j] == 2:
                        cnt += 1

    return cnt


def part_2(fabric):
    splitter = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')

    with open('input') as f:
        for line in f:
            line = line.strip()
            id, x, y, w, h = map(int, splitter.match(line).groups())
            flag = True
            for i in range(x, x+w):
                if not flag:
                    break
                for j in range(y, y+h):
                    if fabric[i][j] != 1:
                        flag = False
                        break

            if flag:
                return id


def main():
    fabric = [[0] * 1000 for _ in range(1000)]
    print('1:', part_1(fabric))
    print('2:', part_2(fabric))


if __name__ == '__main__':
    main()
