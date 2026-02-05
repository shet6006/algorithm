import sys
input = sys.stdin.readline

k, l = map(int, input().split())
dict1 = {}

for i in range(l):
    dict1[int(input())] = i

sorted_items = sorted(dict1.items(), key=lambda x: x[1])

for i in range(min(k, len(sorted_items))):
    print(sorted_items[i][0])
# dict.items()함수, key = lambda 잘 활용