n, s = map(int,input().split())
arr = list(map(int, input().split()))
end = 0
count = float('inf')
interval_sum = 0
for start in range(n):
    while end < n and interval_sum < s:
        interval_sum += arr[end]
        end += 1
    if  interval_sum >= s:
        count = min(count, end-start)
    interval_sum -= arr[start]
if count == float('inf'):
    print(0)
else:
    print(count)
