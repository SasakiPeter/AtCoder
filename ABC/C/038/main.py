n = int(input())
A = list(map(int, input().split()))

# 勉強のために尺取

# 意味わからん尺取になった　解説の尺取が意味不
ans = n
R = 0
for L in range(n):
    if L != R:
        continue
    while True:
        R += 1
        if R == n:
            break
        if A[R-1] < A[R]:
            continue
        break
    # print(L, R, ans)
    ans += (R-L)*(R-L-1)//2

print(ans)

# # 不完全な尺取
# R = 0
# for L in range(n):
#     # おっかけなくちゃいけないのに、スタート地点に戻されてるので尺取じゃない
#     R = L
#     while R != n-1:
#         R += 1
#         if A[R-1] < A[R]:
#             ans += 1
#             continue
#         break

# print(ans)


# # zip使えば、尺取しなくていい
# ans = n
# prev = 0
# for x, y in zip(A, A[1:]):
#     if x < y:
#         prev += 1
#     else:
#         prev = 0
#     ans += prev
# print(ans)
