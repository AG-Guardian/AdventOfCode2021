with open('../Day 10/in.txt', 'r') as file:
    crabs = [int(pos) for pos in file.read().split(',')]

hi = max(crabs)
lo = min(crabs)

# for each crab, build an array of fuel costs for each possible final position
costs = [[abs(crab - pos) for crab in crabs] for pos in range(lo, hi)]

# print the lowest sum of fuel costs
print(min([sum(vals) for vals in costs]))
