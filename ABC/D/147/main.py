# # 文字列変換しない場合 pypy
# MOD = 10**9+7
# n = int(input())
# A = list(map(int, input().split()))
# # n_bit = 60
# n_bit = max(A).bit_length()
# bit_cnt = [0]*n_bit
# for i in range(n):
#     for d in range(n_bit):
#         # d桁目を取り出す場合
#         # 一桁目が1か判定するみたいな書き方
#         if (A[i] >> d) & 1:
#             bit_cnt[d] += 1


# ans = 0
# for d, one_cnt in enumerate(bit_cnt):
#     ans = ans + one_cnt*(n-one_cnt)*pow(2, d, MOD) % MOD
# print(ans % MOD)

# binの文字列に変換する場合 pythonでOK
# ある桁jが１のとき、その桁がXORをとって１になるのは
# ０とペアになったとき。逆に０の時は、１とペアになった時
# そこから、その桁2**jのくらいがいくつあるのかが計算できる
# つまり、桁ごとに0と１の数を調べて、それらをかけて、2**jをかけて
# 合計すればいい
MOD = 10**9+7
n = int(input())
A = ['{:060b}'.format(a)[::-1] for a in map(int, input().split())]
# c = [a.count('1') for a in zip(*A)]
# print(sum(c[d]*(n-c[d])*pow(2, d, MOD) %
#           MOD for d in range(60)) % MOD)

A_d = []
for col in zip(*A):
    # 両方数えると遅い
    # c = Counter(map(int, col))
    # A_d.append(c[0]*c[1])
    one_cnt = col.count('1')
    A_d.append(one_cnt*(n-one_cnt))
    # zero_cnt = col.count('0')
    # A_d.append(zero_cnt*(n-zero_cnt))

ans = 0
for d in range(60):
    ans = ans + A_d[d]*pow(2, d, MOD) % MOD
print(ans % MOD)


# # 愚直実装
# ans = 0
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         ans += A[i] ^ A[j]
#         ans %= MOD
# print(ans % MOD)
