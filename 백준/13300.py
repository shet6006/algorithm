n, k = map(int,input().split())
grade = [[0,0] for i in range(6)]
for i in range(n):
    s, g = map(int,input().split())
    if s == 0:
        grade[g-1][0] += 1
    elif s == 1:
        grade[g-1][1] += 1
count = 0
for i in range(len(grade)):
    for j in range(len(grade[i])):
        if  1 <= grade[i][j] and grade[i][j] <= k:
            count += 1
        elif grade[i][j] > k:
            count += (grade[i][j] + k - 1) // k
print(count)