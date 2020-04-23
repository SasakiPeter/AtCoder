# 負の蝋燭を何本ともすかを決めると自然に最小の時間が求まる
# 負方向の蝋燭を何本ともすかはO(n)で全部探索できるので終わり

n, k = map(int, input().split())
# X = []
# Y = []
X, Y = [], []
for x in map(int, input().split()):
    if x < 0:
        # X.append(x)
        X.append(-x)
    else:
        Y.append(x)
X.reverse()
INF = 10**9
ans = INF
# print(X, Y)
if len(X) == 0:
    ans = Y[k-1]
elif len(Y) == 0:
    ans = X[k-1]
    # ans = X[k-1]*(-1)
else:
    # for i in range(k):
    for i in range(1, k):
        # L = k-i-1
        # R = i-1
        L, R = k-i-1, i-1
        # print(len(X), len(Y))
        # if L >= len(X) or R >= len(Y):
        if not(L < len(X) and R < len(Y)):
            continue
        # a = X[L]
        # # a = X[L]*(-1)
        # b = Y[R]
        a, b = X[L], Y[R]
        ans = min(ans, min(a, b)+a+b)
print(ans)
