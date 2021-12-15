class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []
        self.cost = None


def build_thicc_grid(lines: list):
    template = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            template[(x, y)] = Node(int(lines[y][x]))

    max_x = max([node[0] for node in template.keys()]) + 1
    max_y = max([node[1] for node in template.keys()]) + 1

    grid = {}
    for y_offset in range(5):
        for x_offset in range(5):
            for y in range(max_y):
                for x in range(max_x):
                    current_x = x + (max_x * x_offset)
                    current_y = y + (max_y * y_offset)
                    
                    val = template[(x, y)].val + ((x_offset + y_offset) % 9)
                    while val > 9:
                        val = val % 9
                        if val == 0:
                            val = 9
                        
                    grid[(current_x, current_y)] = Node(val)
                    
                    if current_x > 0:
                        grid[(current_x, current_y)].neighbors.append((current_x - 1, current_y))
                    if current_x < (max_x * 5) - 1:
                        grid[(current_x, current_y)].neighbors.append((current_x + 1, current_y))
                    if current_y > 0:
                        grid[(current_x, current_y)].neighbors.append((current_x, current_y - 1))
                    if current_y < (max_y * 5) - 1:
                        grid[(current_x, current_y)].neighbors.append((current_x, current_y + 1))

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
    grid = build_thicc_grid(file.read().splitlines())

print(ring_me_up(grid))
