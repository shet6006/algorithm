import sys
input = sys.stdin.readline # 빠른 입력을 위해 필수!

n = int(input())
current = 1  # 다음에 스택에 넣을 숫자
stack = []
op = []
possible = True

for _ in range(n):
    num = int(input())
    
    # 입력받은 숫자(num)까지 스택에 push
    while current <= num:
        stack.append(current)
        op.append('+')
        current += 1
    
    # 스택의 맨 위 숫자가 입력받은 숫자와 같다면 pop
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        # 스택의 맨 위가 num이 아니면 해당 수열을 만들 수 없음
        possible = False
        break

if possible:
    print('\n'.join(op))
else:
    print('NO')