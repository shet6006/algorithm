T = int(input())
for _ in range(T):
    left = []
    right = []
    cmd = input()
    for ch in cmd:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)
    print(''.join(left+right[::-1]))
