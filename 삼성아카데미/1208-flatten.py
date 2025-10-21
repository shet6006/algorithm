for j in range(1,11):
    dump = int(input())
    box = list(map(int,input().split()))
    box.sort()
    for i in range(dump):
        box[0] += 1
        box[-1] -= 1
        box.sort()
        if box[-1] - box[0] == 1 or box[-1] - box[0] == 0:
            break
    print('#' + str(j), box[-1] - box[0])