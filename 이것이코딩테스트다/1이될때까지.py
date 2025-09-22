n, k = map(int, input().split())
print(n,k)
count = 0
while True:
    #target은 n이 k의 배수가 되는 가장 가까운 수
    target = (n // k) * k
    count += n - target
    n = target
    if n < k:
        break
    count += 1
    n //= k
count += (n - 1)
print(count)
# 예시 트레이스
# 예: n = 25, k = 3

# target = (25 // 3) * 3 = 24
# result += 25 - 24 = 1 → result = 1, n = 24
# 나누기: result += 1 → 2, n = 24 // 3 = 8

# target = (8 // 3) * 3 = 6
# result += 8 - 6 = 2 → result = 4, n = 6
# 나누기: result += 1 → 5, n = 6 // 3 = 2

# 이제 n < k(2 < 3)이므로 루프 종료.
# 마지막 처리: result += (n - 1) = 1 → 최종 6

# 실제로 25를 1로 만드는 최소 횟수도 6이 맞습니다.