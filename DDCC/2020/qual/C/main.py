h, w, k = map(int, input().split())
cake = [input() for _ in range(h)]
# print(*cake, sep='\n')

# 貪欲に色を塗っていけばええs
cnt = 1
ans = [[0]*w for _ in range(h)]


for i in range(h):
    cnt_berry = 0
    for j in range(w):
        if cake[i][j] == '#':
            cnt_berry += 1
            if 2 <= cnt_berry:
                cnt += 1
        ans[i][j] = cnt
    if cnt_berry != 0:
        cnt += 1
    else:
        for j in range(w):
            ans[i][j] = ans[i-1][j]

cnt = 0
for row in ans:
    if row[0] == 0:
        cnt += 1
        continue
    break
for i in range(cnt-1, -1, -1):
    for j in range(w):
        ans[i][j] = ans[i+1][j]

for row in ans:
    print(*row)
