# リストをひっくり返してstackとして使えば、popがO(1)になる
d = {c: list(input())[::-1] for c in 'abc'}
# turn
t = 'a'
while d[t]:
    t = d[t].pop()
print(t.upper())

# a, b, c = [input() for _ in range(3)]


# x = 'a'

# while True:
#     if x == 'a':
#         if a == []:
#             print('A')
#             break
#         x, *a = a
#     elif x == 'b':
#         if b == []:
#             print('B')
#             break
#         x, *b = b
#     elif x == 'c':
#         if c == []:
#             print('C')
#             break
#         x, *c = c

# 辞書型でデータを管理すると、とても便利
# S = {c: list(input()) for c in 'abc'}
# s = 'a'
# while S[s]:
#     # 0番目を削除
#     s = S[s].pop(0)
# print(s.upper())


# 0906　身についてんだかどうなんだか... 上の記述が美しすぎる
# s = {chr(x): list(input())
#      for x, _ in zip(range(ord('a'), ord('c')+1), range(3))}
# f = s['a'].pop(0)
# while s[f] != []:
#     f = s[f].pop(0)

# print(f.upper())
