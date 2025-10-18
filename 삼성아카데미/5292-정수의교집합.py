# n, m = map(int, input().split())
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# # set으로 비교해서 a[0]과 b[0]이 같아질떄까지 삭제, 같아지면 그 다음거?
# print(a)
# print(b)
# print(a&b)

testcase = int(input())
for i in range(testcase):
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    num = len(a&b)
    print('#' + str(i+1) ,num)