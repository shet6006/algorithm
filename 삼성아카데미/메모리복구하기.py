# 뒤집기 문제
# 00000과 입력을 비교 => 다를때까지 쭉 가기, 만나면 뒤집고, 반복
T_case = int(input())
for T in range(T_case):
    count = 0
    cur = 0
    n = input()
    for i in range(len(n)):
        if n[i] == "1":
            if cur == 0:
                count += 1
            cur = 1
        else:
            if cur == 1:
                count += 1
            cur = 0
    print('#'+str(T+1), count)