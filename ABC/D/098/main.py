# 尺取
n = int(input())
A = list(map(int, input().split()))
ans = R = X = 0
for L in range(n):
    # 次のやつ足したら、もうダメかどうかが、ここに含まれている
    # &は一桁でも11があったらダメってこと
    while R < n and not(X & A[R]):
        X ^= A[R]
        R += 1
    ans += R-L
    X ^= A[L]
print(ans)

# # 尺取　pypyじゃないと通らない程度には重い
# n = int(input())
# A = [list(map(int, list('{:020b}'.format(a))))
#      for a in map(int, input().split())]

# ans = 0
# R = 0
# X = [0]*20
# for L in range(n):
#     # print(X, L, R)
#     # 尺取無限にバグらせてて辛い
#     # Rによって、どこまで足していくかを決める
#     # 0<=R<=n-1
#     # 次に見るべきは2の時、すぐに足して、試してみちゃう
#     # ので、Rは常に行き過ぎのところに設定される
#     # 条件に合致しなかったら、そもそもwhile回さないのがみそ
#     while R < n and all(x+y != 2 for x, y in zip(X, A[R])):
#         for i in range(20):
#             X[i] += A[R][i]
#         R += 1
#         # print(R, X)
#     # print(L, R, X)
#     ans += R-L
#     # Lは次のために今使ったAを削除するために参照する
#     for i in range(20):
#         X[i] -= A[L][i]
# print(ans)


# # S = [0]*(n+1)
# cnt = n
# for i in range(n-1):
#     for j in range(i+1, n):
#         # 桁ごとに足算して、２以上が現れたらだめ
#         for x in zip(*A[i:j+1]):
#             if 1 < sum(map(int, x)):
#                 break
#         else:
#             cnt += 1

# print(cnt)
