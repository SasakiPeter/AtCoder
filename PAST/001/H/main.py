# 在庫状況をうまく管理してやれば、セグ木いらない？
n = int(input())
C = list(map(int, input().split()))
even_min = min(C[::2])
all_min = min(C)
even_cnt = all_cnt = 0
sold_cnt = [0]*n

q = int(input())
ans = 0
for _ in range(q):
    com, *query = map(int, input().split())
    if com == 1:
        x, a = query
        x -= 1
        left = C[x]-sold_cnt[x]-all_cnt
        if x % 2 == 0:
            left -= even_cnt
        if left < a:
            continue
        sold_cnt[x] += a
        tmp = left-a
        if tmp < all_min:
            all_min = tmp
        if x % 2 == 0 and tmp < even_min:
            even_min = tmp
        ans += a
    elif com == 2:
        a = query[0]
        if even_min < a:
            continue
        even_min -= a
        if even_min < all_min:
            all_min = even_min
        even_cnt += a
        ans += a*((n+1)//2)
    else:
        a = query[0]
        if all_min < a:
            continue
        all_min -= a
        even_min -= a
        all_cnt += a
        ans += a*n

print(ans)

# # セグ木使う 遅延評価じゃないとダメそう


# def update(i, x):
#     i += SEG_LEN
#     SEG[i] = x
#     while i > 0:
#         i //= 2
#         SEG[i] = min(SEG[i*2], SEG[i*2+1])


# def find(left, right):
#     left += SEG_LEN
#     right += SEG_LEN
#     ans = INF
#     while left < right:
#         if left % 2 == 1:
#             ans = min(SEG[left], ans)
#             left += 1
#         left //= 2
#         if right % 2 == 1:
#             ans = min(SEG[right-1], ans)
#             right -= 1
#         right //= 2
#     return ans


# n = int(input())
# INF = (1 << 31) - 1
# SEG_LEN = n
# SEG = [INF]*(SEG_LEN*2)


# def val(i):
#     if i % 2 == 0:
#         return i//2
#     else:
#         return ((n+1)//2)+i//2


# for i, c in enumerate(map(int, input().split())):
#     update(val(i), c)

# # print(SEG)
# ans = 0
# q = int(input())
# for _ in range(q):
#     com, *query = map(int, input().split())
#     if com == 1:
#         x, a = query
#         x -= 1
#         y = find(val(x), val(x)+1)
#         if y < a:
#             continue
#         ans += a
#         update(val(x), y-a)
#     elif com == 2:
#         a = query[0]
#         y = find(0, (n+1)//2)
#         if y < a:
#             continue
#         ans += a*((n+1)//2)
#         for i in range((n+1)//2):
#             x = find(i, i+1)
#             update(i, x-a)
#     else:
#         a = query[0]
#         y = find(0, n)
#         if y < a:
#             continue
#         ans += a*n
#         for i in range(n):
#             x = find(i, i+1)
#             update(i, x-a)
# print(ans)

# # 制約４秒だったので、シミュレーションで良さそう←だめ
# n = int(input())
# C = list(map(int, input().split()))
# q = int(input())
# ans = 0
# all_min = min(C)
# even_min = min(C[::2])
# all_tmp = 0
# even_tmp = 0
# for _ in range(q):
#     com, *query = map(int, input().split())
#     if com == 1:
#         x, a = query
#         x -= 1
#         # うーん遅そう
#         if (all_tmp, even_tmp) != (0, 0):
#             for i in range(n):
#                 C[i] -= all_tmp+even_tmp*((i+1) % 2)
#             all_tmp = even_tmp = 0
#         if a <= C[x]:
#             C[x] -= a
#             ans += a
#             if C[x] < all_min:
#                 all_min = C[x]
#             if x % 2 == 0 and C[x] < even_min:
#                 even_min = C[x]
#     elif com == 2:
#         a = query[0]
#         # C[::2]の最小値が知りたい
#         if even_min < a:
#             continue
#         even_min -= a
#         all_min = min(even_min, all_min)
#         ans += a*((n+1)//2)
#         even_tmp += a
#     else:
#         a = query[0]
#         if all_min < a:
#             continue
#         all_min -= a
#         even_min -= a
#         ans += a*n
#         all_tmp += a
# print(ans)
