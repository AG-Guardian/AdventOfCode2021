with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

# set up the grid as a 2d array of ints
grid = [[int(lines[y][x]) for x in range(len(lines[0]))] for y in range(len(lines))]
count = 0

# for each point, check to see if it is a low point
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

        # if we made it here, this is a low point
        count += 1 + val

print(count)
