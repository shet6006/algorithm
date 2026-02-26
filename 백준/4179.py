from collections import deque

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))
j_queue = deque()
f_queue = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            graph[i][j] = 0
            j_queue.append((i,j))
        if graph[i][j] == 'F':
            f_queue.append((i,j))

def bfs():
    while j_queue and f_queue:
        x, y = j_queue.popleft()
        f_x, f_y = f_queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nf_x = f_x + dx[i]
            nf_y = f_y + dy[i]
            if 0 <= nf_x < r and 0 <= nf_y < c:
                graph[nf_x][nf_y] = '#'
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
                graph[nx][ny] = graph[x][y] + 1
bfs()
print(graph)
###############################
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

fire_dist = [[-1] * c for _ in range(r)] # 불이 붙는 시간 기록
j_dist = [[-1] * c for _ in range(r)]    # 지훈이가 도착하는 시간 기록

f_q = deque()
j_q = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            f_q.append((i, j))
            fire_dist[i][j] = 0
        elif graph[i][j] == 'J':
            j_q.append((i, j))
            j_dist[i][j] = 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 1. 불의 BFS (불이 각 칸에 도달하는 최단 시간 계산)
while f_q:
    x, y = f_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != '#' and fire_dist[nx][ny] == -1:
                fire_dist[nx][ny] = fire_dist[x][y] + 1
                f_q.append((nx, ny))

# 2. 지훈이의 BFS (탈출 가능한지 확인)
while j_q:
    x, y = j_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # [탈출 조건] 범위를 벗어나면 탈출 성공!
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            print(j_dist[x][y] + 1)
            exit()
            
        if graph[nx][ny] != '#' and j_dist[nx][ny] == -1:
            # 불이 아직 안 붙었거나(fire_dist == -1), 
            # 지훈이가 불보다 "먼저" 도착할 수 있는 경우만 이동
            if fire_dist[nx][ny] == -1 or j_dist[x][y] + 1 < fire_dist[nx][ny]:
                j_dist[nx][ny] = j_dist[x][y] + 1
                j_q.append((nx, ny))

print("IMPOSSIBLE")