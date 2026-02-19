def solution(brown, yellow):
    answer = []
    a = (brown-4)/2
    a = int(a)
    for i in range(a, 0, -1):
        if (a-i)*i == yellow:
            answer.append(a-i+2)
            answer.append(i+2)
            break
    answer.sort(reverse=True)
    
    return answer
# (brown-4)/2 1,9 2,8 ... 4,6 > 곱했을때 24
# 3 1,2 
