with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

# set up the grid as a 2d array of ints
grid = [[int(lines[y][x]) for x in range(len(lines[0]))] for y in range(len(lines))]
basins = dict([])

# determine the low points in the map
for y in range(len(grid)):
    for x in range(len(grid[0])):
        val = grid[y][x]

        # check the (potential) 4 adjacent points to see if any are lower
        if x < len(grid[y]) - 1:
            if grid[y][x + 1] <= val:
                continue
        if x > 0:
            if grid[y][x - 1] <= val:
                continue
        if y < len(grid) - 1:
            if grid[y + 1][x] <= val:
                continue
        if y > 0:
            if grid[y - 1][x] <= val:
                continue

        # if we made it here, this is a low point. Add an entry for this basin
        basins[f'{x},{y}'] = 0

# for each point, find the low point it flows into and add 1 to the size of that basin
for y in range(len(grid)):
    for x in range(len(grid[0])):
        val = grid[y][x]
        if val != 9:
            x1 = x
            y1 = y

            # follow the flow towards the lowest point until we hit the low point in a basin
            while f'{x1},{y1}' not in basins.keys():
                adjacent = []
                if x1 < len(grid[y1]) - 1:
                    if grid[y1][x1 + 1] < val:
                        y2 = y1
                        x2 = x1 + 1
                        val = grid[y2][x2]
                if x1 > 0:
                    if grid[y1][x1 - 1] < val:
                        y2 = y1
                        x2 = x1 - 1
                        val = grid[y2][x2]
                if y1 < len(grid) - 1:
                    if grid[y1 + 1][x1] < val:
                        y2 = y1 + 1
                        x2 = x1
                        val = grid[y2][x2]
                if y1 > 0:
                    if grid[y1 - 1][x1] < val:
                        y2 = y1 - 1
                        x2 = x1
                        val = grid[y2][x2]
                x1 = x2
                y1 = y2

            # once we have determined where this point flows to, we can increase its basin's size
            basins[f'{x1},{y1}'] += 1

# print out the product of the 3 largest basins
sorted_basins = list(reversed(sorted(basins.values())))
if len(sorted_basins) >= 3:
    print(sorted_basins[0] * sorted_basins[1] * sorted_basins[2])
else:
    print("Failed to process input.")
