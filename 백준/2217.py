import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()
answers = []
for k in lst:
    answers.append(k*n)
    n -= 1
print(max(answers))