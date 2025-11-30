NUM_CHART = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}
 
T = int(input())
for _ in range(1, T + 1):
    test_case, length = input().split()
    arr = input().split()
    test_case = int(test_case[1:])
    arr.sort(key=lambda x: NUM_CHART[x])
    print("#{0}".format(test_case), " ".join(arr))
