n = int(input())
ans = 11
for i in range(1, int(-(-n**.5//1))+1):
    x, r = divmod(n, i)
    if r == 0:
        ans = min(ans, max(map(lambda x: len(str(x)), (i, x))))
print(ans)

# n = int(input())


# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp % i == 0:
#             cnt = 0
#             while temp % i == 0:
#                 cnt += 1s
#                 temp //= i
#             arr.append([i, cnt])

#     if temp != 1:
#         arr.append([temp, 1])

#     if arr == []:
#         arr.append([n, 1])

#     return arr


# fact = factorization(n)
# # print(fact)
# ans = 0
# # 貪欲はダメ
# # a = b = 1
# # for x, cnt in fact[::-1]:
# #     for _ in range(cnt):
# #         if a > b:
# #             a, b = b, a
# #         a *= x
# # print(a, b)

# it = []
# for x, cnt in fact:
#     for _ in range(cnt):
#         it.append(x)
# # print(it)


# def dfs(n, a, b):
#     if n == 0:
#         return max(map(lambda x: len(str(x)), (a, b)))
#     else:
#         x1 = dfs(n-1, a*it[n-1], b)
#         x2 = dfs(n-1, a, b*it[n-1])
#         return min(x1, x2)


# print(dfs(len(it), 1, 1))
