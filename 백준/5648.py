import sys
input = sys.stdin.readline
lst = []
n = input().split()
a = int(n[0])
n.remove(n[0])
while len(n) != a:
    n += list(map(int,input().split()))

for i in range(len(n)):
    n[i] = int(n[i])

for i in range(a):
    n[i] = int(str(n[i])[::-1])

n.sort()
for i in range(len(n)):
    print(n[i])

# import sys
# input = sys.stdin.readline

# # 모든 입력을 한 번에 읽어서 공백 기준으로 분리
# data = sys.stdin.read().split()

# n = int(data[0])      # 첫 번째 값: 개수
# nums = data[1:]       # 나머지 숫자들

# result = []

# for i in range(n):
#     reversed_num = int(nums[i][::-1])  # 문자열 뒤집고 int 변환
#     result.append(reversed_num)

# result.sort()

# for x in result:
#     print(x)
