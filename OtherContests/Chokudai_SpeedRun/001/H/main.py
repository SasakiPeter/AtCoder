# LIS
import bisect
n = int(input())
A = list(map(int, input().split()))

# 最長部分列？を作るには、２つ方法がある
# １つはO(N**2)のdp
# 正直、こっちが実装できる能力の方が大事な気がする
# dp = [0]*n
# for i in range(n):
#     dp[i] = 1
#     for j in range(n):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(dp)


# いつもやるやつは、O(NlogN)を使う
INF = 10**18
dp = [INF]*n
for i in range(n):
    # dpテーブルのもっとも値が小さいところを書き換える
    # 最終的にできた配列の長さが答え
    dp[bisect.bisect_left(dp, A[i])] = A[i]
print(bisect.bisect_left(dp, INF))
