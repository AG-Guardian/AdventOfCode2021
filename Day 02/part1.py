input = open('../Day 10/in.txt', 'r')

x = 0
y = 0

for line in input.readlines():
    if ' ' in line:
        distance = int(line.split(' ')[1])
        if 'forward' in line:
            x += distance
        elif 'up' in line:
            y -= distance
        elif 'down' in line:
            y += distance

print(x * y)