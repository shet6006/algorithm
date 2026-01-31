import sys
input = sys.stdin.readline
test_case = int(input())
for tc in range(test_case):
    n = int(input())
    q = []
    for i in range(n):
        op, a = input().split()
        a = int(a)
        if op == 'I':
            q.append(a)
        if op == 'D' and a == 1 and q:
            q.remove(max(q))
        if op == 'D' and a == -1 and q:
            q.remove(min(q))
    if len(q) == 0:
        print('EMPTY')
    else:
        print(max(q), min(q))

