# n = int(input())

# BTC_EXCHANGE_RATE = 380000

# money = 0
# for _ in range(n):
#     x, u = input().split()
#     x = float(x)
#     money += [x, x*BTC_EXCHANGE_RATE][u == 'BTC']

# print(money)

# 923 まじ頭いい
n = int(input())
XU = [input().split() for _ in range(n)]
print(sum(float(x)*{'JPY': 1, 'BTC': 380000}[u] for x, u in XU))

# rateを辞書で管理するのすごい 思いつかなかった
