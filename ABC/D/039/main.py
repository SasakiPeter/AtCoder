# スライムの時のような失敗はしない！
# 貪欲に処理すれば行けそう
h, w = map(int, input().split())
IMAGE = [list(input())for _ in range(h)]
reconstructed_img = [['']*w for _ in range(h)]

dirc = [
    (0, 0),
    (-1, 0), (0, 1), (1, 0), (0, -1),
    (-1, 1), (1, 1), (1, -1), (-1, -1)
]

for i in range(h):
    for j in range(w):
        # 自分を含めた四方八方全てが#なら
        is_black = 0
        for x, y in dirc:
            di, dj = i+x, j+y
            if di < 0 or h <= di or dj < 0 or w <= dj:
                continue
            if IMAGE[di][dj] != '#':
                break
        else:
            is_black = 1

        if is_black:
            reconstructed_img[i][j] = '#'
        else:
            reconstructed_img[i][j] = '.'

# 検証 reconの通りに削除していって、#残ってないならOK
# 必要十分をうまく満たせているはず
for i in range(h):
    for j in range(w):
        if reconstructed_img[i][j] == '#':
            for x, y in dirc:
                di, dj = i+x, j+y
                if di < 0 or h <= di or dj < 0 or w <= dj:
                    continue
                IMAGE[di][dj] = '.'

if any('#' in row for row in IMAGE):
    print('impossible')
else:
    print('possible')
    for row in reconstructed_img:
        print(''.join(row))
