# N, M = map(int, input().split())
# list = list(map(int, input().split()))
# ans = []
# l = 0
# for i in range(M):
#     k, m = map(int, input().split())
#     for j in range(k-1, m):
#         l += list[j]
#     ans.append(l)
#     l = 0
# for i in range(M):
#     print(ans[i])
# 틀린 풀이(시간초과)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list = list(map(int, input().split()))
pre = [0] # 누적합
mysum = 0

for i in range(n):
    mysum += list[i]
    pre.append(mysum)
# 5 3, 5 4 3 2 1 입력을 받았을 때, 5회 반복동안 누적합을 저장
# pre = [0, 5, 9, 12, 14, 15]
# 출력할 때에는 pre[1]부터 출력해야 하므로 pre[0]은 0으로 초기화

for i in range(m):
    a, b = map(int, input().split())
    print(pre[b] - pre[a-1]) # a-1을 빼주는 이유는 0부터 시작하기 때문
