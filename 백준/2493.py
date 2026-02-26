import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = [] # (탑의 인덱스, 탑의 높이)를 저장
answer = [0] * n

for i in range(n):
    # 현재 탑보다 낮은 탑들은 스택에서 다 제거 (나한테 가려져서 의미가 없음)
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    
    # 만약 스택에 남아있는 탑이 있다면, 그 탑이 바로 현재 탑의 신호를 받는 탑임
    if stack:
        answer[i] = stack[-1][0] + 1 # 인덱스는 0부터 시작하므로 +1
    
    # 현재 탑 정보를 스택에 넣음 (다음 탑들에게는 내가 신호를 받을 후보가 됨)
    stack.append((i, towers[i]))
    print(stack)
print(*(answer))