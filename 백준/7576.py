from collections import deque

queue = deque()

m, n = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs()
day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print('-1')
            exit()
        else:
            day = max(graph[i][j], day)
print(day-1)