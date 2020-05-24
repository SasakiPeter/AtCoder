# bitDP
n, m = map(int, input().split())
items = []
costs = []
for _ in range(m):
    s, c = input().split()
    tmp = 0
    for i in range(n):
        if s[n-i-1] == 'Y':
            tmp += 1 << i
    items.append(tmp)
    costs.append(int(c))

bit = 1 << n
INF = 10**18
dp = [INF]*bit
dp[0] = 0

for i in range(1, m+1):
    item = items[i-1]
    cost = costs[i-1]
    for j in reversed(range(bit)):
        x = item | j
        y = dp[j]+cost
        if y < dp[x]:
            dp[x] = y
print(dp[-1]if dp[-1] != INF else -1)

# # bitDP
# n, m = map(int, input().split())
# items = []
# costs = []
# for _ in range(m):
#     s, c = input().split()
#     tmp = 0
#     for i in range(n):
#         if s[n-i-1] == 'Y':
#             tmp += 1 << i
#     items.append(tmp)
#     costs.append(int(c))

# bit = 1 << n
# INF = 10**18
# dp = [[INF]*bit for _ in range(m+1)]
# dp[0][0] = 0

# for i in range(1, m+1):
#     item = items[i-1]
#     cost = costs[i-1]
#     for j in range(bit):
#         dp[i][j] = min(dp[i][j], dp[i-1][j])
#         x = item | j
#         dp[i][x] = min(dp[i][x], dp[i-1][j]+cost)
# print(dp[-1][-1]if dp[-1][-1] != INF else -1)
