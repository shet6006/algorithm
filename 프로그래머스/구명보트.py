def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people)-1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
            
    return answer
## 카운터 활용
# from collections import Counter

# def solution(k, tangerine):
#     # 단 한 줄로 개수 세기 + 정렬 준비 완료
#     counts = sorted(Counter(tangerine).values(), reverse=True)
    
#     answer = 0
#     for c in counts:
#         k -= c
#         answer += 1
#         if k <= 0: break
#     return answer