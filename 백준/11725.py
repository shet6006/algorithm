import sys
sys.setrecursionlimit(10**7) # 런타임에러: 리커전에러 방지

def dfs(graph, v, visited):
    global parent
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph, i, visited)

# 1번의 요소 2개가 부모
# 부모로 탐색을 했을 때, 각각의 자식들의 부모
n = int(input())
graph = [[] for _ in range(1,n+2)]
parent = [0] * (n + 1)
visited = [False] * (n+2)
for i in range(1, n):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(graph, 1, visited)
for i in range(2, n+1):
    print(parent[i])

# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# def dfs(v):
#     for nxt in graph[v]:
#         if parent[nxt] == 0:      # 아직 방문 안 한 노드
#             parent[nxt] = v       # 부모 지정 = 방문 처리
#             dfs(nxt)

# n = int(input())
# graph = [[] for _ in range(n + 1)]

# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# parent = [0] * (n + 1)

# parent[1] = -1   # 루트 방문 처리
# dfs(1)

# for i in range(2, n + 1):
#     print(parent[i])
