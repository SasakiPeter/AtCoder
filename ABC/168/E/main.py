class P:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, q):
        return P(self.x-q.x, self.y-q.y)

    def __mul__(self, q):
        return P(self.x*q.x, self.y*q.y)

    def __str__(self):
        return "{},{}".format(self.x, self.y)

    def sum(self):
        return self.x+self.y


MOD = 10**9+7
n = int(input())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append(P(a, b))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (AB[i]*AB[j]).sum() == 0:
            print(i, j)


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


com(n-3, n//2)

ans = n
for i in range(2, n+1):
    # ans += nCr(n, i)
    ans += com(n-3, i)*(2**3)
print(ans % MOD)
