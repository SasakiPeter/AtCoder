h, w, a, b = map(int, input().split())
s = [[0]*w for _ in range(h)]
# print(s)

for row in s:
    for i in range(a):
        row[i] = 1
# print(s)

# 足りなかったら、countをlenに

# てんち
t = []
for i in range(w):
    col = [s[j][i] for j in range(h)]
    t.append(col)
# print(t, 'trans')
for i in range(w):
    # col == t[i]
    # print(t[i], 'col')
    n_one = t[i].count(1)
    if n_one != b:
        for j in range(n_one - b):
            # 下の２列をずらす
            # print(s, 'h')
            s[-(j+1)][i] = 0
            # print(s, 'e')
            s[-(j+1)][(i+a) % w] = 1
            # print(s, 'l')
            # print(t, 'hc')
            t[i][-(j+1)] = 0
            # print(t, 'ec')
            t[(i+a) % w][-(j+1)] = 1
            # print(t, 'lc', (i+a) % w, -(j+1), a, h)
            # print(s, 'ちな')
# print(s)

# print(t)

no = False
for row in s:
    n_ones = row.count(1)
    n_zeros = w - n_ones
    if min(n_ones, n_zeros) != a:
        no = True
        break

for col in t:
    n_ones = col.count(1)
    n_zeros = h - n_ones
    if min(n_ones, n_zeros) != b:
        no = True
        break


if no or h == w == 1:
    print('No')
else:
    for row in s:
        print(*row, sep="")
