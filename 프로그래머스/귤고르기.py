from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dict1 = defaultdict(int)
    for i in range(len(tangerine)):
        dict1[tangerine[i]] += 1

    sorted_items = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
    for i in sorted_items:
        if k<=0:
            return answer
        k-=sorted_items[i]
        answer+=1
    return answer
