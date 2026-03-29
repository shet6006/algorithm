import sys
sys.setrecursionlimit(10000)
n, m = map(int,input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
