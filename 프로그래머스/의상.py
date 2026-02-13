def solution(clothes):
    dict1 = {}
    # answer = 0
    # return answer
    comb = 1
    
    for cloth in clothes:
        if cloth[1] not in dict1:
            dict1[cloth[1]] = []
        dict1[cloth[1]].append(cloth[0])

    print(dict1)
    for key in dict1:
        comb *= (len(dict1[key]) + 1)

    return comb-1