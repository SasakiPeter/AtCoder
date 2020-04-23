n, k = map(int, input().split())
MOD = 10**9+7
ans = 0
for i in range(k, n+2):
    ans += (2*n-i+1)*i//2-(i-1)*i//2+1
    ans %= MOD
print(ans % MOD)
