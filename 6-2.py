with open('in.txt', 'r') as file:
    fishes = [int(day) for day in file.read().split(',')]

fish_by_day = [fishes.count(day) for day in range(9)]

for day in range(256):
    fish_by_day.append(fish_by_day.pop(0))
    fish_by_day[6] += fish_by_day[8]

print(sum(fish_by_day))
