n = int(input())
lst = list(map(int,input().split()))
count = 0
for i in range(n):
    if lst[i] == 1:
        continue
    for j in range(2, lst[i]):
        if lst[i]%j==0:
            break
    else:
        count += 1

print(count)