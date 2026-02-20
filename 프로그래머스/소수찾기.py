import math
from itertools import permutations

def solution(numbers):
    answer = 0
    arr = list(numbers)
    result = set()
    for i in range(1, len(arr)+1):
        for p in permutations(arr, i):
            result.add(int(''.join(p)))
    for num in result:
        if int(num) < 2:
            continue
        is_prime = True

        for i in range(2, int(math.sqrt(int(num)))+1):
            if int(num) % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    
    return answer
