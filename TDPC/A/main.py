# setDP
n = int(input())
p = list(map(int, input().split()))
s = {0}
for point in p:
    s |= {x+point for x in s}
print(len(s))


# # 空間計算量削減
# n = int(input())
# p = sorted(map(int, input().split()))
# PMAX = sum(p)
# dp = [0]*(PMAX+1)
# dp[0] = 1
# for i in range(1, n+1):
#     for j in reversed(range(PMAX+1)):
#         if j-p[i-1] < 0:
#             continue
#         dp[j] = max(dp[j], dp[j-p[i-1]])
# print(sum(dp))

# n = int(input())
# p = sorted(map(int, input().split()))
# PMAX = sum(p)
# dp = [[0]*(PMAX+1) for _ in range(n+1)]
# dp[0][0] = 1
# for i in range(1, n+1):
#     for j in range(PMAX+1):
#         dp[i][j] = max(dp[i][j], dp[i-1][j])
#         if j-p[i-1] < 0:
#             continue
#         dp[i][j] = max(dp[i][j], dp[i-1][j-p[i-1]])
# print(sum(dp[-1]))
