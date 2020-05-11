MOD = 998244353
n, m, k = map(int, input().split())

fact = [0]*(n+1)
fact[0] = 1
for i in range(1, n+1):
    fact[i] = fact[i-1]*i % MOD

# # 実は、全部powしなくて大丈夫
# 一番大きい逆元から戻してけばいい　こっちの方が早い
invfact = [0]*(n+1)
invfact[n] = pow(fact[n], MOD-2, MOD)
for i in reversed(range(n)):
    invfact[i] = invfact[i+1]*(i+1) % MOD

# invfact = [0]*(n+1)
# for i in range(n+1):
#     invfact[i] = pow(fact[i], MOD-2, MOD)


def nCr(n, r):
    if r < 0 or n < r:
        return 0
    return fact[n]*invfact[r]*invfact[n-r]


ans = 0
for i in range(k+1):
    ans += m*pow(m-1, n-1-i, MOD)*nCr(n-1, i)
    ans %= MOD
print(ans)
