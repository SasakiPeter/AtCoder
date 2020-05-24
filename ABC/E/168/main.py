# 既約分数でグループ分けすればいい
from collections import defaultdict
from math import gcd
import sys
input = sys.stdin.readline
MOD = 10**9+7
n = int(input())
cnt = defaultdict(lambda: [0, 0])
zeros = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == b == 0:
        zeros += 1
        continue
    if a < 0 or (a == 0 and b < 0):
        a *= -1
        b *= -1
    g = gcd(a, b)
    a //= g
    b //= g
    if b > 0:
        cnt[(a, b)][0] += 1
    else:
        cnt[(-b, a)][1] += 1
# print(cnt)
ans = 1
for v, v2 in cnt.values():
    # print(v, v2)
    ans *= 1+pow(2, v, MOD)-1+pow(2, v2, MOD)-1
    ans %= MOD
# 1匹も入れないを数えているので引く
ans = (ans+zeros-1) % MOD
print(ans)
