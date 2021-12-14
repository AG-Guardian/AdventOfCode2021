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

    grid = [[' ' for x in range(width + 1)] for y in range(depth + 2)]

    for coord in coords:
        grid[coord[1]][coord[0]] = '#'

    return grid


def merge_lines(a: list, b: list) -> list:
    for index in range(len(a)):
        if a[index] != ' ':
            b[index] = a[index]
    return b


def fold_grid(grid: list, instructions: list) -> list:
    for instruction in instructions:
        axis = instruction.split('=')[0][-1]
        line = int(instruction.split('=')[1])
        new = []

        if axis == 'y':
            top = grid[:line]
            bottom = list(reversed(grid[line + 1:]))

            for index in range(len(bottom)):
                new.append(merge_lines(bottom[index], top[index]))
            grid = new

        elif axis == 'x':
            left = [grid[y][:line] for y in range(len(grid))]
            right = [list(reversed(grid[y][line + 1:])) for y in range(len(grid))]

            for index in range(len(right)):
                new.append(merge_lines(right[index], left[index]))
            grid = new

    return grid


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

separator = lines.index('')
instructions = lines[separator + 1:]
grid = setup_grid(lines[:separator])
grid = fold_grid(grid, instructions)

for line in grid:
    print(''.join(line))