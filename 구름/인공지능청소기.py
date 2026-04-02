testCase = int(input())
for tc in range(testCase):
    x,y,n = map(int,input().split())
    c = abs(x) + abs(y)
    if c <= n and (c-n)%2 == 0:
        print('YES')
    else:
        print('NO')
        