# n, k = map(int, input().split())
# A = list(map(int, input().split()))

n, k = 2*10**3, 10**9
A = [1, 3, 5, 3, 3, 5, 3, 3, 5, 4]*(n//10)

S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i]+A[i]

# print(S)
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if (S[j]-S[i]) % k == (j-i):
            ans += 1

print(ans)

# 何言ってんのかわからないけど、式変形すればいいらしい
