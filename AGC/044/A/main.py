from itertools import product
t = int(input())
for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    # nが18乗なのがきつすぎる
    # dp = [0]*(n+1)
    # dp[1] = d
    # for i in range(1, n):
    #     if i*2 <= n:
    #         dp[i*2] = min(dp[i*2], dp[i]+a)
    #     if i*3 <= n:
    #         dp[i*3] = min(dp[i*3], dp[i]+b)
    #     if i*5 <= n:
    #         dp[i*5] = min(dp[i*5], dp[i]+c)
    #     if i+1 <= n:
    #         dp[i+1] = min(dp[i+1], dp[i]+d)
    #     dp[i-1] = min(dp[i-1], dp[i]+d)

    it = [i for i in range(20)]
    INF = 10**18
    ans = INF
    for bit in product(it, repeat=3):
        a_cnt, b_cnt, c_cnt = bit
        for d_cnt in range(1, 100):
            cnt = 0
            cnt += a_cnt*a+b_cnt*b+c_cnt*c+d_cnt*d
            coins = d_cnt*(2*a_cnt)*(3*b_cnt)*(5*c_cnt)
            cnt += abs(n-coins)*d
            if cnt < ans:
                ans = cnt

    print(ans)
