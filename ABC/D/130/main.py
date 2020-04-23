# わからん！とりあえず実装
n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i]+A[i]

idx_cnt = 0
ans = 0
for i in range(n):
    while S[i+1]-S[idx_cnt] >= k:
        idx_cnt += 1
    ans += idx_cnt

print(ans)

# ans = 0
# for i in range(n):
#     for j in range(i, n+1):
#         if S[j]-S[i] >= k:
#             ans += 1
# print(A)
# print(S)
# print(ans)
