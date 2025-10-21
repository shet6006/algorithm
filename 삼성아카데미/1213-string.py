for i in range(1,11):
    j = int(input())
    string = input()
    sentence = input()

    result = 0
    start = 0

    while True:
        idx = sentence.find(string, start)
        if idx == -1:
            break
        result += 1
        start = idx + len(string)
    print('#' + str(i), result)
