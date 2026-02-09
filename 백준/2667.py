def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[x][y] == 0:
        return 0

    graph[x][y] = 0
    cnt = 1  

    cnt += dfs(x, y-1)
    cnt += dfs(x-1, y)
    cnt += dfs(x+1, y)
    cnt += dfs(x, y+1)

    return cnt

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            size = dfs(i, j)
            result.append(size)

result.sort()
print(len(result))
for x in result:
    print(x)
