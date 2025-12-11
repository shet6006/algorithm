n, s = map(int,input().split())
arr = list(map(int, input().split()))
count = 0

def dfs(idx, current_sum):
    global count

    if idx == n:
        if current_sum == s:
            count += 1
        return
    dfs(idx+1, current_sum + arr[idx])

    dfs(idx+1, current_sum)

dfs(0,0)
if s == 0:
    count -= 1
print(count)