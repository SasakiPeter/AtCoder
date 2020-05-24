# 列挙は無理なので、最小をどのように構築すればいいかを
# 考察すれば良い
import heapq
n, k, d = map(int, input().split())
A = list(map(int, input().split()))

ans = []
choices = []
end_idx = 0
INF = 10**18
largest_idx = -INF
while len(ans) != k:
    prev_end = end_idx
    i = len(ans)+1
    end_idx = n-(k-i)*d

    for j in range(prev_end, end_idx):
        heapq.heappush(choices, (A[j], j))
    while choices:
        val, idx = heapq.heappop(choices)
        if idx <= largest_idx+d-1:
            continue
        largest_idx = idx
        ans.append(val)
        break
    else:
        print(-1)
        exit()
print(*ans)
