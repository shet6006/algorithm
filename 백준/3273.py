n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 값이 있는지 표시하는 불리언 배열 (1~1,000,000 범위)
exists = [False] * 1000001

for num in arr:
    exists[num] = True

count = 0
for num in arr:
    target = x - num
    if 0 < target <= 1000000 and exists[target]:
        count += 1

# (a, b), (b, a) 두 번 세니까 절반으로 나눔
print(count // 2)
