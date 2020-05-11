from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
S = [input().rstrip()for _ in range(n)]
# print(S)
ans = 0
for ss in permutations(S, n):
    point = 0
    s = "".join(ss)
    for c in s:
        if c == '(':
            point += 1
        elif c == ')':
            point -= 1
            if point < 0:
                break
    else:
        if point == 0:
            ans = 1
print('Yes' if ans else 'No')
