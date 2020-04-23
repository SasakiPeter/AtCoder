n, k = map(int, input().split())
h = list(map(int, input().split()))
# この間のwaterとかsugerに値をぶち込むときと同じ発想
# dijkstraとかbellmanfordもこの配るDPやな
INF = float('inf')
dp = [INF]*n
dp[0] = 0

for i in range(n):
    for j in range(1, k+1):
        # print(i, j, dp)
        if n <= i+j:
            continue
        dp[i+j] = min(dp[i+j], dp[i]+abs(h[i+j]-h[i]))
# print(dp)
print(dp[-1])

# こういうとき、もらうDPよりも配るDPで実装した方が、
# 初期の遷移を追わなくて楽
# # pypyで出す
# n, k = map(int, input().split())
# h = list(map(int, input().split()))
# dp = [0]*n
# dp[1] = abs(h[1]-h[0])
# for i in range(2, n):
#     # if i < k:
#     #     dp[i] = min(dp[i-j]+abs(h[i]-h[i-j])for j in range(1, i+1))
#     # else:
#     #     dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]) for j in range(1, k+1))
#     dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]) for j in range(1, min(i, k)+1))
# print(dp[-1])
# # print(dp)
