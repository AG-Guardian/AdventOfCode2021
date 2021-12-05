def filter_input(input, criteria, index=0):
    ones = 0
    zeroes = 0

    for line in input:
        if len(line.strip()) > index:
            if line[index] == '1':
                ones += 1
            elif line[index] == '0':
                zeroes += 1

    if criteria == 'oxygen':
        if ones >= zeroes:
            result = list(filter(lambda line: line[index] == '1', input))
        else:
            result = list(filter(lambda line: line[index] == '0', input))
    elif criteria == 'carbon':
        if ones < zeroes:
            result = list(filter(lambda line: line[index] == '1', input))
        else:
            result = list(filter(lambda line: line[index] == '0', input))

    if len(result) == 1:
        return result[0]
    elif len(result) == 0 or len(input) == len(result):
        exit("Unable to process input.")
    else:
        return filter_input(result, criteria, index + 1)


input = open('in.txt', 'r').readlines()
oxygen = filter_input(input, 'oxygen')
carbon = filter_input(input, 'carbon')

print(int(oxygen, 2) * int(carbon, 2))
