# n = int(input())
# r = input()
# print((r.count('A')*4+r.count('B')*3+r.count('C')*2+r.count('D'))/n)

# IQ200戦略
# インデックスとスコアを対応させる
score = 'FDCBA'
n = int(input())
print(sum(score.index(r) for r in input())/n)

# map戦略　これもなかなかすごい
# n = int(input())
# print(sum(map(int, input().translate(str.maketrans('FDCBA', '01234'))))/n)

# 文字列を置換するのに、１つならreplaceを使うが、複数の時は
# .translate(str.maketrans('hoge', 'fuga'))が使える
