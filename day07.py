import re


def get_data(filename='input'):
    with open(filename) as f:
        text = f.read().strip()
        lookup = {}
        extractor = re.compile(r'[Ss]tep\s+(\w+)')
        nodes = set()
        for line in text.splitlines():
            a, b = extractor.findall(line)
            nodes.update((a, b))
            lookup.setdefault(b, set()).add(a)

    return sorted(nodes), lookup


def part_1(nodes, lookup):
    result = ''
    visited = set()
    while len(visited) != len(nodes):
        for node in nodes:
            if node in visited:
                continue
            if not lookup.get(node, set()) - visited:
                result += node
                visited.add(node)
                break

    return result


def part_2(nodes, lookup):
    workers = 5
    seconds = -1
    visited = set()
    preparing = {}
    while len(visited) != len(nodes):
        for k in list(preparing.keys()):
            preparing[k] -= 1
            if preparing[k] == 0:
                visited.add(k)
                del preparing[k]

        for node in nodes:
            if node in visited or node in preparing:
                continue
            if len(preparing) == workers:
                break
            if not lookup.get(node, set()) - visited:
                preparing[node] = 60 + ord(node) - 64

        seconds += 1

    return seconds


def main():
    data = get_data()
    print('1:', part_1(*data))
    print('2:', part_2(*data))


if __name__ == '__main__':
    main()
