n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
k = sum(B)-sum(A)

if k < 0:
    print('No')
else:
    cnt_a = cnt_b = 0
    for a, b in zip(A, B):
        if a < b:
            x, y = divmod((b-a), 2)
            cnt_a += x+y
            cnt_b += y
        elif b < a:
            cnt_b += b-a
    if max(cnt_a, cnt_b) <= k:
        print('Yes')
    else:
        print('No')
