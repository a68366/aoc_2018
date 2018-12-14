def get_data():
    with open('input') as f:
        return f.read()


def part_1(data):
    data = int(data)
    scores = [3, 7]
    a, b = 0, 1
    while len(scores) < data + 10 + 1:
        val = scores[a] + scores[b]
        if val >= 10:
            scores.extend((val // 10 % 10, val % 10))
        else:
            scores.append(val % 10)
        a = (a + 1 + scores[a]) % len(scores)
        b = (b + 1 + scores[b]) % len(scores)

    return ''.join(str(x) for x in scores[data:data+10])


def part_2(data):
    scores = [3, 7]
    to_find = list(map(int, data))
    a, b = 0, 1

    while True:
        val = scores[a] + scores[b]
        if val >= 10:
            scores.extend((val // 10 % 10, val % 10))
        else:
            scores.append(val % 10)
        a = (a + 1 + scores[a]) % len(scores)
        b = (b + 1 + scores[b]) % len(scores)

        if scores[-len(to_find):] == to_find:
            return len(scores) - len(to_find)
        if scores[-len(to_find)-1:-1] == to_find:
            return len(scores) - len(to_find) - 1


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data))


if __name__ == '__main__':
    main()
