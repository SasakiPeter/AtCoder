from collections import defaultdict
n = int(input())


def f(x):
    s = str(x)
    return (s[0], s[-1])
    # a = x % 10
    # b = 0
    # while x:
    #     b = x
    #     x //= 10
    # return (a, b)


freq = defaultdict(int)

for i in range(1, n+1):
    p = f(i)
    freq[p] += 1

# print(freq)

ans = 0

for i in range(1, n+1):
    a, b = f(i)
    ans += freq[(b, a)]

print(ans)

# O(N)だろうとこうするのはつらい
# for i in range(1, n+1):
#     print(i, ans)
#     if len(str(i)) == 1:
#         if i <= int(str(n)[0]):
#             ans += 1+2*(digit-1)
#         else:
#             ans += digit-1
#         continue
#     s = str(i)
#     front = s[0]
#     rear = s[-1]
#     if rear == '0':
#         continue
#     if int(rear+front) <= n:
#         ans += 1

#     # 3桁以上のやつ
#     if int(rear) < int(str(n)[0]):
#         ans += (digit-2)*10
#     elif int(rear) == int(str(n)[0]):
#         ans += max(int(str(n)[1])*(digit-3)*10, 0)
#     else:
#         ans += max((digit-3)*10, 0)
# print(ans)
