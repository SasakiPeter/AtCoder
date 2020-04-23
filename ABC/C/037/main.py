# 部分和を予め求めておく方法　脳筋でできる
n, k = map(int, input().split())
A = list(map(int, input().split()))

S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i]+A[i]

ans = 0
for i in range(n-k+1):
    L, R = i, i+k
    ans += S[R]-S[L]
print(ans)

# 係数計算して求める方法　場合わけがめんどい
# n, k = map(int, input().split())
# A = list(map(int, input().split()))

# if 2*k-1 <= n:
#     x = [i for i in range(1, k)]
#     coef = x+[k]*(n-2*k+2)+x[::-1]
# else:
#     max = n-k+1
#     x = [i for i in range(1, max+1)]+[max]*(n//2-max)
#     # cnt = n//2-len(x)
#     # x += [max]*cnt
#     # if n % 2 == 0:
#     #     coef = x+x[::-1]
#     # else:
#     #     coef = x+[max]+x[::-1]
#     coef = x+[[], [max]][n % 2]+x[::-1]

# # print(coef)
# print(sum(x*y for x, y in zip(coef, A)))
# # ans = 0
# # for x, y in zip(coef, A):
# #     ans += x*y
# # print(ans)
