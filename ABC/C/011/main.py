n = int(input())
# ngs = sorted(int(input()) for _ in range(3))
ngs = [int(input()) for _ in range(3)]
INF = 10**8
dp = [INF]*(n+1)
dp[n] = 0
# 最小手数を記録していく
for i in range(n, 0, -1):
    if i in ngs:
        dp[i] = INF
        continue
    for j in range(1, 4):
        dp[i-j] = min(dp[i]+1, dp[i-j])
        # dp[i-j] = dp[i]+1
# print(dp)
print("YES" if dp[0] <= 100 else "NO")

# # 貪欲
# n = int(input())
# ngs = sorted(int(input()) for _ in range(3))

# ans = False
# if n in ngs:
#     print("NO")
#     exit()
# for i in range(100):
#     n -= 3
#     if n <= 0:
#         ans = True
#         break
#     if n in ngs:
#         n += 1
#         if n in ngs:
#             n += 1
#             if n in ngs:
#                 break
# print("YES" if ans else "NO")

# 連続であるかを判定する
# if n in ngs:
#     print("NO")
# elif all(ng < n for ng in ngs) and ngs[0]+ngs[2] == 2*ngs[1]:
#     print("NO")
# else:
#     if n == 300 and any(ng % 3 == 0 for ng in ngs):
#         print("NO")
#     elif n==299 and
#     else:
#         print("YES")


# dfs全探索 3**100はむり
# def dfs(x, cnt):
#     if cnt == 100:
#         return False
#     if x in ngs:
#         return False
#     if x < 0:
#         return False
#     if x == 0:
#         return True
#     else:
#         ls = []
#         for i in range(4, 1, -1):
#             ls.append(dfs(x-i, cnt+1))
#         return True in ls


# print(dfs(n, 0))
