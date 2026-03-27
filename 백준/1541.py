#enumerate 활용

import sys
input = sys.stdin.readline

s = input().strip().split('-')
result = 0
for i, part in enumerate(s):
    arr = list(map(int,part.split('+')))
    if i == 0:
        result += sum(arr)
    else:
        result -= sum(arr)

print(result)