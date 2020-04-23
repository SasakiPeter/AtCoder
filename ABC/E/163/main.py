# n = int(input())
# A = [(a, i) for i, a in enumerate(map(int, input().split()))]
# A.sort(reverse=True)
# dp = [[0]*(n+1) for _ in range(n+1)]
# ans = 0
# # 配る
# for L in range(n):
#     for R in range(n):
#         if L+R == n:
#             ans = max(ans, dp[L][R])
#             break
#         # 個人的にはもらうの方がここが悩まずかけるからいい
#         a, i = A[L+R]
#         dp[L][R+1] = max(dp[L][R+1], dp[L][R]+abs((n-R-1)-i)*a)
#         dp[L+1][R] = max(dp[L+1][R], dp[L][R]+abs(i-L)*a)
# # for row in dp:
# #     print(row)
# print(ans)

n = int(input())
A = [(a, i) for i, a in enumerate(map(int, input().split()))]
A.sort(reverse=True)
dp = [[0]*(n+1) for _ in range(n+1)]
ans = 0
# もらう
for L in range(n+1):
    for R in range(n+1):
        if n <= L+R-1:
            break
            # continue
        a, i = A[L+R-1]
        if 0 <= R-1:
            dp[L][R] = max(dp[L][R], dp[L][R-1]+abs((n-R)-i)*a)
        if 0 <= L-1:
            dp[L][R] = max(dp[L][R], dp[L-1][R]+abs(i-(L-1))*a)
        ans = max(ans, dp[L][R])
# for row in dp:
#     print(row)
print(ans)
