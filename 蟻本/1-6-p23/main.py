l, n = [int(input()) for _ in range(2)]
x = sorted(map(int, input().split()))


# 最短は、近い方の橋に行くまでの時間で計算できる
# L/2のところからの距離/1cm/secって感じ
print(max(min(l-y, y-1) for y in x))
print(max(max(l-y, y-1) for y in x))
