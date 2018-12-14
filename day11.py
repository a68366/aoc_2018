def get_data():
    with open('input') as f:
        return int(f.read())


def sum_square(field, x, y, sz=3):
    result = 0
    for i in range(x, x+sz):
        for j in range(y, y+sz):
            result += field[i][j]
    return result


def part_1(data):
    return '{},{}'.format(*part_2(data, 3)[:-1])


def part_2(data, one_sz=None):
    # I used pypy and it took a few minutes to produce the result

    field = [[0]*300 for _ in range(300)]
    for i in range(len(field)):
        for j in range(len(field)):
            rack_id = i + 1 + 10
            power = (rack_id * (j+1) + data) * rack_id
            power = power // 100 % 10 - 5
            field[i][j] = power

    mx = float('-inf')
    point = None
    if one_sz:
        rng = range(one_sz, one_sz+1)
    else:
        rng = range(1, len(field))
    for sz in rng:
        for i in range(len(field)-sz):
            for j in range(len(field)-sz):
                t = sum_square(field, i, j, sz)
                if t > mx:
                    mx = t
                    point = (i+1, j+1, sz)
    return point


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data))


if __name__ == '__main__':
    main()
