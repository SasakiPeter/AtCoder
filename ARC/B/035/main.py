from collections import defaultdict
MOD = 10**9+7
n = int(input())
# 早く解けるやつは早く解いたほうがいい
T = []
dd = defaultdict(int)
for _ in range(n):
    t = int(input())
    T.append(t)
    dd[t] += 1
T.sort()
S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i]+T[i]
print(sum(S))
ans = 1
for v in dd.values():
    for i in range(1, v+1):
        ans = ans*i % MOD
print(ans % MOD)
