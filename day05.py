def react(text):
    stack = []
    for letter in text:
        if not stack:
            stack.append(letter)
        else:
            l = stack[-1]
            if letter != l and l.lower() == letter.lower():
                stack.pop()
            else:
                stack.append(letter)

    return len(stack)


def part_1():
    with open('input') as f:
        text = f.read().strip()
        return react(text)


def part_2():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with open('input') as f:
        orig_text = f.read().strip()
        results = []

        for letter in letters:
            text = ''.join(l for l in orig_text if l not in (letter, letter.upper()))
            results.append(react(text))

        return min(results)


def main():
    print('1:', part_1())
    print('2:', part_2())


if __name__ == '__main__':
    main()
