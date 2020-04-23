n, w = map(int, input().split())
values, weights = zip(*[tuple(map(int, input().split()))for _ in range(n)])

max_value = max(values)
max_weight = max(weights)

if max_weight <= 1000:
    # 価値でやる
    # O(4*10**7)
    UW = 2*10**5
    dp = [0]*(UW+1)

    for i in range(1, n+1):
        for j in reversed(range(1, UW+1)):
            if j-weights[i-1] < 0:
                continue
            dp[j] = max(dp[j], dp[j-weights[i-1]]+values[i-1])
    print(dp[w])
    # dp = [[0]*(UW+1) for _ in range(n+1)]

    # # 貰う
    # for i in range(1, n+1):
    #     for j in range(1, UW+1):
    #         dp[i][j] = dp[i-1][j]
    #         if j-weights[i-1] < 0:
    #             continue
    #         dp[i][j] = max(dp[i][j], dp[i-1][j-weights[i-1]]+values[i-1])

    # print(dp[-1][w])
elif max_value <= 1000:
    # 重みでやる
    # O(4*10**7)
    UV = 2*10**5
    INF = 10**10
    dp = [INF]*(UV+1)
    dp[0] = 0
    for i in range(1, n+1):
        # 逆順で回すと１次元でもうまくいく
        for j in reversed(range(1, UV+1)):
            if j-values[i-1] < 0:
                continue
            dp[j] = min(dp[j], dp[j-values[i-1]]+weights[i-1])

    # dp = [[INF]*(UV+1) for _ in range(n+1)]
    # for i in range(n+1):
    #     dp[i][0] = 0

    # # 貰う
    # for i in range(1, n+1):
    #     for j in range(1, UV+1):
    #         dp[i][j] = dp[i-1][j]
    #         if j-values[i-1] < 0:
    #             continue
    #         dp[i][j] = min(dp[i][j], dp[i-1][j-values[i-1]]+weights[i-1])

    ans = 0
    for j in reversed(range(1, UV+1)):
        if dp[j] <= w:
            ans = j
            break
        # if dp[-1][j] <= w:
        #     ans = j
        #     break
    print(ans)
elif n <= 30:
    import itertools
    import bisect

    vw = [(value, weight)for value, weight in zip(values, weights)]
    A = vw[:n//2]
    B = vw[n//2:]
    # print(A)
    # O(n**15)
    A_ls = []
    for pattern in itertools.product([0, 1], repeat=len(A)):
        tmp_v, tmp_w = 0, 0
        for i in range(len(A)):
            if pattern[i]:
                value, weight = A[i]
                tmp_v += value
                tmp_w += weight
        if w < tmp_w:
            continue
        A_ls.append((tmp_v, tmp_w))
    A_ls.sort(key=lambda x: x[1])

    A_list = []
    max_val = -1
    for value, weight in A_ls:
        if max_val < value:
            max_val = value
            A_list.append((value, weight))
    # print(A_ls)

    B_list = []
    for pattern in itertools.product([0, 1], repeat=len(B)):
        tmp_v, tmp_w = 0, 0
        for i in range(len(B)):
            if pattern[i]:
                value, weight = B[i]
                tmp_v += value
                tmp_w += weight
        if w < tmp_w:
            continue
        B_list.append((tmp_v, tmp_w))

    # A_lsとB_lsをマージ
    # Bから要素を取り出して、Aの中で最も重いものとマッチングさせる
    # wを超えないように注意
    ans = 0
    A_values, A_weights = zip(*A_list)
    for b_value, b_weight in B_list:
        idx = bisect.bisect_right(A_weights, w-b_weight)-1
        ans = max(ans, A_values[idx]+b_value)
    print(ans)
