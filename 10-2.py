closings = {'{': '}', '[': ']', '(': ')', '<': '>'}
openings = {'}': '{', ']': '[', ')': '(', '>': '<'}
points = {')': 1, ']': 2, '}': 3, '>': 4}


def stack_em_up(line: str):
    score = 0
    stack = []

    for char in line:
        if char in openings.values():
            stack.append(char)
        elif char in closings.values():
            if stack and openings[char] == stack[-1]:
                stack.pop()
            else:
                return None
        else:
            print("Bad input.")

    while stack:
        score *= 5
        score += points[closings[stack.pop()]]

    return score


with open('in.txt', 'r') as file:
    lines = file.read().splitlines()

scores = []
for line in lines:
    score = stack_em_up(line)
    if score:
        scores.append(score)

print(sorted(scores)[len(scores) // 2])
