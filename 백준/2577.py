a = int(input())
b = int(input())
c = int(input())
answer = str(a*b*c)
lst = [0]*10
for ans in answer:
    if ans == '0':
        lst[0] += 1
    if ans == '1':
        lst[1] += 1
    if ans == '2':
        lst[2] += 1
    if ans == '3':
        lst[3] += 1
    if ans == '4':
        lst[4] += 1
    if ans == '5':
        lst[5] += 1
    if ans == '6':
        lst[6] += 1
    if ans == '7':
        lst[7] += 1
    if ans == '8':
        lst[8] += 1
    if ans == '9':
        lst[9] += 1
for i in range(len(lst)):
    print(lst[i])
        