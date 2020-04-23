from collections import Counter
n = int(input())
*a, = map(int, input().split())

if sum(a) == 0:
    print("Yes")
elif n % 3 != 0:
    print("No")
else:
    can_put_on = False
    c = Counter(a)
    if c[0] == n//3 and len(c) == 2:
        can_put_on = True
    if len(c) == 3:
        s = 0
        for k in c.keys():
            s ^= k
        # print(s)
        if s == 0 and all(v == n//3 for v in c.values()):
            can_put_on = True

    print("Yes" if can_put_on else "No")

# n**2
# for i in range(n):
#     for j in range(i+1, n):
#         x = a[i]
#         y = a[j]
#         # print(x, y)
#         if x ^ y not in a:
#             print("No")
#             exit()
# else:
#     print("Yes")
