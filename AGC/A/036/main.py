# √sの空間に、押し込む問題
# ベクトルの成分表記から面積を求める公式を使って、式変形する
# 1/2 * abs(x1*y2 - x2*y1)

s = int(input())
MOD = 10**9
# y2, x2 = divmod(s, MOD)
# if y2+1 <= MOD:
#     x2 = abs(x2-MOD)
#     y2 += 1

x = (-s) % MOD
y = (s+x)//MOD

print(0, 0, 10**9, 1, x, y)

print(abs(10**9*y - x), s)

assert abs(10**9*y - x) == s
