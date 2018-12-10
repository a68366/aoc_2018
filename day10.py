import re


def get_data():
    with open('input') as f:
        result = []
        for line in f:
            result.append(tuple(map(int, re.findall(r'(-?\d+)', line))))

        return result


def part_1(data):
    i, minx, miny, w, h = part_2(data)
    field = [['.'] * h for _ in range(w)]
    for x, y, vx, vy in data:
        x = x + i * vx - minx
        y = y + i * vy - miny
        field[x][y] = '*'

    for line in zip(*field):
        print(''.join(line))

    return 'Read the text above ^'


def part_2(data):
    i = 0
    decreasing = True
    minx = miny = w = h = 0
    area = float('inf')
    while decreasing:
        decreasing = False
        x1 = min(x+i*v for (x, _, v, _) in data)
        x2 = max(x+i*v for (x, _, v, _) in data)
        y1 = min(y+i*v for (_, y, _, v) in data)
        y2 = max(y+i*v for (_, y, _, v) in data)
        new_area = (x2-x1) * (y2-y1)
        if new_area < area:
            decreasing = True
            minx, miny, w, h = x1, y1, x2-x1, y2-y1
            area = new_area
            i += 1

    i, w, h = i-1, w+1, h+1
    return i, minx, miny, w, h


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data)[0])


if __name__ == '__main__':
    main()
