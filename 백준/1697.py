from collections import deque

n, m = map(int,input().split())
visited = [-1] * 100001
queue = deque([n])
visited[n] = 0

while queue:
    v = queue.popleft()

    if v == m:
        print(visited[m])
        break
    else:
        for i in (v-1, v+1, v*2):
            if 0<= i <= 100000 and visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)
