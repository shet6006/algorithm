import sys
input = sys.stdin.readline

left = list(input().rstrip())
m = int(input())
right = []

for _ in range(m):
    cmd = input().rstrip()
    if not cmd:
        continue
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'R':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'D':                 
        if right:
            left.append(right.pop())
    else: 
        _, x = cmd.split(maxsplit=1)
        left.append(x)

print(''.join(left + right[::-1]))
