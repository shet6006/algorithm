from itertools import combinations
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
result = 1
mod = 1
for i in range(n-k+1,n+1):
    result *= i
for i in range(1, k+1):
    mod *= i
print((result//mod)%10007)