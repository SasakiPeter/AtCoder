# それぞれの移動を何回行ったかをカウントする
MOD = 10**9+7
x, y = map(int, input().split())
# (+1, +2), (+2, +1)の移動をそれぞれn,m回行ったとすると
# 2n+m=y, n+2m=xが成り立つ
# ここから、3m=2x-y, 3n=2y-x(0<=x,y)が導かれる
n, r1 = divmod(2*y-x, 3)
m, r2 = divmod(2*x-y, 3)


def com(n, r):
    X = Y = 1
    if r < 0 or n < r:
        return 0
    if n-r < r:
        r = n-r
    for i in range(1, r+1):
        Y = Y*i % MOD
        X = X*(n-i+1) % MOD
    Y = pow(Y, MOD-2, MOD)
    return X*Y % MOD


if r1 or r2:
    print(0)
else:
    print(com(n+m, n))


# # プロットしてみると、二項係数になっている
# MOD = 10**9+7
# X, Y = map(int, input().split())
# x, y = X, Y
# while 0 <= y:
#     if x == 2*y:
#         break
#     x += 1
#     y -= 1
# else:
#     print(0)
#     exit()


# def com(n, r):
#     X = Y = 1
#     if r < 0 or n < r:
#         return 0
#     if n-r < r:
#         r = n-r
#     for i in range(1, r+1):
#         Y = Y*i % MOD
#         X = X*(n-i+1) % MOD
#     Y = pow(Y, MOD-2, MOD)
#     return X*Y


# print(com(x//2, x-X) % MOD)
