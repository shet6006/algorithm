def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            count1 += 1
        if answers[i] == second[i%8]:
            count2 += 1
        if answers[i] == third[i%10]:
            count3 += 1
    
    scores = [count1, count2, count3]
    max_score = max(scores)
    
    answer = []
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i+1)  # 사람 번호는 1부터
    
    return answer
