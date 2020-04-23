# 累積和する
from collections import defaultdict
n, W = map(int, input().split())
dd = defaultdict(list)
for i in range(n):
    weight, value = map(int, input().split())
    dd[weight].append(value)

a = min(dd.keys())
b, c, d = a+1, a+2, a+3
Vcum = defaultdict(lambda: [0])
for k in [a, b, c, d]:
    s = 0
    dd[k].sort(reverse=True)
    for val in dd[k]:
        s += val
        Vcum[k].append(s)

ans = 0
for w in range(len(dd[a])+1):
    for x in range(len(dd[b])+1):
        for y in range(len(dd[c])+1):
            if W < a*w+b*x+c*y:
                break
            z = min((W-a*w-b*x-c*y)//d, len(dd[d]))
            val = Vcum[a][w]+Vcum[b][x]+Vcum[c][y]+Vcum[d][z]
            ans = max(ans, val)
print(ans)


# 全探索とか、それを累積和で高速化するのが想定解らしい
# 4種類しか重さが存在しない
# 同じ重さの場合、価値が高いものからバッグに入れた方がいいのは自明
# それぞれの重さごとに、いくつピックするかを決めると、価値が産出できる
# 制約上、１つの重さを最大100回ピックできるので、
# 最大でも5**8にしかならない4*10**5
# 累積和使わなくても行けました！！
# n, W = map(int, input().split())
# dd = defaultdict(list)
# for i in range(n):
#     weight, value = map(int, input().split())
#     dd[weight].append(value)

# for k in dd.keys():
#     dd[k].sort(reverse=True)

# # print(dd)
# a = min(dd.keys())
# b, c, d = a+1, a+2, a+3
# ans = 0
# for w in range(len(dd[a])+1):
#     for x in range(len(dd[b])+1):
#         for y in range(len(dd[c])+1):
#             for z in range(len(dd[d])+1):
#                 # print(w, x, y, z)
#                 if W < a*w+b*x+c*y+d*z:
#                     continue
#                 # print(a, b, c, d, dd)
#                 val = sum(dd[a][:w])+sum(dd[b][:x]) + \
#                     sum(dd[c][:y])+sum(dd[d][:z])
#                 ans = max(ans, val)
# print(ans)

# n, w = map(int, input().split())
# weights, values = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# min_w = min(weights)-1
# weights = [weight-min_w for weight in weights]
# W_MAX = 4*200
# dp = [[0]*(W_MAX+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for k in reversed(range(1, n+1)):
#         for j in range(1, W_MAX+1):
#             if j-weights[i-1] < 0:
#                 continue
#             dp[k][j] = max(dp[k][j], dp[k-1][j-weights[i-1]]+values[i-1])

# # for row in dp:
# #     print(row[:10])

# ans = 0
# # いくつ選んだかによって、wを幾つにすればいいかが変わってくる
# for k in range(n+1):
#     w_max = min(w-k*min_w, W_MAX)
#     if w_max < 0:
#         continue
#     ans = max(ans, dp[k][w_max])
# print(ans)
