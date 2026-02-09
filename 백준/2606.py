def dfs(graph, v, visited):
    global count
    count += 1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(graph, 1, visited)
print(count-1)