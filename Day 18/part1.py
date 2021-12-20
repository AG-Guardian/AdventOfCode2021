import ast
import math


def explodable(string: str) -> bool:
    if not string:
        return False

    depth = 0
    for char in string:
        if char == '[':
            depth += 1
            if depth > 4:
                return True
        elif char == ']':
            depth -= 1
    return False


def explode(string: str) -> str:
    left = [None, None]
    pair = [None, None]
    right = [None, None]
    previous = None
    depth = 0

    for index in range(len(string)):
        char = string[index]

        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char.isdigit():
            if previous == '[':
                left[0] = index
                left[1] = string.find(',', index) - 1
            elif previous == ',':
                left[0] = index
                left[1] = string.find(']', index) - 1

        if depth > 4:
            pair[0] = index
            pair[1] = string.find(']', index + 1)

            pair_left = [pair[0] + 1, string.find(',', pair[0] + 1) - 1]
            pair_right = [string.find(',', pair[0] + 1) + 1, pair[1] - 1]

            for right_index in range(pair[1], len(string)):
                if string[right_index].isdigit():
                    right[0] = right_index
                    while string[right_index + 1].isdigit():
                        right_index += 1
                    right[1] = right_index
                    break

            if left[0]:
                left_string = string[:left[0]]
                left_num = str(int(string[left[0]:left[1] + 1]) + int(string[pair_left[0]:pair_left[1] + 1]))
                left_between = string[left[1] + 1:pair[0]]
            else:
                left_string = string[:pair[0]]
                left_num = ''
                left_between = ''
            if right[0]:
                right_string = string[right[1] + 1:]
                right_num = str(int(string[right[0]:right[1] + 1]) + int(string[pair_right[0]:pair_right[1] + 1]))
                right_between = string[pair[1] + 1:right[0]]
            else:
                right_string = string[pair[1] + 1:]
                right_num = ''
                right_between = ''

            return f'{left_string}{left_num}{left_between}0{right_between}{right_num}{right_string}'

        previous = char


def splittable(string: str) -> bool:
    if not string:
        return False

    previous = ''
    for char in string:
        if char.isdigit() and previous.isdigit():
            return True
        previous = char
    return False


def split(string: str) -> str:
    previous = ''
    first_index = None
    last_index = None

    for index in range(len(string)):
        char = string[index]

        if not first_index:
            if char.isdigit() and previous.isdigit():
                first_index = index - 1
        elif not char.isdigit():
            last_index = index - 1

            left_string = string[:first_index]
            right_string = string[last_index + 1:]
            num = int(string[first_index:last_index + 1])
            left_num = str(math.floor(num / 2))
            right_num = str(math.ceil(num / 2))

            return f'{left_string}[{left_num},{right_num}]{right_string}'

        previous = char


def magnitude(obj) -> int:
    if isinstance(obj, list):
        return 3*magnitude(obj[0]) + 2*magnitude(obj[1])
    else:
        return obj


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

snumber = lines[0]
for line in range(1, len(lines)):
    snumber = f'[{snumber},{lines[line]}]'
    while True:
        if explodable(snumber):
            snumber = explode(snumber)
            continue
        elif splittable(snumber):
            snumber = split(snumber)
            continue
        else:
            break

print(snumber)
print(magnitude(ast.literal_eval(snumber)))
