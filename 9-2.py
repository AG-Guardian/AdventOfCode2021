class Point:
    def __init__(self, x: int, y: int, val: int, next=None):
        self.x = x
        self.y = y
        self.val = val
        self.next = next


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

# set up the grid as a 2d array of points
grid = [[Point(x, y, int(lines[y][x])) for x in range(len(lines[0]))] for y in range(len(lines))]
basins = dict([])

# edge indexes
top = 0
left = 0
bottom = len(grid) - 1
right = len(grid[0]) - 1

# determine the low points in the map
for y in range(len(grid)):
    for x in range(len(grid[0])):
        val = grid[y][x].val

        # check the (potential) 4 adjacent points to see if any are lower
        if val != 9:
            # Check right
            if x < right and grid[y][x + 1].val < val:
                val = grid[y][x + 1].val
                grid[y][x].next = grid[y][x + 1]
            # Check left
            if x > left and grid[y][x - 1].val < val:
                val = grid[y][x - 1].val
                grid[y][x].next = grid[y][x - 1]
            # Check down
            if y < bottom and grid[y + 1][x].val < val:
                val = grid[y + 1][x].val
                grid[y][x].next = grid[y + 1][x]
            # Check up
            if y > top and grid[y - 1][x].val < val:
                val = grid[y - 1][x].val
                grid[y][x].next = grid[y - 1][x]

            # if this point does not flow anywhere, it's a low point. Add an entry for this basin to track its size
            if not grid[y][x].next:
                basins[f'{x},{y}'] = 1

# for each point, find the low point it flows into and add 1 to the size of that basin
for y in range(len(grid)):
    for x in range(len(grid[0])):
        point = grid[y][x]

        # if this point flows somewhere, follow the flow to the low point
        if point.next:
            while point.next:
                point = point.next

            # once we have determined where this point flows to, we can increase its basin's size
            basins[f'{point.x},{point.y}'] += 1

# sort basins by size
sorted_basins = list(reversed(sorted(basins.values())))

if len(sorted_basins) >= 3:
    print(sorted_basins[0] * sorted_basins[1] * sorted_basins[2])
else:
    print("Failed to process input.")
