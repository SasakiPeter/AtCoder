import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, q = map(int, input().split())
s = input()

# 10**5
# score = [x+y == 'AC' for x, y in zip(s, s[1:])]
score = [0]*n
for i in range(n-1):
    score[i+1] = score[i]
    if s[i:i+2] == 'AC':
        score[i+1] += 1
# print(score)

# 10**5 sumは遅いので使えない
for _ in range(q):
    l, r = map(int, input().split())
    print(score[r-1]-score[l-1])
    # print(s[l-1:r].count('X'))
    # print(sum(score[l-1:r-1]))
