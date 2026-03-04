def solution(numbers, target):
    answer = 0
    sum = 0
    index = 0
    def a(target, sum, index):
        nonlocal answer
        
        if index == len(numbers):
            if sum == target:
                answer += 1
            return
        a(target, sum+numbers[index], index+1)
        a(target, sum-numbers[index], index+1)
        
    a(target,sum, index)
    return answer
