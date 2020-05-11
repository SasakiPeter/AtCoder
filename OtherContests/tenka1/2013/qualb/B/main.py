q, L = map(int, input().split())
stack = []
size = 0
for _ in range(q):
    com, *query = input().split()
    if com == 'Push':
        q = tuple(map(int, query))
        stack.append(q)
        size += q[0]
        if L < size:
            print('FULL')
            break
    elif com == 'Pop':
        n = int(query[0])
        size -= n
        if size < 0:
            print('EMPTY')
            break
        cnt = 0
        while cnt != n:
            m, x = stack.pop()
            if n <= cnt+m:
                if n != cnt+m:
                    stack.append((cnt+m-n, x))
                cnt = n
            elif m < n:
                cnt += m
    elif com == 'Top':
        if size == 0:
            print('EMPTY')
            break
        print(stack[-1][1])
    elif com == 'Size':
        print(size)
else:
    print('SAFE')
