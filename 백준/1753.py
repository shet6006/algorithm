import heapq
# 현재 노드를 기준으로 인접 노드까지의 거리 = 현재 거리 + 간선 가중치이며,
# 이 값이 기존 distance보다 작으면 distance를 갱신하고 힙에 넣는다.
# 다익스트라 알고리즘
# 간선 리스트를 인접 리스트로 변경
vertex, edge = map(int,input().split())
start = int(input())

graph = [[] for _ in range(vertex+1)]

for i in range(edge):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))
    # graph[v].append((u,w)) #무방향 그래프일 경우 필요

# 처음시작할 장소 빼고 inf로 초기화
INF = int(1e9)

distance = [INF] * (vertex + 1)
distance[start] = 0

# 힙 생성
q = []
heapq.heappush(q,(0,start))   # (거리, 노드)

# 다익스트라 시작
while q:
    dist, now = heapq.heappop(q)

    # 이미 더 짧은 경로가 있으면 무시
    if distance[now] < dist:
        continue

    # 현재 노드와 연결된 노드 탐색
    for next_node, weight in graph[now]:
        cost = dist + weight

        # 기존 거리보다 작으면 갱신
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q,(cost,next_node))

# 결과 출력
for i in range(1, vertex+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])