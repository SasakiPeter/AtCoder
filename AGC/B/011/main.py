n = int(input())
A = sorted(map(int, input().split()))

t = 0
s = A[0]
for i in range(1, n):
    if 2*s < A[i]:
        t = i
    s += A[i]

print(n-t)

# import heapq
# n = int(input())
# A = list(map(int, input().split()))
# heapq.heapify(A)

# cnt = 1
# prev = heapq.heappop(A)
# while A:
#     x = heapq.heappop(A)
#     if prev > x:
#         heapq.heappush(A, prev)
#         prev = x
#         continue
#     # print(prev, x, A, cnt)
#     if 2*prev < x:
#         cnt = 1
#     else:
#         cnt += 1
#     # cnt += 1
#     prev += x

# print(cnt)
