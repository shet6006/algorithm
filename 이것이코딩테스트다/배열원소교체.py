# 배열 A를 오름차순 정렬, 배열 B를 내림차순 정렬
# k개만큼 배열 A원소와 B의 원소 교체
# 배열 A의 합
from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
a = deque(a)
b.sort(reverse = True)
result = 0
for i in range(k):
    a.popleft()
    a.append(b[i])
for i in range(len(a)):
    result += a[i]

print(result)