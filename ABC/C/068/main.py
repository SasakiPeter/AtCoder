# 10**5
n, m = map(int, input().split())
s = {tuple(map(int, input().split())) for _ in range(m)}

# とりあえずの洗い出し実装
# ２個取り出すということは、
# 最初は1、最後はn 中央がn以下の数以外しかないので、
# それを洗い出せばいい

for i in range(2, n):
    route = [1, i, n]
    if all(edge in s for edge in zip(route, route[1:])):
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')

# このあいだのgraphの問題が生きた


# 1中継地でゴールまで行かないといけない問題なので、
# 中継地を抑えれば解ける

# n, m = map(int, input().split())
# transit_a = set()
# transit_b = set()
# for _ in range(m):
#     a, b = map(int, input().split())
#     if a == 1:
#         transit_b.add(b)
#     elif b == n:
#         transit_a.add(a)

# print('POSSIBLE' if len(transit_a & transit_b) else 'IMPOSSIBLE')
