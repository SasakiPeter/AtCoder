MOD = 998244353
n, a, b, k = map(int, input().split())
# n, a, b, k = 3*10**5, 1, 2, 18*10**18


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


# def lcm(a, b):
#     return (a*b)//gcd(a, b)


# print(gcd(a, b))


# a,bが0以上なので、取りうる最小のkはLCMになる
# いや、違う　片方0でもいいから
# print(lcm(a, b))

# ax+by=kの一次不定方程式を解くところまでは考察できてた
# xを全探索していいとは気づかなかった
# n>=max(x,y)だから、xはn以下で全探索できる


pair = []
for x in range(n+1):
    y, r = divmod(k-a*x, b)
    if y < 0:
        continue
    if r == 0:
        pair.append((x, y))

# print(pair)

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


com(n, n//2)

ans = 0
for x, y in pair:
    ans += com(n, x)*com(n, y) % MOD
print(ans % MOD)
