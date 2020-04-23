import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input().rstrip()

S

# wwwwwbbbbbを目指す
# 各地点に対して、左側(exclusive)にあるbを持つ

Lb = [0] * (N+1)
for i, s in enumerate(S, 1):
    Lb[i] = Lb[i-1] + (1 if s == '#' else 0)

answer = N + 100
black = Lb[-1]
for i in range(N+1):
    j = i+1
    # [0,i), [i,N) に分ける
    left = Lb[i]
    right = N - i - (black - Lb[i])
    cost = left + right
    if answer > cost:
        answer = cost

print(answer)
