n = int(input())
v = sorted(map(int, input().split()))

# n種類
# vは価値の集合

# 全探索
# 50 50!

# 価値の低い順に合成する方が良い


cache = 0
for x in v:
    if cache == 0:
        cache = x
    else:
        cache = (cache+x)/2

print(cache)
