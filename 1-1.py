input = open('in.txt', 'r')

previous = None
count = 0
for line in input.readlines():
    if previous and int(line) > int(previous):
        count += 1
    previous = line

print(count)