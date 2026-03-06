def dfs(x, y):
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n and grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
            dfs(nx,ny)
    return 1

def dfs2(x, y):
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n and grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
            dfs2(nx,ny)
    return 1

n = int(input())
grid = []
count1, count2 = 0, 0
for i in range(n):
    grid.append(list(input()))

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count1 += dfs(i,j)

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count2 += dfs2(i,j)
print(count1, count2)