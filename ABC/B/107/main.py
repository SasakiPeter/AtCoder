# # 判定してから、除去
# h, w = map(int, input().split())
# m = [list(input()) for _ in range(h)]

# # 行に全部.があるか判定して、該当する行iを出力
# row_idx = []
# for idx, row in enumerate(m):
#     if not row.count('#'):
#         row_idx.append(idx)

# col_idx = []
# for idx, col in enumerate(zip(*m)):
#     if not col.count('#'):
#         col_idx.append(idx)

# for i, row in enumerate(m):
#     if i in row_idx:
#         continue
#     else:
#         for idx in col_idx[::-1]:
#             row.pop(idx)
#         print(*row, sep='')

# 判定してからじゃないとダメって、思ったけど、そんなことない
h, w = map(int, input().split())
m = [list(input()) for _ in range(h)]
mr = [r for r in m if '#' in r]
mrc = [c for c in zip(*mr) if '#' in c]
print(*(''.join(row) for row in zip(*mrc)), sep='\n')
