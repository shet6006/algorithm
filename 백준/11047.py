n, k = map(int,input().split())
lst = []
for i in range(n):
    value = int(input())
    if value <= k:
        lst.append(value)
count = 0
while k != 0:
    count += k // lst[-1]
    k = k % lst[-1]
    lst.pop()
print(count)

# 정석
# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]

# count = 0
# for coin in reversed(coins):
#     if coin <= k:
#         count += k // coin
#         k %= coin

# print(count)