arr = []
n, m = map(int, input().split())
for _ in range(n):
    arr.append(int(input()))

arr.sort()

end = 0
answer = float('inf')

for start in range(n):
    while end < n:
        diff = arr[end] - arr[start]

        if diff < m:
            end += 1
        else:
            answer = min(answer, diff)
            break

print(answer)
