n = int(input())
a = input()
b = input()
MOD = 1000000007

ans = 3 * ((a[0] != b[0])+1)
tate = a[0] == b[0]
skip = a[0] != b[0]
for x, y in zip(a[1:], b[1:]):
    if skip:
        skip = 0
        continue
    if x == y:
        now_tate = 1
    else:
        now_tate = 0
        skip = 1

    if tate:
        ans *= 2
    else:
        if now_tate:
            ans *= 1
        else:
            ans *= 3
    tate = now_tate
    ans = ans % MOD
print(ans % MOD)


# n = int(input())
# a = input()
# b = input()
# MOD = 1000000007

# ans = 1
# if a[0] == b[0]:
#     ans *= 3
#     tate = 1
#     skip = 0
#     for x, y in zip(a[1:], b[1:]):
#         if skip:
#             skip = 0
#             continue
#         if x == y:
#             now_tate = 1
#         else:
#             now_tate = 0
#             skip = 1

#         if tate:
#             ans *= 2
#         else:
#             if now_tate:
#                 ans *= 1
#             else:
#                 ans *= 3
#         tate = now_tate
#         ans = ans % MOD
# else:
#     ans *= 6
#     tate = 0
#     skip = 0
#     for x, y in zip(a[2:], b[2:]):
#         if skip:
#             skip = 0
#             continue
#         if x == y:
#             now_tate = 1
#         else:
#             now_tate = 0
#             skip = 1

#         if tate:
#             ans *= 2
#         else:
#             if now_tate:
#                 ans *= 1
#             else:
#                 ans *= 3
#         tate = now_tate
#         ans = ans % MOD
# print(ans % MOD)
