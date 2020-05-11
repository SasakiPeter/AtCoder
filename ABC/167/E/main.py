MOD = 998244353
n, m, k = map(int, input().split())

memo = [0]*n


def com(n, r):
    if n < r or r < 0:
        return 0
    if n-r < r:
        r = n-r
    if r == 0:
        memo[r] = 1
        return memo[r]
    if memo[r] != 0:
        return memo[r]
    X = Y = 1
    for i in range(1, r+1):
        Y = Y*i % MOD
        X = X*(n-i+1) % MOD
        memo[i] = X*pow(Y, MOD-2, MOD)
    return memo[r]


com(n-1, n//2)

ans = 0
for i in range(k+1):
    ans += com(n-1, i)*m*pow(m-1, n-1-i, MOD)
    ans %= MOD
print(ans)
