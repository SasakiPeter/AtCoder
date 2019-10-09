r = int(input())
print('ABC' if r < 1200 else 'ARC' if r < 2800 else 'AGC')

# 16
# print(1 << 4)

# 1/32 つまりx//32となる
# print(32 >> 5)

# これをシフトを用いるとこうなる
# どうして50でわって+8足して2**pを作ったのだろうか？
# print(["ABC", "ARC", "AGC"][r//50+8 >> 5])
