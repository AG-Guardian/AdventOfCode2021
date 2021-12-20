def probe_me(x_velocity: int, y_velocity: int, x_min: int, x_max: int, y_min: int, y_max: int):
    x = 0
    y = 0
    highest = 0

    # are we aiming the right direction?
    if (x_velocity > 0 and x_min < 0) or (x_velocity < 0 and x_min > 0):
        return False, highest

    # deal with negative values
    x_velocity = abs(x_velocity)
    x_max = abs(x_max)
    x_min = abs(x_min)
    temp = min(y_min, y_max)
    y_max = max(y_min, y_max)
    y_min = temp

    # can we even make it?
    farthest = sum([x for x in range(x_velocity + 1)])
    if farthest < x_min:
        return False, highest

    passed_max = y >= y_max

    while x < x_max:
        x += x_velocity
        y += y_velocity

        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1

        if y > highest:
            highest = y

        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True, highest

        # if we are already falling and we miss the target, break
        if not passed_max:
            passed_max = y >= y_max
        elif y <= y_min:
            break

    return False, highest


with open('in.txt', 'r') as file:
    target = file.read()

x_str = target[target.index('x=') + 2:target.index(',')]
y_str = target[target.index('y=') + 2:]

x_min = int(x_str.split('..')[0])
x_max = int(x_str.split('..')[1])

y_min = int(y_str.split('..')[0])
y_max = int(y_str.split('..')[1])


# to avoid doing any sort of math, lets just go dumbo mode
hits = []
for x in range(abs(x_max) + 1):
    for y in range(y_min, 1000):
        hit, height = probe_me(x, y, x_min, x_max, y_min, y_max)
        if hit:
            hits.append(height)

print(len(hits))
