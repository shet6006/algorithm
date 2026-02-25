n = int(input())
arr = list(map(int,input().split()))
v = int(input())
count = 0
for a in arr:
    if v == a:
        count += 1
print(count)