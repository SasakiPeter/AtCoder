# ABC072 B - OddString


# atcoder
s = input()
print(''.join(s_ for i, s_ in enumerate(s) if i % 2 == 0))
print(s[::2])
