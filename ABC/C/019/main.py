n = int(input())
A = list(map(int, input().split()))
# ２で割り切れるなら、わる
# 間に合わないかも
s = set()
for a in A:
    # ２で割り切れるかはbit演算で現せる
    # while a % 2 == 0:
    while not(a & 1):
        a //= 2
    s |= {a}
print(len(s))
