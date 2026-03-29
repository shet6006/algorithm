import heapq
import sys
input = sys.stdin.readline
q = []
n = int(input())
for i in range(n):
    op = -int(input())
    if op == 0 and q:
        print(-heapq.heappop(q))
    elif op == 0 and not q:
        print(0)
    else:
        heapq.heappush(q,op)

#최대힙은 거꾸로