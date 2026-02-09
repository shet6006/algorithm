from collections import defaultdict

tc = int(input())
for _ in range(tc):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        _, kind = input().split()
        clothes[kind] += 1

    ans = 1
    for cnt in clothes.values():
        ans *= (cnt + 1)

    print(ans - 1)
