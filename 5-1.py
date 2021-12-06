class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


grid = [[0 for i in range(999)] for i in range(999)]

with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

for line in lines:
    nums = [int(num) for num in line.replace(' -> ', ',').split(',')]
    start = Coord(nums[0], nums[1])
    end = Coord(nums[2], nums[3])

    # horizontal
    if start.y == end.y:
        x = start.x
        for i in range(abs(start.x - end.x) + 1):
            grid[x][start.y] += 1
            x = x + 1 if start.x <= end.x else x - 1

    # vertical
    elif start.x == end.x:
        y = start.y
        for i in range(abs(start.y - end.y) + 1):
            grid[start.x][y] += 1
            y = y + 1 if start.y <= end.y else y - 1

count = 0
for row in grid:
    for cell in row:
        if cell > 1:
            count += 1

print(count)
