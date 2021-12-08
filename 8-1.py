values = []

with open('in.txt', 'r') as file:
    for line in file.readlines():
        values.append(line.split('|')[1].split())

count = 0
for row in values:
    for val in row:
        count = count + 1 if len(val) in [2, 4, 3, 7] else count

print(count)