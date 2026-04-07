from collections import deque

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


result = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    result.append(sum(visited))

print(result.index(min(result))+1)