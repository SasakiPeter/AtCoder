# # numba使い方ようわからん

# from collections import Counter
# from numba import njit
# n = int(input())
# s = input()
# c = Counter(s)
# rgb = set(['R', 'G', 'B'])
# ans = c['R']*c['G']*c['B']


# @njit
# def f(n):
#     retval = 0
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             x, y = s[i], s[j]
#             if x == y:
#                 continue
#             if n <= 2*j-i:
#                 continue
#             z = s[2*j-i]
#             if {x, y, z} == rgb:
#                 retval += 1
#     return retval


# print(ans-f(n))


from collections import Counter
n = int(input())
s = input()
c = Counter(s)
# rgb = set(['R', 'G', 'B'])
ans = c['R']*c['G']*c['B']
for i in range(n-2):
    for j in range(i+1, n-1):
        # x, y = s[i], s[j]
        # if x == y:
        # if s[i] == s[j]:
        #     continue
        if n <= 2*j-i:
            continue
        # z = s[2*j-i]
        # if x != z and y != z:
        # if {x, y, z} == rgb:
        # if {s[i], s[j], s[2*j-i]} == rgb:

        # ギリギリ通る
        if s[i] != s[j] and s[i] != s[2*j-i] and s[j] != s[2*j-i]:
            ans -= 1

print(ans)
