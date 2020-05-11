from collections import defaultdict
s = input()
n, p = len(s), 2019

dd = defaultdict(int)
dd[0] = 1
prev = 0

for i in range(n-1, -1, -1):
    d = int(s[i]) * pow(10, n-i, p)
    prev = (prev + d) % p
    dd[prev] += 1

print(sum(v*(v-1)//2 for v in dd.values()))

# # 3の倍数か判定して、その中で、673の倍数か判定
# # 尺取で
# s = input()
# n = len(s)
# ans = 0
# R = 0
# X = 0
# for L in range(n):
#   #
#   while R<n and :
#     X+=int(s[R])
#     R+=1
#   ans +=
#   X-=int(s[L])


# def is_prime(x):
#     if x == 1:
#         return 0
#     for i in range(2, int(x**.5)+1):
#         if x % i == 0:
#             return 0
#     else:
#         return 1


# def factorization(n):
#     retval = []
#     tmp = n
#     for i in range(2, int(-(-n**.5//1))+1):
#         if tmp % i == 0:
#             cnt = 0
#             while tmp % i == 0:
#                 cnt += 1
#                 tmp //= i
#             retval.append((i, cnt))
#     if tmp != 1:
#         retval.append((tmp, 1))
#     if not retval:
#         retval.append((n, 1))
#     return retval


# print(factorization(2019))


# #!/usr/bin/env python3
# import re
# s = input()
# n = len(s)
# print(s, n)
# # 全ての倍数を洗い出す
# A = []
# for i in range(1, 100):
#     A.append(str(2019*i))
# # print(A)

# ans = 0
# for a in A:
#     for i in range(n):
#         if i+len(a) <= n:
#             # 0は別で計算しないとダメかも
#             if a == s[i:i+len(a)]:
#                 print(a, s[i:i+len(a)])
#                 ans += 1


# # 0だけ
# for x in map(len, re.sub(r'[1-9]', ' ', s).split()):
#     ans += x*(x+1)//2
# print(ans)
