import re


def get_data():
    with open('input') as f:
        data = [tuple(map(int, re.findall(r'(-?\d+)', s))) for s in f]
        return data


def distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def part_1(data):
    cons = [[data.pop(0)]]

    while data:
        for c in cons:
            for p1 in c:
                i = 0
                while i < len(data):
                    p2 = data[i]
                    if distance(p1, p2) <= 3:
                        c.append(data.pop(i))
                    else:
                        i += 1
        if data:
            cons.append([data.pop(0)])

    return len(cons)


def main():
    data = get_data()
    print('1:', part_1(data))


if __name__ == '__main__':
    main()
