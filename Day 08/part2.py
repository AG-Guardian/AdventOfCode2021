def decode(display: list) -> list:
    decoded = ['', '', '', '', '', '', '', '', '', '']

    # uniques [1, 4, 7, 8]
    for val in display:
        if len(val) == 2:
            decoded[1] = val
            continue
        elif len(val) == 4:
            decoded[4] = val
            continue
        elif len(val) == 3:
            decoded[7] = val
            continue
        elif len(val) == 7:
            decoded[8] = val
            continue

    # 6 segments [0, 6, 9]
    for val in [val for val in display if len(val) == 6 and val not in decoded]:
        if len(set(decoded[1]).union(val)) == 7:
            decoded[6] = val
            continue
        elif len(set(val) - set(decoded[4]).union(decoded[7])) == 1:
            decoded[9] = val
            continue
        else:
            decoded[0] = val
            continue

    # 5 segments [2, 3, 5]
    for val in [val for val in display if len(val) == 5 and val not in decoded]:
        if len(set(val) - set(decoded[1])) == 3:
            decoded[3] = val
            continue
        elif len(set(decoded[6]).union(val)) == 6:
            decoded[5] = val
            continue
        else:
            decoded[2] = val
            continue

    return [sorted(val) for val in decoded]


displays = []
values = []
total = 0

with open('../Day 10/in.txt', 'r') as file:
    for line in file.readlines():
        displays.append(line.split('|')[0].split())
        values.append(line.split('|')[1].split())

for i in range(len(displays)):
    decoded = decode(displays[i])
    output = ''
    for value in values[i]:
        output += str(decoded.index(sorted(value)))
    total += int(output)

print(total)
