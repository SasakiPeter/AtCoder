# マトリックスの孤立しているかどうかを確かめる
h, w = map(int, input().split())
m = [["."]*(w+2)]
for _ in range(h):
    m.append(["."]+list(input())+["."])
m.append(["."]*(w+2))
# print(m)

# 行列の上下左右に白であるマスを追加してやり、
# 黒のマスが存在する時に、その上下左右のいずれかにも黒が存在しない時に
# フラグを立てれば良い


def canAchive(m):
    for i in range(h):
        for j in range(w):
            around = [m[i-1][j],
                      m[i+1][j],
                      m[i][j-1],
                      m[i][j+1]]
            if m[i][j] == '#' and all(s != "#" for s in around):
                return False
    return True


print('Yes' if canAchive(m) else 'No')
