# n = int(input())
# list=[]
# while n > 10:
#     list.append(n%10)
#     n = n//10
# list.append(n)
# list.sort(reverse = True)
# n = int(''.join(map(str,list)))
# print(n)

n = list(map(int, str(input())))
n.sort(reverse=True)
for i in n:
    print(i, end='')