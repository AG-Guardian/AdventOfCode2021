class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []
        self.cost = None


def build_thicc_grid(lines: list):
    # build a template map from input values
    template = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            template[(x, y)] = int(lines[y][x])

    max_x = max([node[0] for node in template.keys()]) + 1
    max_y = max([node[1] for node in template.keys()]) + 1

    # use the template to build out the larger map
    grid = {}
    for y_offset in range(5):
        for x_offset in range(5):
            for y in range(max_y):
                for x in range(max_x):
                    # calculate the current x and y
                    current_x = x + (max_x * x_offset)
                    current_y = y + (max_y * y_offset)

                    # calculate the new value based on the position and original template value
                    val = (template[(x, y)] + x_offset + y_offset) % 9
                    if val == 0:
                        val = 9

                    # create the Node and find the keys of its neighbors
                    node = grid[(current_x, current_y)] = Node(val)
                    if current_x > 0:
                        node.neighbors.append((current_x - 1, current_y))
                    if current_x < (max_x * 5) - 1:
                        node.neighbors.append((current_x + 1, current_y))
                    if current_y > 0:
                        node.neighbors.append((current_x, current_y - 1))
                    if current_y < (max_y * 5) - 1:
                        node.neighbors.append((current_x, current_y + 1))

    # replace neighbor keys with values to save time on lookups later
    for node in grid.values():
        node.neighbors = [grid[neighbor] for neighbor in node.neighbors]

    return grid


def ring_me_up(map: dict):
    # init the cost of the starting point
    if (0, 0) in grid.keys():
        grid[(0, 0)].cost = 0
    else:
        raise KeyError

    # calculate the cost of getting to any given point for each point in the grid
    # this must be run until no further improvements can be made to guarantee the best path is found
    improvements = True
    while improvements:
        improvements = False
        for node in map.values():
            for neighbor in node.neighbors:
                new_cost = node.cost + neighbor.val
                # have we calculated a cost?
                if neighbor.cost:
                    # is it cheaper to get there from here?
                    if new_cost < neighbor.cost:
                        neighbor.cost = new_cost
                        improvements = True
                else:
                    neighbor.cost = node.cost + neighbor.val
                    improvements = True

    max_x = max([node[0] for node in grid.keys()])
    max_y = max([node[1] for node in grid.keys()])

    return grid[(max_x, max_y)].cost


with open('in.txt', 'r') as file:
    grid = build_thicc_grid(file.read().splitlines())

print(ring_me_up(grid))
