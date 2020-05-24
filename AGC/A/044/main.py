# もらうDPをメモ化再帰にしました的な実装
t = int(input())
for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    memo = {0: 0, 1: d}
    # cnt = 0

    def dfs(n):
        # global cnt
        # cnt += 1
        if n in memo.keys():
            return memo[n]

        res1 = n*d
        r = n % 2
        res2 = a+r*d+dfs((n-r)//2)
        if r != 0:
            tmp = a+(2-r)*d+dfs((n+(2-r))//2)
            if tmp < res2:
                res2 = tmp

        r = n % 3
        res3 = b+r*d+dfs((n-r)//3)
        if r != 0:
            tmp = b+(3-r)*d+dfs((n+(3-r))//3)
            if tmp < res3:
                res3 = tmp

        r = n % 5
        res5 = c+r*d+dfs((n-r)//5)
        if r != 0:
            tmp = c+(5-r)*d+dfs((n+(5-r))//5)
            if tmp < res5:
                res5 = tmp

        memo[n] = min(res1, res2, res3, res5)
        return memo[n]

    print(dfs(n))
    # print(cnt)


# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10**7)
# INF = 10**18
# t = int(input())
# for _ in range(t):
#     n, a, b, c, d = map(int, input().split())
#     memo = defaultdict(lambda: INF)
#     # cnt = 0

#     def dfs(n, cost):
#         # global cnt
#         # cnt += 1
#         if memo[n] <= cost:
#             return 0

#         memo[n] = cost
#         if n == 0:
#             return 0
#         # 2で割るとき
#         # nを2の倍数にしてから遷移

#         dfs(0, cost+n*d)

#         r = n % 2
#         dfs((n-r)//2, cost+a+r*d)
#         if r != 0:
#             dfs((n+(2-r))//2, cost+a+(2-r)*d)

#         r = n % 3
#         dfs((n-r)//3, cost+b+r*d)
#         if r != 0:
#             dfs((n+(3-r))//3, cost+b+(3-r)*d)

#         r = n % 5
#         dfs((n-r)//5, cost+c+r*d)
#         if r != 0:
#             dfs((n+(5-r))//5, cost+c+(5-r)*d)
#     # print(dfs(n, 0))
#     # print(mincost)
#     # print(costs)
#     dfs(n, 0)
#     # print(memo)
#     print(memo[0])
#     # print(cnt)
