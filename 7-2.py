def cost(dist):
    return int(dist * (1 + dist) / 2)

with open('in.txt', 'r') as file:
    crabs = [int(pos) for pos in file.read().split(',')]

costs = []
hi = max(crabs)
lo = min(crabs)
for crab in crabs:
    costs.append([cost(abs(crab - fuel)) for fuel in range(lo, hi)])

inv = [[None for i in range(len(crabs))] for i in range(len(costs[0]))]
for y in range(len(costs)):
    for x in range(lo, hi):
        inv[x][y] = costs[y][x]

print(min([sum(list) for list in inv]))