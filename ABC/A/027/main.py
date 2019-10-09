from collections import Counter
*l, = map(int, input().split())
print(*(k for k, v in Counter(l).items() if v % 2))

# 絶対もっと簡単に書けるやろ
# set型にしなくても、対称差集合の演算子使えるらしい
# print(eval(input().replace(' ', '^')))
