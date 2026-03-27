n, k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    lan_num = 0
    for lan in arr:
        lan_num += lan//mid
    if lan_num >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)