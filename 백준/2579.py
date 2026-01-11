n = int(input())
d = [int(input()) for _ in range(n)]
dp = [0] * n
if len(d) <= 2:
    print(sum(d))
else:
    dp[0] = d[0]
    dp[1] = d[1] + d[0]
    dp[2] = max(d[0] + d[2], d[1] + d[2])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + d[i], dp[i-3] + d[i-1] + d[i])

    print(dp[-1])