from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    db = defaultdict(list)

    # 1. info 전처리
    for line in info:
        lang, job, career, food, score = line.split()
        score = int(score)

        for l in (lang, '-'):
            for j in (job, '-'):
                for c in (career, '-'):
                    for f in (food, '-'):
                        db[(l, j, c, f)].append(score)

    # 2. 점수 정렬
    for key in db:
        db[key].sort()

    # 3. query 처리
    answer = []
    for q in query:
        q = q.replace("and ", "")
        l, j, c, f, score = q.split()
        score = int(score)

        scores = db[(l, j, c, f)]
        cnt = len(scores) - bisect_left(scores, score)
        answer.append(cnt)

    return answer
