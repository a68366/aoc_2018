from collections import deque
from itertools import cycle
import re


def get_data():
    with open('input') as f:
        return tuple(map(int, re.findall(r'(\d+)', f.read())))


def part_1(players, last_value):
    marbles = [0, 1]
    scores = [0] * players
    value = 1
    curr_idx = 1

    for player in cycle(range(players)):
        value += 1
        if value > last_value:
            break
        if value % 23 == 0:
            curr_idx = (curr_idx - 8 + len(marbles)) % len(marbles) + 1
            scores[player] += value + marbles.pop(curr_idx)
        else:
            curr_idx = (curr_idx + 1) % len(marbles) + 1
            marbles.insert(curr_idx, value)

    return max(scores)


def part_2(players, last_value):
    # part_1 is too slow
    # return part_1(players, last_value*100)

    marbles = deque([0, 1])
    scores = [0] * players
    value = 1

    for player in cycle(range(players)):
        value += 1
        if value > last_value:
            break
        if value % 23 == 0:
            marbles.rotate(-7)
            scores[player] += value + marbles.pop()
        else:
            marbles.rotate(2)
            marbles.append(value)

    return max(scores)


def main():
    players, last_value = get_data()
    print('1:', part_1(players, last_value))
    print('2:', part_2(players, last_value*100))


if __name__ == '__main__':
    main()
