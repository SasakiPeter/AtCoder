# from tqdm import tqdm
n, x = map(int, input().split())

# A, P = [1], [1]
# for i in range(50):
#     A.append(A[i] * 2 + 3)
#     P.append(P[i] * 2 + 1)


def p(level):
    if level == 0:
        return 1
    return 2*p(level-1)+1


def a(level):
    if level == 0:
        return 1
    return 2*a(level-1)+3


# うまくいく
# def f(N, X):
#     if N == 0:
#         return 0 if X <= 0 else 1
#     elif X <= 1 + a(N-1):
#         return f(N-1, X-1)
#     else:
#         return p(N-1) + 1 + f(N-1, X-2-a(N-1))


# うまくいかない
# def f(level, x):
#     if x == 1:
#         return 0
#     else:
#         if 1 < x <= 1 + A[level-1]:
#             return f(level-1, x-1)
#         else:
#             if x == 2 + A[level-1]:
#                 return 1 + P[level-1]
#             elif 2+A[level-1] < x <= 2 + 2*A[level-1]:
#                 return 1 + P[level-1]+f(level-1, x-2-A[level-1])
#             elif x == 3 + 2*A[level-1]:
#                 return 1 + 2*P[level-1]


# 1 2 どうなる？ BPPPB
# f(0, 1) →　0
def f(level, x):
    # 再帰書く時は、初期条件が妥当か注意する
    if level == 0:
        return 1
    elif x == 1:
        return 0
    # if x == 1:
    #     return 0
    else:
        if 1 < x <= 1 + a(level-1):
            return f(level-1, x-1)
        else:
            if x == 2 + a(level-1):
                return 1 + p(level-1)
            elif 2+a(level-1) < x <= 2 + 2*a(level-1):
                return 1 + p(level-1)+f(level-1, x-2-a(level-1))
            elif x == 3 + 2*a(level-1):
                return 1 + 2*p(level-1)


print(f(n, x))

# for n in range(1, 51):
#     for x in range(1, 100):
#         if x > n:
#             continue
#         if f(n, x) != f_(n, x):
#             print(n, x, f(n, x), f_(n, x))

# print(p(n), a(n))


# def num_p(level):
#     if level == 0:
#         return 1
#     return 2*num_p(level-1)+1


# def num_bp(level):
#     if level == 0:
#         return 1
#     return 2*num_bp(level-1)+3


# def num_b(level):
#     if level == 0:
#         return 0
#     return 2*num_b(level-1)+2


# print(num_p(n), num_b(n))
# print(num_bp(n))
# print(num_bp(n) - x)


# def memoize(f):
#     dd = defaultdict(int)

#     def memoized(*args):
#         if args in dd.keys():
#             return dd[args]
#         else:
#             dd[args] = f(*args)
#             return dd[args]

#     return memoized

# 一応、全部シミュレーションしてみる
# まぁ、重いよね


# @memoize
# def dp(level):
#     if level == 0:
#         return "P"
#     return "B" + dp(level-1) + "P" + dp(level-1) + "B"


# print(dp(n)[-x:].count("P"))
