import sys
sys.setrecursionlimit(10000)
TC = int(input())
for test_case in range(TC):
    m, n, k = map(int,input().split())
    count = 0
    qocn = [[0]*n for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        qocn[x][y] = 1
    def dfs(x, y):
        qocn[x][y] = -1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and qocn[nx][ny] == 1:
                dfs(nx,ny)
        return 1
    for i in range(m):
        for j in range(n):
            if qocn[i][j] == 1:
                count += dfs(i,j)
    print(count)