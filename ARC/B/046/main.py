# 石取れなくなったら負け
n = int(input())
A, B = map(int, input().split())
if A == B:
    if n % (A+1) == 0:
        print('Aoki')
    else:
        print('Takahashi')
elif A < B and A < n:
    print('Aoki')
else:
    print('Takahashi')
