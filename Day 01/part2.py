input = open('../Day 10/in.txt', 'r')

a = None
b = None
c = None
previous = None
count = 0

for line in input.readlines():
    a = b
    b = c
    c = int(line)
    if previous and a and b and c and (a + b + c) > previous:
        count += 1
    if a and b and c:
        previous = a + b + c

print(count)