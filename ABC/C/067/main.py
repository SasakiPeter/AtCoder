n = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
INF = 10**18
ans = INF
X = 0
for a in A[:-1]:
    X += a
    ans = min(ans, abs(2*X-sum_A))
print(ans)

# n = int(input())
# A = list(map(int, input().split()))
# S = [0]*(n+1)
# for i in range(n):
#     S[i+1] = S[i]+A[i]
# INF = 10**18
# ans = INF
# for R in range(1, n):
#     ans = min(ans, abs((S[R]-S[0])-(S[n]-S[R])))
# print(ans)
