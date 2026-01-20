tc = int(input())
for t_case in range(tc):
    n, a, b = map(int, input().split())
    ans = [[] for _ in range(n+1)]

    for i in range(0, n+1):
        for j in range(0, i+1):
            if i == 0 or j == 0 or j == i:
                ans[i].append(1)
            else:
                ans[i].append(ans[i-1][j-1] + ans[i-1][j])

    print(f"#{t_case+1} {ans[n][b]}")
