import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

R, G, B = map(int, read().split())


def F(left, x):
    # 中心が0として、leftからx個並べるときのコストをかえす
    right = left+x-1
    if left > 0 and right > 0:
        return (left+right)*x//2
    if left < 0 and right < 0:
        return (-left-right)*x//2
    return sum(x*(x+1)//2 for x in [-left, right])


def min_cost(left, x):
    # 置ける可能な左端が left であるときの最小コスト
    n = x//2
    if left >= -n:
        # 敷き詰めておく
        return F(left, x)
    return F(-n, x)


opt = 10**18
for GL in range(-1000, 1000):
    g = F(GL, G)
    b = min_cost(GL+G-100, B)
    r = min_cost(-99-GL, R)
    opt = min(opt, r+g+b)

print(opt)
