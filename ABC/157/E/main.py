n = int(input())
s = list(input())
q = int(input())

INF = (1 << 31) - 1
SEG_LEN = 1 << 17
SEG = [INF]*(SEG_LEN*2)


def update(i, x):
    i += SEG_LEN
    SEG[i] = x
    while i > 0:
        i //= 2
        SEG[i] = min(SEG[i*2], SEG[i*2+1])


def find(left, right):
    left += SEG_LEN
    right += SEG_LEN
    ans = INF
    while left < right:
        if left % 2 == 1:
            ans = min(SEG[left], ans)
            left += 1
        left //= 2
        if right % 2 == 1:
            ans = min(SEG[right-1], ans)
            right -= 1
        right //= 2
    return ans


for _ in range(q):
    cmd, x, y = input().split()
    if cmd == '1':
        update(int(x)-1, y)
    else:
        print(find(int(x)-1, int(y)))
        # print(len(set(s[int(x)-1:int(y)])))
