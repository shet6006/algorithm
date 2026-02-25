import sys
input = sys.stdin.readline
str1 = list(input().rstrip())
str2 = list(input().rstrip())
if len(str1)>len(str2):
    str1, str2 = str1, str2
count = 0
for i in str1:
    if i in str2:
        str2.remove(i)
        count += 1
print(len(str1)- count + len(str2))
