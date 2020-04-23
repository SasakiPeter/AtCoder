n = int(input())
C, S, F = [[0]*n for i in range(3)]
for i in range(1, n):
    c, s, f = map(int, input().split())
    C[i], S[i], F[i] = c, s, f
# print(C)

ans = [0]*(n+1)
for i in range(1, n):
    # i番目の駅から出発
    t = S[i]+C[i]
    for j in range(i+1, n):
        # j番目の駅についた時の時刻
        t = S[j]+C[j]+[0, -(-(t-S[j])//F[j])*F[j]][S[j] < t]
    ans[i] = t

print(*(x for x in ans[1:]), sep="\n")


# # sample3のケースが通らない
# dp = [0]*(n+1)
# dp[n-1] = S[n-1]+C[n-1]
# for i in range(n-2, 0, -1):
#     if S[i]+C[i] <= S[i+1]:
#         dp[i] = dp[i+1]
#     else:
#         print(i, dp, S[i]+C[i]-S[i+1])
#         dp[i] = dp[i+1]-(-(S[i]+C[i]-S[i+1])//F[i+1])*F[i+1]

# print(dp)

# for x in dp[1:]:
#     print(x)

# n = int(input())
# dp = [0]*n
# csf = [list(map(int, input().split()))for i in range(n-1)]
# dp[n-2] = csf[n-2][1]+csf[n-2][0]
# for i in range(n-3, -1, -1):
#     if csf[i][1]+csf[i][0] < csf[i+1][1]:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = -(-(csf[i][1]+csf[i][0]-csf[i+1][1]))//csf[i+1][2]+csf[i+1][2]

#     # c,s,f =map(int, input().split())
#     # if dp[i-1] < csf[i-1][1]:
#     #     dp[i] = csf[i-1][1]+csf[i-1][0]
#     # else:
#     #     dp[i] = -(-(dp[i-1]-csf[i-1][1])//csf[i-1][2])*csf[i-1][2]+csf[i-1][1]

# print(dp)
