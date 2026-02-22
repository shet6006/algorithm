def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop(-1)
            k -= 1
        stack.append(num)
    if k != 0:
        for i in range(k):
            stack.pop(-1)
    result = ''.join(stack)
    return result
