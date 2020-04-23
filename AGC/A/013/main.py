n = int(input())
A = list(map(int, input().split()))

ans = 1
prev = A[0]
direction = 0
for a in A[1:]:
    if direction == 1:
        if prev > a:
            ans += 1
            direction = 0
            prev = a
            continue
    if direction == -1:
        if prev < a:
            ans += 1
            direction = 0
            prev = a
            continue
    if direction == 0:
        if prev < a:
            direction = 1
        elif prev > a:
            direction = -1
    prev = a
print(ans)

# if n == 1 or n == 2:
#     print(1)
#     exit()

# ans = 1
# is_increase = A[2] < A[3]
# reset = 0
# for a, b in zip(A[1:-1], A[2:]):
#     if reset:
#         if a == b:
#             continue
#         elif a < b:
#             is_increase = 1
#         else:
#             is_increase = 0
#         reset = 0

#     if is_increase:
#         if a < b:
#             pass
#         else:
#             ans += 1
#             is_increase = 0
#             reset = 1
#     else:
#         if a < b:
#             ans += 1
#             is_increase = 0
#             reset = 1
#         else:
#             pass
# print(ans)
