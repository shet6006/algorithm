n, m = map(int, input().split())

no_hear = set()
no_see = set()

for _ in range(n):
    no_hear.add(input().strip())

for _ in range(m):
    no_see.add(input().strip())

result = sorted(no_hear & no_see)

print(len(result))
for name in result:
    print(name)