# 包除原理をうまく使う
# 計算がめんどそうなものは、簡単なものの組み合わせで求める
n, k = map(int, input().split())
MOD = 10**9+7
d = [0]*(k+1)
for i in range(1, k+1):
    d[i] = pow(k//i, n, MOD)

for i in reversed(range(1, k+1)):
    for j in range(2*i, k+1, i):
        d[i] -= d[j]
        d[i] %= MOD

ans = 0
for i in range(1, k+1):
    ans += i*d[i] % MOD
print(ans % MOD)
