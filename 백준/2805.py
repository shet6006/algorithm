import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = list(map(int,input().split()))
start = 0
end = max(tree)
while start <= end:
    tree_len = 0

    mid = (start + end) // 2
    for t in tree:
        if t > mid:
            tree_len += t - mid
            if tree_len >= m:
                break

    if tree_len >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)