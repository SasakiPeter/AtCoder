can_change = '@atcoder'

s = input()
t = input()
win = True
for x, y in zip(s, t):
    if x == y:
        continue
    # これは上で書いた方が早い
    # if x != y:
    if x == '@' and y in can_change:
        continue
    if y == '@' and x in can_change:
        continue
    win = False
    break


print('You can win' if win else 'You will lose')


# maspy
# S = input()
# T = input()

# bl = True

# atcoder = set('atcoder@')

# for s, t in zip(S, T):
#     # 同じなら弾く処理を入れた方が早い
#     if s == t:
#         continue
#     # 必ずsが'@'なら、いろいろ考えなくていい
#     if t == '@':
#         s, t = t, s
#     if s != '@':
#         bl = False
#         break
#     if t not in atcoder:
#         bl = False
#         break


# answer = 'You can win' if bl else 'You will lose'
# print(answer)
