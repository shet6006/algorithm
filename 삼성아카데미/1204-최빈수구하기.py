n = int(input())
for i in range(n):
    num = int(input())
    scores = list(map(int, input().split()))
    numbers = [0] * 101
    for i in scores:
        numbers[i] += 1
    print('#' + str(num), len(numbers) - 1 - numbers[::-1].index(max(numbers)))
