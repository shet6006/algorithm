def solution(priorities, location):
    queue = list(enumerate(priorities))
    count = 0

    while True:
        cur = queue.pop(0)

        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == location:
                return count
