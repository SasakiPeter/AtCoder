from collections import defaultdict
n, s = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i]+A[i]

cnt = defaultdict(int)
for L in range(n):
    for R in range(i+1, n+1):
        if S[R]-S[L] == s:
            cnt[R-L] += 1
print(cnt)
