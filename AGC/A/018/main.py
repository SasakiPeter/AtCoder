from functools import reduce
# 想定解
# 最大公約数を使う
# diffを求めるのと、gcdを求めるのは同じことっぽい
# それは、ユークリッドの互除法から明らか
n, k = map(int, input().split())
A = sorted(map(int, input().split()))

# 生成できる一番小さいボール=Aの最大公約数
# もっとも大きい数をそのボールで割ったあまりが0ならpossible


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# def gcd(a, b):
#     if a < b:
#         a, b = b, a
#     if a == b:
#         return a
#     # 本当は%にする
#     return gcd(b, a-b)


# ここ、reduce使うと簡単にかける
# smallest_ball = A[0]
# for a in A[1:]:
#     smallest_ball = gcd(smallest_ball, a)

# gcd_A
smallest_ball = reduce(gcd, A)

# 別にこれも、ユークリッドの互除法から、k%gcd_A==0で十分
print("POSSIBLE" if (A[-1]-k) %
      smallest_ball == 0 and k <= A[-1] else "IMPOSSIBLE")

# # 圧倒的別解だった模様←ACだが反例が作れてしまうので実質WA
# # 最大の数以下のkで1が作れるならPossible確定

# n, k = map(int, input().split())
# A = sorted(map(int, input().split()))
# INF = 10**9+1
# # もっとも差が小さいボールを探す
# # ただし、0になるのは困る
# diff = INF
# for x, y in zip(A, A[1:]):
#     z = abs(x-y)
#     if z > 0:
#         diff = min(diff, z)

# MAX = A[-1]
# ans = False
# for a in A:
#     if a-k < 0:
#         continue
#     x, r = divmod((a-k), diff)
#     # 割り切れたら、possible
#     if r == 0:
#         ans = True
#         break
# print("POSSIBLE" if ans else "IMPOSSIBLE")
