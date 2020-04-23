n, s = map(int, input().split())
A = list(map(int, input().split()))


def f(ls):
    S = [0]*(len(ls)+1)
    for i in range(len(ls)):
        S[i+1] = S[i]+ls[i]
    cnt = 0
    # 尺取
    idx = 0
    # print(S)
    for i in range(len(ls)):
        # print(i+1, idx)
        # いや、この辺よくわかんね
        while i+1 != idx:
            if S[i+1]-S[idx] != s:
                cnt += 1
                idx += 1
                break
            idx += 1

    return cnt


for L in range(n):
    for R in range(L+1, n+1):
        print(A[L:R])
        print(f(A[L:R]))
