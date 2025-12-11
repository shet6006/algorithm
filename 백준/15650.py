from itertools import combinations
n, m = map(int,input().split())
lst=[]
for i in range(1,n+1):
    lst.append(i)
for i in combinations(lst, m):
    print(*i)
