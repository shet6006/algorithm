import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict1 = {}
for _ in range(n):
    k, v = input().split()
    dict1[k] = v
    
for _ in range(m):
    a = input().rstrip()
    print(dict1[a])