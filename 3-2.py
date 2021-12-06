def filter_input(input_lines, criteria, index=0):
    ones = 0
    zeroes = 0

    for line in input_lines:
        if len(line) > index:
            if line[index] == '1':
                ones += 1
            elif line[index] == '0':
                zeroes += 1

    if criteria == 'oxygen':
        if ones >= zeroes:
            result = list(filter(lambda line: line[index] == '1', input_lines))
        else:
            result = list(filter(lambda line: line[index] == '0', input_lines))
    elif criteria == 'carbon':
        if ones < zeroes:
            result = list(filter(lambda line: line[index] == '1', input_lines))
        else:
            result = list(filter(lambda line: line[index] == '0', input_lines))

    if len(result) == 1:
        return result[0]
    elif len(result) == 0 or len(input_lines) == len(result):
        exit("Unable to process input.")
    else:
        return filter_input(result, criteria, index + 1)


with open('in.txt', 'r') as file:
    input_lines = file.read().splitlines()

oxygen = filter_input(input_lines, 'oxygen')
carbon = filter_input(input_lines, 'carbon')

print(int(oxygen, 2) * int(carbon, 2))
