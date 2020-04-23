L, X, Y, S, D = map(int, input().split())
INF = 10**9+1
a = b = INF

if S < D:
    clockwise_dist = D-S
    counterclockwise_dist = S+L-D
else:
    clockwise_dist = D+L-S
    counterclockwise_dist = S-D

a = clockwise_dist/(X+Y)
if X-Y < 0:
    b = counterclockwise_dist/(Y-X)

print("{:.10f}".format(min(a, b)))
