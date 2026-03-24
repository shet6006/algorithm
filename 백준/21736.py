from collections import deque
n, m = map(int,input().split())
grid = []
for i in range(n):
    grid.append(list(input()))
queue = deque()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'I':
            queue.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 'X':
            if grid[nx][ny] == 'O':
                grid[nx][ny] = 'I'
                queue.append((nx,ny))
            elif grid[nx][ny] == 'P':
                grid[nx][ny] = 'I'
                count += 1
                queue.append((nx,ny))
if count == 0:
    print("TT")
else:
    print(count)