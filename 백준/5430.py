from collections import deque
# reverse flag와 deque이용해서 풀기
tc = int(input())
for i in range(tc):
    op = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    queue = deque(arr)
    flag = True #정방향

    if n == 0:
        queue = []

    for operand in op:
        if operand == 'R':
            flag = not flag
        elif operand == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if flag:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")