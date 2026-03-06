from collections import deque

n, m, h = map(int,input().split())
grid = []
queue = deque()
for k in range(h):
    layer = []
    for x in range(m):
        layer.append(list(map(int, input().split())))
        grid.append(layer)
        for y in range(n):
            if layer[y] == 1:
                queue.append((k,x,y))


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
while queue:
    z,x,y = queue.popleft()
for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]
    if 0<=nx<n and 0<=ny<m and 0<=nz<h:
        if grid[nz][nx][ny] == 0:
            grid[nz][nx][ny] = grid[z][x][y] +1
            queue.append((nz,nx,ny))
ans = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if grid[z][x][y] == 0:
                print(-1)
                exit()
            ans = max(ans, grid[z][x][y])

print(ans - 1)