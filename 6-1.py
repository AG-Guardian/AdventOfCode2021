with open('in.txt', 'r') as file:
    fishes = [int(fish) for fish in file.read().split(',')]

for day in range(60):
    spawns = []
    for index in range(len(fishes)):
        if fishes[index] == 0:
            spawns.append(8)
            fishes[index] = 6
        else:
            fishes[index] -= 1
    fishes += spawns

print(len(fishes))

# going back and looking at this after part 2 makes me feel like a maroon
