closings = {'{': '}', '[': ']', '(': ')', '<': '>'}
openings = {'}': '{', ']': '[', ')': '(', '>': '<'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}


def stack_em_up(line: str):
    stack = []
    for char in line:
        if char in openings.values():
            stack.append(char)
        elif char in closings.values():
            if stack and openings[char] == stack[-1]:
                stack.pop()
            else:
                return char
        else:
            print("Bad input.")
    return None


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    error = stack_em_up(line)
    if error:
        total += points[error]

print(total)
