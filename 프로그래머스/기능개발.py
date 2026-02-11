from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        count = 0
        while progresses[i] + speeds[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        queue.append(count)
    current = queue.popleft()
    count = 1

    while queue:
        if queue[0] <= current:
            queue.popleft()
            count += 1
        else:
            answer.append(count)
            current = queue.popleft()
            count = 1

    answer.append(count)
    return answer