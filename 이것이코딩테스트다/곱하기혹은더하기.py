s = input()
digits = list(map(int,s))       # ['1', '2', '3', '4', '5']
print(digits)
result = digits[0]
# 0이나 1이 아니면 모두 곱하기가 이득
for i in digits[1:]:
    if i > 1 and result > 1:
        result *= i
    else:
        result += i
print(result)