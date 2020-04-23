from collections import Counter
n = int(input())
c = Counter(input())
print(sum(x % 2 for x in c.values()))
