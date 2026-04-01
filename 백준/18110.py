import math

n = int(input())

if n == 0:
    print(0)
    exit()

exclude_n = int(n * 0.15 + 0.5)

level = []
for i in range(n):
    level.append(int(input()))

level.sort()

result = 0
up = n - exclude_n

for i in range(exclude_n, up):
    result += level[i]

count = n - (2 * exclude_n)

print(int(result / count + 0.5))