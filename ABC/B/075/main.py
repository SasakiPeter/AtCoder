# h, w = map(int, input().split())
# m = [[0]*(w+2)]
# for _ in range(h):
#     m.append([0]+[0 if s == '.' else s for s in input()]+[0])
# m.append([0]*(w+2))
# around = [(i, j)for i in range(-1, 2) for j in range(-1, 2)]
# for i in range(1, h+1):
#     for j in range(1, w+1):
#         if m[i][j] == '#':
#             for x, y in around:
#                 if m[i+x][j+y] != '#':
#                     m[i+x][j+y] += 1

# for i in range(1, h+1):
#     print(''.join(map(str, m[i]))[1:-1])


# 解答の解法
h, w = map(int, input().split())
s = [input() for _ in range(h)]
for i in range(h):
    tmp = ''
    for j in range(w):
        if s[i][j] == '#':
            tmp += '#'
        else:
            # 単純に、周りにある＃の数をカウントするっていう実装
            # 前後含めた３行を取得
            cnt = 0
            for t in s[max(0, i-1):min(h, i+2)]:
                # 3文字抽出
                cnt += t[max(0, j-1):min(w, j+2)].count('#')
            tmp += str(cnt)
    print(tmp)
