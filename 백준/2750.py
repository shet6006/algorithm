n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]


for i in range(n):
    print(lst[i])