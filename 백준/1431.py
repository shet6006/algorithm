import sys
input = sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]

def digit_sum(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total

lst.sort(key=lambda x: (len(x), digit_sum(x), x))

for s in lst:
    print(s)
