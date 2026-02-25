n = int(input())
arr = list(map(int, input().split()))
x = int(input())

exists = [False] * 1000001

for num in arr:
    exists[num] = True

count = 0
for num in arr:
    target = x - num
    if 0 < target <= 1000000 and exists[target]:
        count += 1

print(count // 2)
