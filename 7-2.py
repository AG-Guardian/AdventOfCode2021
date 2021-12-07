# fuel cost for a given distance
def cost(dist: int) -> int:
    return int(dist * (1 + dist) / 2)


with open('in.txt', 'r') as file:
    crabs = [int(pos) for pos in file.read().split(',')]

costs = []
hi = max(crabs)
lo = min(crabs)

# for each crab, build an array of fuel costs for each possible final position
for crab in crabs:
    costs.append([cost(abs(crab - fuel)) for fuel in range(lo, hi)])

# init an inversely sized array so that we can easily sum the columns
inverse = [[None for i in range(len(crabs))] for i in range(len(costs[0]))]

# fill the inversed array
for y in range(len(costs)):
    for x in range(lo, hi):
        inverse[x][y] = costs[y][x]

# print the lowest sum column of fuel costs
print(min([sum(costs) for costs in inverse]))
