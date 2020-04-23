# 幅、枚数の組み合わせが50000通り-> 価値の最大値を記録

import numpy as np
W = int(input())
N, K = map(int, input().split())

dp = np.zeros((K+1, W+1), dtype=np.int64)

for _ in range(N):
    a, b = map(int, input().split())
    for k in range(K, 0, -1):
        dp[k, a:] = np.maximum(dp[k, a:], dp[k-1, :-a]+b)
answer = dp.max()
print(answer)
