import sys
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 5*10**3 2重ループが認められている
n = int(input())
s = input().rstrip()

# まず、同じ文字がどれくらいあるかを調べる？
c = Counter(s)
print(c)

# valueが1だったら、それは除外
for k, v in c.items():
    if v == 1:
        s = s.replace(k, '_')
print(s)
