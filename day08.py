def get_data():
    with open('input') as f:
        return list(map(int, f.read().strip().split()))


def part_1(data):
    children = []
    meta = []
    i = 0
    result = 0

    while i != len(data):
        if not children:
            children.append(data[i])
            continue
        if not meta:
            meta.append(data[i])
            continue

        ch_cnt = children[-1]
        meta_cnt = meta[-1]

        if ch_cnt == 0:
            result += sum(data[i:i+meta_cnt])
            i += meta_cnt
            children.pop()
            meta.pop()
            children[-1] -= 1
        else:
            children.append(data[i])
            meta.append(data[i+1])
            i += 2

    return result


def part_2(data):
    ch_cnt, meta_cnt = data[:2]
    data = data[2:]
    values = []

    for _ in range(ch_cnt):
        value, data = part_2(data)
        values.append(value)

    if ch_cnt == 0:
        return sum(data[:meta_cnt]), data[meta_cnt:]
    else:
        value = 0
        for k in data[:meta_cnt]:
            if k-1 in range(len(values)):
                value += values[k-1]
        return value, data[meta_cnt:]


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data)[0])


if __name__ == '__main__':
    main()
