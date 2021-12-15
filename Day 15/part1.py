class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []
        self.cost = None


def build_grid(lines: list):
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x, y)] = Node(int(lines[y][x]))
            if x > 0:
                grid[(x, y)].neighbors.append((x - 1, y))
            if x < len(lines[y]) - 1:
                grid[(x, y)].neighbors.append((x + 1, y))
            if y > 0:
                grid[(x, y)].neighbors.append((x, y - 1))
            if y < len(lines) - 1:
                grid[(x, y)].neighbors.append((x, y + 1))
    return grid


def ring_me_up(map: dict):
    if (0, 0) in grid.keys():
        grid[(0, 0)].cost = 0

    # calculate the cost of getting to any given point for each point in the grid
    # this must be run until no further improvements can be made
    improvements = True
    while improvements:
        improvements = False
        for node in map:
            for neighbor in map[node].neighbors:
                if not map[neighbor].cost:
                    map[neighbor].cost = map[node].cost + map[neighbor].val
                    improvements = True
                elif map[node].cost + map[neighbor].val < map[neighbor].cost:
                    map[neighbor].cost = map[node].cost + map[neighbor].val
                    improvements = True

    max_x = max([node[0] for node in grid.keys()])
    max_y = max([node[1] for node in grid.keys()])

    return grid[(max_x, max_y)].cost


with open('in.txt', 'r') as file:
    grid = build_grid(file.read().splitlines())

print(ring_me_up(grid))
