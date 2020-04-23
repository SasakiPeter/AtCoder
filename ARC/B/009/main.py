# from itertools import product
B = list(map(str, input().split()))
n = int(input())
A = [int(input()) for _ in range(n)]
d = {k: str(i) for i, k in enumerate(B)}


# def func(x):
#     # retval = ""
#     # x = str(x)
#     # for k in x:
#     #     retval += d[k]
#     retval = "".join(map(lambda x: d[x], str(x)))
#     # print(list(map(lambda x: d[x], str(x))))
#     return int(retval)


ans = sorted(A, key=lambda x: int("".join(map(lambda y: d[y], str(x)))))
print(*ans, sep='\n')

# ソートするアルゴリズムを学ぶ必要があるのでは？→ない
# ans = []
# rep = len(str(max(A)))
# for b in product(B, repeat=rep):
#     x = int("".join(b))
#     if x in A:
#         ans.append(x)
# print(ans)
