import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    area = 1  # 현재 그림 넓이

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                area += dfs(nx, ny)

    return area


count = 0        # 그림 개수
max_area = 0     # 가장 큰 그림 넓이

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            count += 1
            max_area = max(max_area, dfs(i, j))

print(count)
print(max_area)
