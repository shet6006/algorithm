n = int(input())
s = set()
for i in range(n):

    op = input().split()

    if len(op) == 1:
        cmd = op[0]
        
        if cmd == 'all':
            s = set(range(1, 21))
        elif cmd == 'empty':
            s = set()

    else:
        cmd, num = op
        num = int(num)

        if cmd == 'add':
            s.add(num)
        elif cmd == 'check':
            print(1 if num in s else 0)
        elif cmd == 'remove':
            s.discard(num)
        elif cmd == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)