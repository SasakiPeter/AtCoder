import heapq
n = int(input())
AB = [tuple(map(int, input().split()))for _ in range(n)]
AB.sort(reverse=True)

tasks = []
ans = 0
for k in range(1, n+1):
    while AB and AB[-1][0] == k:
        a, b = AB.pop()
        heapq.heappush(tasks, -b)
    ans += -heapq.heappop(tasks)
    print(ans)
