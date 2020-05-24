from collections import deque
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W = map(int, readline().split())
A = b''.join(read().split())
S = A.index(b'S')
G = A.index(b'G')

A = A.replace(b'S', b'0').replace(b'G', b'0')
A = tuple(int(x) - ord('0') for x in A)

INF = 10 ** 9
dist = [INF] * (H * W * 10)
dist[10 * S] = 0
q = deque([10 * S])


def next_n(n):
    x, y = divmod(n, W)
    if 0 < x:
        yield n - W
    if x < H - 1:
        yield n + W
    if 0 < y:
        yield n - 1
    if y < W - 1:
        yield n + 1


while q:
    v = q.popleft()
    n, i = divmod(v, 10)
    for m in next_n(n):
        j = max(i, A[m])
        j = i + 1 if i + 1 == j else i
        w = 10 * m + j
        if dist[w] == INF:
            dist[w] = dist[v] + 1
            q.append(w)

x = dist[10 * G + 9]
if x == INF:
    x = -1
print(x)
