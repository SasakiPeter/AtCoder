from collections import Counter
n = int(input())
s = input()
colors = ('R', 'G', 'Y')
c = Counter(s)
*xy, z = sorted(c[color] for color in colors)
if sum(xy)+1 < z:
    print(-1)
    exit()
