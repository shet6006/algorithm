def dfs(x,y):
    if graph[x][y] == 0:
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    else:

n, m = int(map, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        dfs(0,0)

