import sys
sys.setrecursionlimit(100000)

def dfs(x,y, lv):
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
            if grid[nx][ny] > lv:
                dfs(nx,ny,lv)

    return 1

n = int(input())
grid = []
count = []
for i in range(n):
    grid.append(list(map(int,input().split())))
lv = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        lv = max(grid[i][j], lv)
for k in range(lv+1):
    visited = [[False]*n for _ in range(n)]
    a = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > k:
                a += dfs(i,j,k)
    count.append(a)
print(max(count))


# 비의 높이가 k일 때, k보다 큰 애들만 남기고 걔네를 구역