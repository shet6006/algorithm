from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sorted(permutations(arr, m))

for i in ans:
    print(*i)