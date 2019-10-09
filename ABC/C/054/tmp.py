from itertools import permutations

n, m = map(int, input().split())
edges = {tuple(map(int, input().split())) for _ in range(m)}
# print(edges)

# 道順問題は、全ての道順を列挙しておく
ans = 0
for route in permutations(range(2, n+1)):
    route = [1] + list(route)
    # print(route)
    # cnt = 0
    # for edge in zip(route, route[1:]):
    #     if tuple(sorted(edge)) in edges:
    #         cnt += 1

    # if cnt == n-1:
    #     ans += 1

    # if len([1 for edge in zip(route, route[1:]) if tuple(sorted(edge)) in edges]) == n-1:
    #     ans += 1

    # 実はTrueを入れればいい
    ans += len([1 for edge in zip(route, route[1:])
                if tuple(sorted(edge)) in edges]) == n-1
print(ans)
