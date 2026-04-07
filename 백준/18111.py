#기회비용: 파는데 2초, 놓는데 1초
#높이 256블록일때는 파기만 하고, 0일때는 놓기만하기

# 1 2 3
# 4 5 6
# 7 8 9
grid = []
n, m, b = map(int,input().split())
for i in range(n):
    grid.append(list(map(int,input().split())))

min_time = float('inf')
best_height = 0
for target in range(257):
    time = 0
    inventory = b

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] - target < 0:
                time += abs(grid[i][j] - target)
                inventory -= abs(grid[i][j] - target)
            else:
                time += abs(grid[i][j] - target) * 2
                inventory += abs(grid[i][j] - target)
    if inventory < 0:
        continue
    if time < min_time or (time == min_time and target > best_height):
        min_time = time
        best_height = target
print(min_time, best_height)
