n, k = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for L in range(k+1):
    for R in range(k-L+1):
        if n < L+R:
            break
        val = 0
        neg = []
        for i in range(L):
            val += V[i]
            if V[i] < 0:
                neg.append(V[i])
        for i in range(n-1, n-1-R, -1):
            val += V[i]
            if V[i] < 0:
                neg.append(V[i])
        neg.sort()
        val -= sum(neg[:k-L-R])
        if ans < val:
            # print(L, R, V, val, neg, k-L-R)
            ans = val
print(ans)
