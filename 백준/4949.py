while True:
    line = input()
    if line == ".":
        break
    is_true = True
    stack = []
    for ch in line:
        if ch == '(':
            stack.append(ch)
        elif ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                is_true = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                is_true = False
                break
    if is_true and not stack:
        print('yes')
    else:
        print('no')
    
# (, [가 들어오면 추가, ), ]가 들어왔을 때 스택 최상단(stack[-1])이 짝이 안 맞거나, 스택이 비어있다면 다음 글자,
# 짝이 맞다면, 팝