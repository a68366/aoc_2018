from collections import Counter
from itertools import chain
import copy


def get_data():
    with open('input') as f:
        return ([list(line) for line in f.read().split()])


def get_adjacent(field, point):
    height = len(field)
    width = len(field[0])
    x, y = point
    for y2 in range(y - 1, y + 2):
        for x2 in range(x - 1, x + 2):
            if -1 < x < width and -1 < y < height and (x != x2 or y != y2) \
                    and 0 <= x2 < width and 0 <= y2 < height:
                yield field[x2][y2]


def part_1(data, total_repeats=10):
    field = copy.deepcopy(data)
    prev = copy.deepcopy(field)

    for _ in range(total_repeats):
        for i, row in enumerate(prev):
            for j, val in enumerate(row):
                cnt = Counter(get_adjacent(prev, (i, j)))
                if val == '.' and cnt['|'] >= 3:
                    field[i][j] = '|'
                elif val == '|' and cnt['#'] >= 3:
                    field[i][j] = '#'
                elif val == '#' and (cnt['#'] < 1 or cnt['|'] < 1):
                    field[i][j] = '.'
        prev = copy.deepcopy(field)

    cnt = Counter(chain(*field))
    return cnt['#'] * cnt['|']


def part_2(data, total_repeats=1000000000):
    field = copy.deepcopy(data)
    prev = copy.deepcopy(field)
    seen = []
    repeats = 0
    found = False
    while repeats != total_repeats:
        for i, row in enumerate(prev):
            for j, val in enumerate(row):
                cnt = Counter(get_adjacent(prev, (i, j)))
                if val == '.' and cnt['|'] >= 3:
                    field[i][j] = '|'
                elif val == '|' and cnt['#'] >= 3:
                    field[i][j] = '#'
                elif val == '#' and (cnt['#'] < 1 or cnt['|'] < 1):
                    field[i][j] = '.'
        if not found and field in seen:
            found = True
            idx = seen.index(field)
            repeats = total_repeats // (idx+1) * (idx+1)
            seen = []
        else:
            seen.append(copy.deepcopy(field))
        prev = copy.deepcopy(field)
        repeats += 1

    cnt = Counter(chain(*field))
    return cnt['#'] * cnt['|']


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data))


if __name__ == '__main__':
    main()
