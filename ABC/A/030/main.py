a, b, c, d = map(int, input().split())
print('DRAW' if b/a == d/c else 'TAKAHASHI' if b/a > d/c else 'AOKI')

# この方が見やすい
# a, b, c, d = map(int, input().split())
# T, A = b/a, d/c
# print('TAKAHASHI' if T > A else 'AOKI' if T < A else 'DRAW')
