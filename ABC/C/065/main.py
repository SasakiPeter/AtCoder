n, m = map(int, input().split())
MOD = 10**9+7

# 階乗の計算
if abs(n-m) > 1:
    print(0)
else:

    # nとmは同じか、最大でも1しか違わないので、両方とも階乗を計算する必要はない
    nf, mf = 1, 1
    for i in range(1, min(n, m)+1):
        nf = (nf*i) % MOD

    if n != m:
        mf = max(n, m) * nf
    else:
        mf = nf

    # nf = 1
    # for i in range(1, n+1):
    #     nf = (nf * i) % MOD
    #     # nf *= i
    #     # nf %= MOD

    # mf = 1
    # for i in range(1, m+1):
    #     mf = (mf * i) % MOD
    #     # mf *= i
    #     # mf %= MOD

    if n == m:
        print(nf * mf * 2 % MOD)
    else:
        print(nf * mf % MOD)
