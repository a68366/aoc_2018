from collections import defaultdict


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def uniq_min_idx(data):
    uniq = True
    idx = 0
    for i, val in enumerate(data):
        if val < data[idx]:
            uniq = True
            idx = i
        elif val == data[idx]:
            uniq = False

    return idx if uniq else None


def both():
    with open('input') as f:
        coords = set()
        top = left = float('inf')
        bot = right = 0

        for line in f:
            x, y = map(int, line.split(','))
            top = min(top, y)
            bot = max(bot, y)
            left = min(left, x)
            right = max(right, x)
            coords.add((x, y))

        coords = list(sorted(coords))

        not_inf = lambda p: left < p[0] < right and top < p[1] < bot

        count = defaultdict(int)
        result_2 = 0
        for i in range(left, right):
            for j in range(top, bot):
                distances = [dist((i, j), c) for c in coords]

                mn = uniq_min_idx(distances)
                if mn is not None:
                    count[coords[mn]] += 1

                if sum(distances) < 10000:
                    result_2 += 1

        result_1 = 0
        for point, val in count.items():
            if not_inf(point):
                result_1 = max(result_1, val)

        return result_1, result_2


def main():
    print('Both:', *both())


if __name__ == '__main__':
    main()
