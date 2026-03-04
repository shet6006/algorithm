def solution(s):
    answer = []
    count = 0
    zero_count = 0
    
    while len(s) != 1:
        a = []
        c = []
        for i in s:
            if int(i) == 1:
                a.append(i)
            else:
                zero_count += 1
        b = len(a)
        while b != 1:
            c.append(b%2)
            b = b//2
        c.append(1)
        c.sort(reverse=True)
        s = c
        count += 1
    answer.append(count)
    answer.append(zero_count)
    return answer