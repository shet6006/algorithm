import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
B = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr)-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    
    return 0

for x in B:
    print(binary_search(A,x))