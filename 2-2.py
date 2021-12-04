input = open('in.txt', 'r')

x = 0
y = 0
aim = 0

for line in input.readlines():
    if ' ' in line:
        distance = int(line.split(' ')[1])
        if 'forward' in line:
            x += distance
            y += distance * aim
        elif 'up' in line:
            aim -= distance
        elif 'down' in line:
            aim += distance

print(x * y)