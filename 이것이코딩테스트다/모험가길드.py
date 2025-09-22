N = int(input())
horror = list(map(int, input().split()))
horror.sort()
count = 0
result = 0
for i in horror:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
# 큰 놈들부터
# list원소 n으로 list 앞에서부터 n씩 빼기
# 1, 2,3,6,6,6,7,7,7
