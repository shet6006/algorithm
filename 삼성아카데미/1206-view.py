# 입력받은 애들을 탐색
# 왼쪽, 그 왼쪽보다 본인이 커야함
# 왼쪽, 그 왼쪽 중 큰 것(max?)과 비교해서 본인 빼기 그 값
# 오른쪽에도 같은 알고리즘 적용 후 min연산
# 카운트 측정
n = int(input())
height = list(map(int, input().split()))
result = 0
print(height)
for i in range(2, len(height)-2):
    if height[i] > (height[i-1]) and height[i] > (height[i-2]) and height[i] > height[i+1] and height[i] > height[i+2]:
        left_max = height[i] - max(height[i-1],height[i-2])
        right_max = height[i] - max(height[i+1], height[i+2])
        result += min(left_max, right_max)
print(result)