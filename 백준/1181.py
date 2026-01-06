N=int(input())
lists=[]
sort_list=[]
for i in range(N):
    lists.append(input())
lists=list(set(lists))
lists.sort()
lists.sort(key=len)
for i in range(len(lists)):
    print(lists[i])
lists.sort(lambda x : len(x))