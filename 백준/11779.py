import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

start, end = map(int,input().split())

INF = int(1e9)
distance = [INF] * (n+1)
distance[start] = 0

parent = [0] * (n+1)

q = []
heapq.heappush(q,(0,start))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            parent[next_node] = now   # ⭐ 핵심
            heapq.heappush(q,(cost,next_node))

# 경로 복원
path = []
cur = end
while cur != 0:
    path.append(cur)
    cur = parent[cur]

path.reverse()

print(distance[end])
print(len(path))
print(*path)