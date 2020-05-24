# 宝石が全て取れるような最小全域木がわかれば
# その辺の数の２倍が答え
n, x = map(int, input().split())
H = list(map(int, input().split()))
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)


need_v = [0]*n


def dfs(v, parent):
    if H[v]:
        need_v[v] = 1

    for v2 in edges[v]:
        if v2 == parent:
            continue
        # 探索した頂点に、宝石があれば、
        # vも必要なノード
        dfs(v2, v)
        if need_v[v2]:
            need_v[v] = 1


dfs(x-1, -1)
# need_v_cnt = sum(need_v)
# print(2*(need_v_cnt-1) if 0 < need_v_cnt else 0)
print(2*(max(0, sum(need_v)-1)))
