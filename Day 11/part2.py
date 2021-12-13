class Dumbo:
    def __init__(self, x: int, y: int, val: int):
        self.x = x
        self.y = y
        self.val = val
        self.flashed = False


def flash_me(squid: Dumbo):
    if not squid.flashed:
        squid.val += 1
        if squid.val > 9:
            return True
    return False


def flash_neighbors(grid: list, x: int, y: int):
    neighbors = []
    if x < 9:
        if flash_me(grid[y][x + 1]):
            neighbors.append(grid[y][x + 1])
    if x > 0:
        if flash_me(grid[y][x - 1]):
            neighbors.append(grid[y][x - 1])
    if y < 9:
        if flash_me(grid[y + 1][x]):
            neighbors.append(grid[y + 1][x])
    if y > 0:
        if flash_me(grid[y - 1][x]):
            neighbors.append(grid[y - 1][x])
    if x < 9 and y < 9:
        if flash_me(grid[y + 1][x + 1]):
            neighbors.append(grid[y + 1][x + 1])
    if x > 0 and y > 0:
        if flash_me(grid[y - 1][x - 1]):
            neighbors.append(grid[y - 1][x - 1])
    if y < 9 and x > 0:
        if flash_me(grid[y + 1][x - 1]):
            neighbors.append(grid[y + 1][x - 1])
    if y > 0 and x < 9:
        if flash_me(grid[y - 1][x + 1]):
            neighbors.append(grid[y - 1][x + 1])

    return neighbors


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

squid_grid = [[Dumbo(x, y, int(lines[y][x])) for x in range(len(lines[y]))] for y in range(len(lines))]
all_flashed = False
day = 0

while not all_flashed:
    flashers = []
    for y in range(len(squid_grid)):
        for x in range(len(squid_grid[y])):
            squid = squid_grid[y][x]
            squid.val += 1
            if squid.val > 9:
                flashers.append(squid)

    while flashers:
        for squid in flashers:
            if not squid.flashed:
                squid.flashed = True
                neighbors = flash_neighbors(squid_grid, squid.x, squid.y)
                if neighbors:
                    flashers.extend(neighbors)
                flashers.remove(squid)
            else:
                flashers.remove(squid)

    all_flashed = True
    for y in range(len(squid_grid)):
        for x in range(len(squid_grid[y])):
            squid = squid_grid[y][x]
            if squid.flashed:
                squid.flashed = False
                squid.val = 0
            else:
                all_flashed = False
    day += 1


print(day)
