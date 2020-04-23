# 今度は尺取でやってみる
import sys
input = sys.stdin.readline
n, d, a = map(int, input().split())
xh = sorted([tuple(map(int, input().split()))for _ in range(n)])
INF = 10**18
x_list = [x for x, h in xh]
x_list.append(INF)

end_idx_list = [0]*n
idx = 0
for i in range(n):
    while True:
        if x_list[i]+2*d < x_list[idx]:
            end_idx_list[i] = idx
            break
        idx += 1

damage = [0]*(n+1)
ans = 0
for i in range(n):
    x, h = xh[i]
    h -= damage[i]
    if 0 < h:
        cnt = -(-h//a)
        ans += cnt
        damage[i] += cnt*a
        end_idx = end_idx_list[i]
        damage[end_idx] -= cnt*a

    damage[i+1] += damage[i]
print(ans)

# import sys
# import bisect
# input = sys.stdin.readline
# n, d, a = map(int, input().split())
# xh = sorted([tuple(map(int, input().split()))for _ in range(n)])
# x_list = [x for x, h in xh]

# # imos
# # 番兵が必要なの忘れないでね
# damage = [0]*(n+1)
# ans = 0
# for i in range(n):
#     x, h = xh[i]
#     h -= damage[i]
#     if h <= 0:
#         # imos update
#         damage[i+1] += damage[i]
#         continue
#     cnt = -(-h//a)
#     ans += cnt
#     damage[i] += cnt*a
#     # imos
#     end_idx = bisect.bisect_right(x_list, x+2*d)
#     damage[end_idx] -= cnt*a
#     # imos update
#     damage[i+1] += damage[i]

# print(ans)

# import sys
# input = sys.stdin.readline
# n, d, a = map(int, input().split())
# xh = sorted([tuple(map(int, input().split()))for _ in range(n)])

# x, h = xh[0]
# cnt = -(-h//a)
# ans = cnt
# bomb_list = [(x+2*d, cnt*a)]
# effective_bomb_idx = 0
# for x, h in xh[1:]:
#     idx = effective_bomb_idx
#     # これをする計算量の余裕はない
#     # どこのモンスターまで同時に体力が削れるかは、別で計算しておかないといけない
#     for bomb in bomb_list[idx:]:
#         area, damage = bomb_list[effective_bomb_idx]
#         if x <= area:
#             h -= damage
#             if h <= 0:
#                 break
#         else:
#             effective_bomb_idx += 1

#     if 0 < h:
#         cnt = -(-h//a)
#         bomb_list.append((x+2*d, cnt*a))
#         ans += cnt

# print(ans)
