n, m = map(int, input().split())

# 1次元配列２つの方が、圧倒的にメモリが少なくて済むし、実行時間も早い
# 後、コードも書きやすい

num = [1]*n
red = [1] + [0]*(n-1)

for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    num[x] -= 1
    num[y] += 1

    if red[x]:
        red[y] = 1
    if num[x] == 0:
        red[x] = 0

print(sum(red))

# A = [[1, 1]] + [[0, 1] for _ in range(n-1)]

# for _ in range(m):
#     x, y = map(lambda x: int(x) - 1, input().split())
#     # print(A)
#     A[x][1] -= 1
#     A[y][1] += 1
#     if A[x][0]:
#         A[y][0] = 1

#     if A[x][1] == 0:
#         A[x][0] = 0

# print(sum(a[0] for a in A))
