import math

with open('in.txt', 'r') as file:
    template = file.readline().strip()
    lines = file.read().splitlines()
    lines.remove('')

letters = set([char for char in template])

for line in lines:
    letters.update([char for char in line if char.isalpha()])

pairs = {}
for one in letters:
    for two in letters:
        pairs[(one, two)] = 0

for index in range(len(template) - 1):
    pairs[(template[index], template[index + 1])] += 1

rules = {}
for one in letters:
    for two in letters:
        rules[(one, two)] = None

for line in lines:
    rules[(line[0], line[1])] = line[-1]

for steps in range(40):
    new = pairs.copy()
    for pair in pairs.keys():
        if pairs[pair] > 0 and rules[pair]:
            new[(pair[0], rules[pair])] += pairs[pair]
            new[(rules[pair], pair[1])] += pairs[pair]
            new[pair] -= pairs[pair]
    pairs = new.copy()


letters = {}
for pair in pairs.keys():
    if pair[0] not in letters.keys():
        letters[pair[0]] = pairs[pair]
    else:
        letters[pair[0]] += pairs[pair]
    if pair[1] not in letters.keys():
        letters[pair[1]] = pairs[pair]
    else:
        letters[pair[1]] += pairs[pair]

for letter in letters.keys():
    letters[letter] = math.ceil(letters[letter] / 2)

vals = list(sorted(letters.values()))
print(vals[-1] - vals[0])