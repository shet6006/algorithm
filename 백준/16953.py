import sys
input = sys.stdin.readline
count = 0
a, b = map(int,input().split())
while b > a:
    if str(b)[-1] == '1':
        b = b//10
        count +=1
    elif b % 2 == 0:
        b = b//2
        count += 1
    else:
        break
 
if b == a:
    print(count+1)
else:
    print('-1')

