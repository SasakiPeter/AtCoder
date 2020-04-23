from collections import Counter
n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]

# dfsで解くときには、引数にどの情報を持たせたら良いかが鍵になってくると思う。
# その発想を手助けするのが、今回は、それぞれの竹について、使わないか、Aの素材か
# Bの素材か、Cの素材にするかということ。
INF = 10**8


def dfs(current_index, sum_a, sum_b, sum_c):
    # 全部の竹を見終わった時
    if current_index == n:
        if min(sum_a, sum_b, sum_c) > 0:
            return sum(abs(x-y) for x, y in
                       zip([a, b, c], [sum_a, sum_b, sum_c]))-30
        else:
            return INF
    # n番目の竹を使わなかった時、Aの素材にした時、Bの素材にした時、Cの素材にした時
    # それぞれ計算した中で、最もコストが低いのを返す
    cost_none = dfs(current_index+1, sum_a, sum_b, sum_c)
    cost_a = dfs(current_index+1, sum_a+L[current_index], sum_b, sum_c)+10
    cost_b = dfs(current_index+1, sum_a, sum_b+L[current_index], sum_c)+10
    cost_c = dfs(current_index+1, sum_a, sum_b, sum_c+L[current_index])+10
    return min(cost_none, cost_a, cost_b, cost_c)


# 一本目の竹から、どう使うかみていく
print(dfs(0, 0, 0, 0))

# 考えが浅い
# def dfs(n, L, cost):
#     if n == 3:
#         print(abs(sum([a, b, c])-sum(L))+cost)
#     else:
#         for i in range(len(L)):
#             for j in range(i+1, len(L)):
#                 ls = [L[i]+L[j]]+L[:i]
#                 ls += L[i+1:j]+L[j+1:]
#                 dfs(n-1, ls, cost+10)


# dfs(n, L, 0)


# どれとどれを合成するか考えるよりも、Aの素材となるか、Bの素材となるか、Cの素材となるか
# 使わないかで考えた方が良い

# def base_n(x, n, zero_padding=8):
#     retval = [[], ['0']][x == 0]
#     while x > 0:
#         x, r = divmod(x, n)
#         retval.append(str(r))
#     cnt = zero_padding - len(retval)
#     pad = ['', '0'*cnt][cnt > 0]
#     return pad+''.join(retval[::-1])


# # print(4**8)
# ans = 10**8
# for i in range(4**n):
#     base_4 = base_n(i, 4, n)
#     n_bamboo = n - base_4.count("0")
#     if n_bamboo < 3 or any(k not in base_4 for k in "123"):
#         continue
#     ctr = Counter(base_4)

#     cost = 0
#     for x, y in zip([a, b, c], "123"):
#         cost += abs(x - sum(L[idx]for idx, v in enumerate(base_4)
#                             if v == y))+(ctr[y]-1)*10
#     if ans > cost:
#         ans = cost
# print(ans)


# L本の中から、どれを使うかを全て洗い出して、その時のコストを計算すれば最適にたどり着ける
# というわけでもなかった↓ボツ
# if n == 3:
#     print(abs(sum([a, b, c])-sum(L)))
# INF = 10**8
# ans = INF
# for i in range(2**n):
#     base_2 = base_n(i, 2, n)
#     n_bamboo = base_2.count("1")
#     if n_bamboo < 3:
#         continue

#     s = sum(L[idx] for idx, bl in enumerate(base_2) if bl)
#     x = abs(sum([a, b, c]) - s) + 10*(n - n_bamboo)
#     if ans > x:
#         print(base_2, s, n_bamboo, abs(sum([a, b, c]) - s))
#         ans = x
# print(ans)
