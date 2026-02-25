n = int(input())
lst = [] #[4,3,6,8,7,5,2,1]
stack = []
answer = []
for i in range(n):
    lst.append(int(input()))

i = 0
while lst:
    if lst[0] in stack and lst[0] == stack[-1]:
        answer.append(stack.pop())
        lst.pop(0)
        print('-')
    elif lst[0] not in stack:
        while i != lst[0]:
            i += 1
            stack.append(i)
            print('+')
    else:
        print('NO')
        break