from collections import defaultdict
n = int(input())
fruit = list(map(int,input().split()))

count = defaultdict(int)
left = 0
max_len = 0

for right in range(n):
    count[fruit[right]] += 1
    
    while len(count) > 2:
        count[fruit[left]] -= 1
        if count[fruit[left]] == 0:
            del count[fruit[left]]
        left += 1
    max_len = max(max_len, right-left+1)

print(max_len)
from collections import defaultdict

n = int(input())
fruit = list(map(int, input().split()))

result = 0

for start in range(n):
    count = defaultdict(int)
    kind = 0  # 과일 종류 수

    for end in range(start, n):
        # 새로운 과일 추가
        if count[fruit[end]] == 0:
            kind += 1
        count[fruit[end]] += 1

        # 종류 2개 초과하면 중단
        if kind > 2:
            break

        result = max(result, end - start + 1)

print(result)