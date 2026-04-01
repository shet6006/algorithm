import math

n = int(input())
exclude_n = round(n * 0.15)

level = []
for i in range(n):
    level.append(int(input()))

level.sort() 

result = 0
up = n - exclude_n

for i in range(exclude_n, up):
    result += level[i]

count = n - (2 * exclude_n)

if count == 0:
    print(0)
else:
    print(round(result / count))