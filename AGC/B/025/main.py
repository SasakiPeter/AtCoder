MOD = 998244353
n, a, b, k = map(int, input().split())
memo = [0]*(n//2+1)


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


com(n, n//2)
ans = 0
for x in range(n+1):
    y, r = divmod(k-a*x, b)
    if y < 0:
        continue
    if r == 0:
        ans += com(n, x)*com(n, y)
        ans %= MOD
print(ans % MOD)
