# s = input()
# for x in range(ord('a'), ord('z')+1):
#     if chr(x) not in s:
#         print(chr(x))
#         break
# else:
#     print('None')


# minの中にor入れるとどうなるの？
# minの中にorが入っていても、orは左が偽なら右を返し、左が真なら左を返すだけの
# 演算子なので、set()ならmin(['None'])で、それ以外ならmin({'a'})みたいな感じで
# 評価される
# print(min(set(map(chr, range(97, 123))) - set(input()) or ['None']))

# for elseはそれはそれで綺麗だと思うけど、セット使って集合として計算する方が
# スマート

# この問題、本当に色々な書き方があって面白い
# 排他的論理和って、どちらかの集合にしかないものを抽出するけど、
# 内包関係にある場合は、-と同じになる
# print(set(map(chr, range(97, 123))) ^ set(input()))
# print(min(set(map(chr, range(97, 123))) ^ set(input()) or ['None']))

# 923 min使うの難しいよね うーんこのって感じの実装
s = input()
# print(min([chr(c)
#            for c in range(ord('a'), ord('z')+1)if chr(c) not in s] or ['None']))

# せめてこうやろ
print(min([c for c in map(chr, range(ord('a'), ord('z')+1))if c not in s] or ['None']))
# それで、最終的にfor使わないでsetで演算するのがスマート
