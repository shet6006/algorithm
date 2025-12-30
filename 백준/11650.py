import sys
input = sys.stdin.readline

n = int(input())
coordinates = []

for i in range(n):
    coordinates_x, coordinates_y = map(int,input().split())
    coordinates.append((coordinates_x, coordinates_y))

coordinates.sort(key = lambda x: (x[0], x[1]))


for x, y in coordinates:
    print(x, y)