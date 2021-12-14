def setup_grid(points: list) -> list:
    width = 0
    depth = 0
    coords = set()

    for coord in points:
        x = int(coord.split(',')[0])
        y = int(coord.split(',')[1])
        coords.add((x, y))
        width = x if x > width else width
        depth = y if y > depth else depth

    grid = [[' ' for x in range(width + 1)] for y in range(depth + 1)]

    for coord in coords:
        grid[coord[1]][coord[0]] = '0'

    return grid


def merge_lines(a: list, b: list):
    for index in range(len(a)):
        if a[index] != ' ':
            b[index] = a[index]
    return b


def fold_grid(grid: list, instructions: list):
    for instruction in instructions:
        axis = instruction.split('=')[0][-1]
        line = int(instruction.split('=')[1])

        if axis == 'y':
            top = list(reversed(grid[:line]))
            bottom = grid[line + 1:]

            while len(bottom) > len(top):
                top.append([' ' for x in range(len(top[0]))])

            new = []
            for index in range(len(bottom)):
                new.append(merge_lines(bottom[index], top[index]))
            grid = list(reversed(new))

        elif axis == 'x':
            left = [list(reversed(grid[y][:line])) for y in range(len(grid))]
            right = [grid[y][line + 1:] for y in range(len(grid))]

            while len(left[0]) > len(right[0]):
                right = [line.append(' ') for line in right]

            new = []
            for index in range(len(left)):
                new.append(merge_lines(left[index], right[index]))
            grid = [list(reversed(line)) for line in new]

        count = 0
        for line in grid:
            count += line.count('0')

        print(count)

    return grid


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

separator = lines.index('')
instructions = lines[separator + 1:]
grid = setup_grid(lines[:separator])

grid = fold_grid(grid, instructions)