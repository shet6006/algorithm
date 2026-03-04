def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    print(A,B)
    for i in range(len(A)):
        multiple = A[i]*B[i]
        answer += multiple

    return answer