def solution(n, w, num):

    answer = 0
    box = [[] for _ in range(w)]
    direction = True
    count = 0
    
    for i in range(n):
        count += 1
        
        if count > w:
            direction = not direction
            count = 1
        
        if direction:
            box[i % w].append(i+1)
        else:
            box[w-(i % w)-1].append(i+1)

    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == num:
                answer = len(box[i])-j
    return answer
    