import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((e, s))  # (끝나는시간, 시작시간)
# 끝나는 시간 기준, 같으면 시작시간 기준으로 정렬
meetings.sort()
print(meetings)

count = 0
end_time = 0

for e, s in meetings:
    if s >= end_time:
        count += 1
        end_time = e

print(count)
