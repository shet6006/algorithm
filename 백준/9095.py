def dp(x):
    arr = [0] * 11
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    
    for i in range(4, x+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    return arr[x]
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for x in lst:
    print(dp(x))