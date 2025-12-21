from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
B = list(map(int, input().split()))

for x in B:
    print(bisect_right(A, x) - bisect_left(A, x), end=" ")
