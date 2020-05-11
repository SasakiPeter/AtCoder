n = int(input())
A = sorted(int(input())for _ in range(n))

if n % 2 == 0:
    low = A[:n//2]
    high = A[n//2:]
    ans = abs(2*sum(high)-high[0]-(2*sum(low)-low[-1]))
else:
    low = A[:n//2]
    high = A[n//2+1:]
    mid = A[n//2]
    ans = abs(2*sum(high)-high[0]-(2*sum(low)-low[-1]))
    ans += max(high[0]-mid, mid-low[-1])
print(ans)

# from collections import deque
# n = int(input())
# A = sorted(int(input())for _ in range(n))
# L = 1
# R = n-1
# B = deque([A[0]])
# prev_L = prev_R = A[0]
# while L <= R:
#     x, y = A[L], A[R]
#     # 4パターンで最もスコアが高いやつだけ勝負すr
#     if abs(min(prev_L, prev_R)-y) < abs(max(prev_L, prev_R)-x):
#         # xを配置する
#         if prev_L < prev_R:
#             B.append(x)
#             prev_R = x
#         else:
#             B.appendleft(x)
#             prev_L = x
#         L += 1
#     else:
#         # yを配置する
#         if prev_L < prev_R:
#             B.appendleft(y)
#             prev_L = y
#         else:
#             B.append(y)
#             prev_R = y
#         R -= 1

# B = list(B)
# ans = 0
# for x, y in zip(B, B[1:]):
#     ans += abs(x-y)
# print(ans)
