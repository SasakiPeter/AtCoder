# ABC018 A - 豆まき
l = [int(input()) for _ in range(3)]
l_ = sorted(l)[::-1]
for x in l:
    print(l_.index(x)+1)
