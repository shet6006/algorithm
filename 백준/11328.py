n = int(input())
for i in range(n):
    str1, str2 = input().split()
    str1 = list(str1)
    str2 = list(str2)
    if len(str1) != len(str2):
        print('Impossible')
        continue
    for s in str1:
        if s in str2:
            str2.remove(s)
    if str2:
        print('Impossible')
    else:
        print('Possible')