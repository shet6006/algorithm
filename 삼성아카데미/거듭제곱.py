def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)
for tc in range(10):
    n = int(input())
    x, y = map(int, input().split())
    print('#'+str(tc+1), power(x,y))