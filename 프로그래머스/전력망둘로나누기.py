def dfs(v, visited, graph, count):
    visited[v] = True
    count[0] += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph, count)

def solution(n, wires):
    answer = n
    graph = [[] for i in range(n+1)]
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]

        for j, wire in enumerate(wires):
            if i == j: continue  # 끊기로 한 전선은 건너뜀
            u, v = wire
            graph[u].append(v)
            graph[v].append(u)

        count = [0]
        visited = [False] * (n+1)
        dfs(1, visited, graph, count)
        diff = abs(count[0] - (n - count[0]))
        answer = min(answer, diff)
    return answer
#원래는 하나로 연결
#끊었을 때 노드 개수 dfs, 반대는 전체 노드 - dfs
#지금 그래프에서 간선을 하나씩 끊는 방법 고안 필요 => 걍 간선 관계를 하나씩 빼고 append?하면될듯