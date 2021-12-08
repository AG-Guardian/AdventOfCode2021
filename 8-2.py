def decode(display: list) -> list:
    s = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
    }

    while display:
        display = [val for val in display if val not in s.values()]
        for val in display:
            if s[6] and s[8] and s[3] and len(val) == 6 and len(set(val) - set(s[3])) == 2:
                s[0] = val
                continue
            elif len(val) == 2:
                s[1] = val
                continue
            elif len(display) == 1:
                s[2] = val
                continue
            elif s[1] and len(set(val) - set(s[1])) == 3:
                s[3] = val
                continue
            elif len(val) == 4:
                s[4] = val
                continue
            elif len(val) == 5 and s[6] and len(set(s[6]).union(val)) == 6:
                s[5] = val
                continue
            elif s[1] and len(val) == 6 and len(set(s[1]).union(val)) == 7:
                s[6] = val
                continue
            elif len(val) == 3:
                s[7] = val
                continue
            elif len(val) == 7:
                s[8] = val
                continue
            elif s[6] and s[0] and len(val) == 6:
                s[9] = val
                continue

    return [sorted(val) for val in list(s.values())]


displays = []
values = []
total = 0

with open('in.txt', 'r') as file:
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
