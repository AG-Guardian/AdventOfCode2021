with open('../Day 10/in.txt', 'r') as file:
    fishes = [int(day) for day in file.read().split(',')]

fish_by_day = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for day in fishes:
    fish_by_day[day] += 1

for day in range(256):
    # shift up the populations for each day (decrementing the timer)
    fish_by_day.append(fish_by_day.pop(0))
    # add back in the mothers at day 6 that were just converted to fresh spawn at day 8
    fish_by_day[6] += fish_by_day[8]

print(sum(fish_by_day))
