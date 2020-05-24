# 二分探索解の存在判定
n, m = map(int, input().split())
AB = [tuple(map(int, input().split()))for _ in range(n)]
CD = [tuple(map(int, input().split()))for _ in range(m)]


def check(x):
    ab = [b-x*a for a, b in AB]
    ab.sort(reverse=True)
    cd = max([d-x*c for c, d in CD])
    val = sum(ab[:4]) + max(ab[4], cd)
    return 0 <= val


L = 0
R = 10**6
while "{:.7f}".format(L) != "{:.7f}".format(R):
    M = (L+R)/2
    if check(M):
        L = M
    else:
        R = M
print("{:.7f}".format(L))

# # DPと思ったが、よく考えたらこれDAGにならない...
# n, m = map(int, input().split())
# AB = [tuple(map(int, input().split()))for _ in range(n)]

# INF = 10**18
# dp = [[(1, -INF)]*6 for _ in range(n+1)]
# dp[0][0] = (0, 0)


# def val(ab):
#     a, b = ab
#     if a == b == 0:
#         return 0
#     else:
#         return b/a


# for i in range(1, n+1):
#     a, b = AB[i-1]
#     for j in range(1, 6):
#         if val(dp[i][j]) < val(dp[i-1][j]):
#             dp[i][j] = dp[i-1][j]

#         if j-1 < 0:
#             continue
#         a2, b2 = dp[i-1][j-1]
#         if val(dp[i][j]) < val((a+a2, b+b2)):
#             dp[i][j] = (a+a2, b+b2)


# ans = val(dp[-1][5])
# a, b = dp[-1][4]
# for _ in range(m):
#     c, d = map(int, input().split())
#     if ans < val((a+c, b+d)):
#         ans = val((a+c, b+d))
# print("{:.7f}".format(ans))

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# AB = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     AB.append((b/a, b-a, a, b))
# AB.sort(reverse=True)
# CD = []
# for _ in range(m):
#     c, d = map(int, input().split())
#     CD.append((d/c, d-c, c, d))
# CD.sort(reverse=True)

# # ans = AB[:4]+max(AB[4],CD[0])
# deno = 0
# nume = 0
# for _, _, a, b in AB[:4]:
#     deno += b
#     nume += a
# x, _ = sorted([AB[4], CD[0]], reverse=True)
# deno += x[3]
# nume += x[2]
# print(AB)
# print(CD)
# print(deno, nume)
# print(deno/nume)
