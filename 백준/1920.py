import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

lst.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for x in lst2:
    print(binary_search(lst, x))
