from itertools import product

k = int(input())
ls = [i for i in range(1, 10)]
digit = 1

while len(ls) < k:
    for i in range(1, 10):
        for j in product([-1, 0, 1], repeat=digit):
            num = str(i)
            skip = 0
            for y in j:
                x = int(num[-1])+y
                if x < 0 or 9 < x:
                    skip = 1
                    break
                num += str(x)
            if skip:
                continue
            ls.append(int(num))

    digit += 1

print(ls[k-1])

# ls = []
# # for i in range(1, 10):
# #     ls.append(i)

# # prev = 1
# # while k < len(ls):
# #     L = max(0, prev-1)
# #     R = max(10, prev+2)
# #     for i in range(L, R):
# #         x = str(prev)+str(i)
# #         ls.append(int(x))
# #     prev += 1

# def dfs(n, s):
#     if n == 0:
#         ls.append(s)
#     else:
#         if
#         for i in range(1, 10):

#             dfs(n-1, s+str(i))


# dfs(2, "")
# print(ls)
