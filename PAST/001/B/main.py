n = int(input())
prev = int(input())
for _ in range(n-1):
    a = int(input())
    if prev == a:
        print('stay')
    elif prev < a:
        print('up', a-prev)
    else:
        print('down', prev-a)
    prev = a
