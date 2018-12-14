from copy import deepcopy


def get_data():
    with open('input') as f:
        data = [list(line) for line in f.readlines()]
        return data


def find_repl(i, j, data, val):
    repl = data[i][j]
    if repl not in '<>^v':
        return repl
    elif val in '<>':
        return '-'
    else:
        return '|'


def next_step(i, j, val):
    if val == '>':
        return i, j+1
    elif val == '<':
        return i, j-1
    elif val == '^':
        return i-1, j
    elif val == 'v':
        return i+1, j


def init(data):
    field = deepcopy(data)
    moving = set('v^<>')
    turns = {('v', 0): '>', ('v', 1): 'v', ('v', 2): '<',
             ('^', 0): '<', ('^', 1): '^', ('^', 2): '>',
             ('<', 0): 'v', ('<', 1): '<', ('<', 2): '^',
             ('>', 0): '^', ('>', 1): '>', ('>', 2): 'v'}
    turn_states = {}
    straight = '-|'
    simples = '\\/'
    simple_turns = {('\\', 'v'): '>', ('\\', '<'): '^', ('\\', '^'): '<', ('\\', '>'): 'v',
                    ('/', 'v'): '<', ('/', '<'): 'v', ('/', '^'): '>', ('/', '>'): '^'}
    carts_count = 0
    carts = set()
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val in moving:
                carts_count += 1
                carts.add((i, j))

    return field, moving, turns, turn_states, straight, simples, simple_turns, carts, carts_count


def part_1(data):
    (field, moving, turns, turn_states,
     straight, simples, simple_turns, carts, _) = init(data)

    while True:
        new_carts = {}
        for i, j in sorted(carts):
            val = field[i][j]
            step = next_step(i, j, val)
            next_val = new_carts.get(step, field[step[0]][step[1]])
            if next_val in moving:
                return '{},{}'.format(*step[::-1])
            elif next_val in simples:
                new_carts[step] = simple_turns[(next_val, val)]
            elif next_val in straight:
                new_carts[step] = val
            else:
                turn = turn_states.get((i, j), 0) % 3
                new_carts[step] = turns[val, turn]
                turn_states[i, j] = turn + 1
            turn = turn_states.get((i, j))
            if turn is not None:
                turn_states[step[0], step[1]] = turn
                del turn_states[i, j]
            new_carts[(i, j)] = find_repl(i, j, data, val)

        carts.clear()
        for i, j in new_carts:
            val = new_carts[(i, j)]
            if val in moving:
                carts.add((i, j))
            field[i][j] = new_carts[(i, j)]


def part_2(data):
    (field, moving, turns, turn_states, straight,
     simples, simple_turns, carts, carts_count) = init(data)

    while carts_count > 1:
        new_carts = {}
        for i, j in sorted(carts):
            if (i, j) in new_carts:
                continue
            val = field[i][j]
            step = next_step(i, j, val)
            next_val = new_carts.get(step, field[step[0]][step[1]])
            if next_val in moving:
                carts_count -= 2
                new_carts[(i, j)] = find_repl(i, j, data, val)
                new_carts[step] = find_repl(step[0], step[1], data, next_val)
            elif next_val in simples:
                new_carts[step] = simple_turns[(next_val, val)]
            elif next_val in straight:
                new_carts[step] = val
            else:
                turn = turn_states.get((i, j), 0) % 3
                new_carts[step] = turns[val, turn]
                turn_states[i, j] = turn + 1
            turn = turn_states.get((i, j))
            if turn is not None:
                turn_states[step[0], step[1]] = turn
                del turn_states[i, j]
            new_carts[(i, j)] = find_repl(i, j, data, val)

        carts.clear()
        for i, j in new_carts:
            val = new_carts[(i, j)]
            if val in moving:
                carts.add((i, j))
            field[i][j] = new_carts[(i, j)]

    if carts:
        return '{},{}'.format(*reversed(next(iter(carts))))
    else:
        return 'No more carts'


def main():
    data = get_data()
    print('1:', part_1(data))
    print('2:', part_2(data))


if __name__ == '__main__':
    main()
