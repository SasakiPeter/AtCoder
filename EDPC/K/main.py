n, k = map(int, input().split())
A = list(map(int, input().split()))
# dp[i] i個の石で手番の時の勝ち負け
dp = [0]*(k+1)
# 貰う
for i in range(1, k+1):
    for j in range(n):
        if i-A[j] < 0:
            continue
        # dp[i] = max(dp[i], 1 if dp[i-A[j]] == 0 else 0)
        # bit演算の方が楽
        # dp[i] |= 1 if dp[i-A[j]] == 0 else 0
        dp[i] |= not dp[i-A[j]]
# print(dp)
print('First' if dp[k] else 'Second')
