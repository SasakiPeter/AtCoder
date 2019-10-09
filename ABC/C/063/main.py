# ~100
n = int(input())
# ~100
s = sorted(int(input()) for _ in range(n))
mask = list(map(lambda x: x % 10 != 0, s))
print([sum(s), sum(s)-s[mask.index(True)]
       if True in mask else 0][sum(s) % 10 == 0])

# 全部足したやつから、小さい順に引けばいいけど、
# 一個引くのと、２子以上引くのでは、ちょっと面倒な感じ


# 問題の取り方が2通りだから2**nの計算量
# 全探索は無理

# 枝を刈ればいけそうな気もしなくもない

# s = [10, 10, 15]
# iまでの数の中での最大値を考える
# dp[i] = [dp[i-1], dp[i-1] + s[i]][(dp[i-1] + s[i]) % 10 == 0]


# def solve(i):
#     if i == 0:
#         return dp(i) = 0
#     return [dp(i-1), dp(i-1) + s[i]][(dp(i-1) + s[i]) % 10 == 0]
# return [dp[i-1], dp[i-1] + s[i]][(dp[i-1] + s[i]) % 10 == 0]


# dp = [0]*n


# def solve(i):
#     if i == 0:
#         if s[i] % 10 == 0:
#             dp[i] = 0
#         else:
#             dp[i] = s[i]
#         return dp[i]
#     print(i, dp, s)
#     if (dp[i-1] + s[i]) % 10 == 0:
#         dp[i] = dp[i-1] + s[i]
#     else:
#         dp[i] = solve(i-1)
#     return dp[i]


# print(solve(n-1))
# max(sum(s), dp[])
