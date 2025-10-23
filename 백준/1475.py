

n = input()
number = [0]*10
for i in n:
    if int(i) == 9:
        number[6] += 1
    else:
        number[int(i)] += 1
number[6] = (number[6]+1) // 2
print(max(number))
    
