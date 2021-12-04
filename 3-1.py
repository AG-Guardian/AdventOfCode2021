input = open('in.txt', 'r').readlines()
bit_counts = [[0, 0] for i in range(len(input[0].strip()))]

for line in input:
    index = 0
    for char in line.strip():
        if char == '1':
            bit_counts[index][1] += 1
        elif char == '0':
            bit_counts[index][0] += 1
        index += 1

gamma = ''
epsilon = ''

for pair in bit_counts:
    if pair[0] > pair[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))
