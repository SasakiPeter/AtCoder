# s = int(input())

# MAX = 1000000


# def f(n):
#     def odd(n):
#         return 3*n+1

#     def even(n):
#         return n/2
#     return odd(n) if n % 2 else even(n)


# dic = {}


# def a(n):
#     if n == 1:
#         dic[n] = s
#         return dic[n]
#     else:
#         dic[n] = f(dic[n-1])
#         return dic[n]


# for m in range(1, MAX):
#     am = a(m)
#     if sum(1 if v == am else 0 for v in dic.values()) == 2:
#         print(m)
#         break


# ナンジャコリャー
s = int(input())
l = []
while (s not in l):
    l.append(s)
    if s % 2 == 0:
        s = s/2
    else:
        s = 3*s+1
print(len(l) + 1)
