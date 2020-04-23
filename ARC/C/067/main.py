from collections import defaultdict
n = int(input())
MOD = 10**9+7


def factorization(n):
    retval = []
    tmp = n
    for i in range(2, int(-(-n**.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            retval.append((i, cnt))
    if tmp != 1:
        retval.append((tmp, 1))
    if not retval:
        retval.append((n, 1))
    return retval


# f = 1
# for i in range(1, n+1):
#     f *= i
d = defaultdict(int)
for i in range(1, n+1):
    f = factorization(i)
    for k, v in f:
        d[k] += v

ans = 1

for k, v in d.items():
    if k == 1:
        continue
    ans = ans*(v+1) % MOD

print(ans)
