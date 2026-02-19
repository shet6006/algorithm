def solution(sizes):
    for i in sizes:
        if i[0] > i[1]: # (작은 수, 큰 수)
            i[0], i[1] = i[1], i[0]
    m, n = 0, 0
    for i in sizes:
        m = max(i[0], m)
        n = max(i[1], n)
    answer = m*n
    return answer