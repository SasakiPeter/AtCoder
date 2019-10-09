# from collections import Counter
# c = Counter(input())
# print('Yes' if sum(v % 2 for v in c.values()) == 0 else 'No')

# countを使う場合
# w = input()
# print('Yes' if sum(w.count(c) % 2 for c in w) == 0 else 'No')

# さらにスマートな場合
w = input()
print('Yes' if all(w.count(c) % 2 == 0 for c in set(w)) else 'No')

# こういうときsumじゃなくてall使えるとかっこいい
