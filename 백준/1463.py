import sys
sys.setrecursionlimit(1000000)

n = int(input())
memo = [-1] * (n + 1)

def dp(x):
    if x == 1:
        return 0
    
    if memo[x] != -1:
        return memo[x]
    
    res = dp(x - 1) + 1

    if x % 2 == 0:
        res = min(res, dp(x // 2) + 1)

    if x % 3 == 0:
        res = min(res, dp(x // 3) + 1)
    
    memo[x] = res
    return res

print(dp(n))

# 바텀업
# n = int(input())
# dp = [0] * (n + 1)

# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)

# print(dp[n])
