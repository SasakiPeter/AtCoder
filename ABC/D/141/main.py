# import bisect
# n, m = map(int, input().split())
# A = sorted(map(int, input().split()))
# # heapq.heapify(A)

# for _ in range(m):
#     x = A.pop()
#     x //= 2
#     # 挿入するときに重い
#     bisect.insort_right(A, x)
# print(sum(A))
# # print(-sum(A))
# # print(A)


import heapq
n, m = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapq.heapify(A)

for _ in range(m):
    x = heapq.heappop(A)*(-1)
    x //= 2
    heapq.heappush(A, -x)
print(-sum(A))
# print(A)
