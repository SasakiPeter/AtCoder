from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
ab = []
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)
    ab.append((a, b))

colors = defaultdict(int)


# k = 1
# init_v = 0
# for v in range(n):
#     if k < len(edges[v]):
#         k = len(edges[v])
#         init_v = v


# v-v2間の色をぬる
def dfs(v, parent):
    # v-parent間で使用済みの色は使えない
    # 使用する色は、親で使っていない中で、最小のものしかない
    palette = [i for i in range(len(edges[v])+1, 0, -1)
               if i != colors[(parent, v)]]
    for v2 in edges[v]:
        if v2 == parent:
            continue
        color = palette.pop()
        colors[(v2, v)] = color
        colors[(v, v2)] = color
        dfs(v2, v)


# どっから探索しても同じ
# dfs(init_v, -1)
dfs(0, -1)

# print(k)
print(max(colors.values()))
for a, b in ab:
    print(colors[(a, b)])
