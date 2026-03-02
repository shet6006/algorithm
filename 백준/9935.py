import sys

n = sys.stdin.readline().strip()
boom = list(sys.stdin.readline().strip())
b_len = len(boom)

stack = []

for char in n:
    stack.append(char)
    if len(stack) >= b_len and stack[-b_len:] == boom:
        for _ in range(b_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")