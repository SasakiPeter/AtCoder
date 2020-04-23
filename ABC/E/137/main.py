# 圧倒的Bellman-Ford
# pypyかな
# 全ての辺から、pコストを引いておけばいい
import sys
input = sys.stdin.readline
n, m, p = map(int, input().split())
edges = []
forward_edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, p-c))
    forward_edges[a].append(b)


can_reach = [0]*n
stack = [0]
while stack:
    v = stack.pop()
    if can_reach[v]:
        continue
    can_reach[v] = 1
    for v2 in forward_edges[v]:
        if can_reach[v2]:
            continue
        stack.append(v2)


INF = 10**10
dist = [INF]*n
dist[0] = 0
# prev = [INF]*n
for i in range(n):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        dist[v2] = dist[v]+c
        # prev[v2] = v

negative = [0]*n
for i in range(n):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        # startから到達できない点は更新しない
        if not can_reach[v2]:
            continue
        dist[v2] = -INF
        negative[v2] = 1

if negative[-1]:
    print(-1)
else:
    print(max(0, -dist[-1]))


# print(dist)
# print(negative)

# got_infinity_coins = 0
# for i in range(n):
#     if negative[i]:
#         if can_reach[i] and can_goal[i]:
#             got_infinity_coins = 1
#             break

# negativeが
# goalから探索していって、negative点滅しているところに到達したら
# 負の閉路に到達可能で、それがゴールに伝播してるかを確かめられる


# ゴールから到達できるノードを先に列挙しておく

# bellman-fordで辺を更新するときに、
# このノードリストに入っていない辺は更新する必要がない

# 逆に、更新する場合、そのノードは必ずゴールへ到達可能なノードである
#


# print(prev)
# スタートから、negativeに入って、そこから、ゴールにいくような経路が存在するか？

# 負の閉路に到達可能で、それがゴールに伝播するかを判定したい


# 負の得点にしておいた
# Bellman-fordは全ての頂点に対して、edge分緩和するので、O(VE)
# このゲームの場合は、ゴールへの道中に、無限にコインが拾えるところがあったら、
# 寄り道していい感じだと思われる

# can_goal = [0]*n


# def dfs(v, parent):
#     can_goal[v] = 1
#     for v2 in backward_edges[v]:
#         if parent == v2:
#             continue
#         dfs(v2, v)


# dfs(n-1, -1)
# # print(can_goal)

# def dfs(v, parent):
#     can_reach[v] = 1
#     for v2 in forward_edges[v]:
#         if parent == v2:
#             continue
#         dfs(v2, v)

# dfs(0, -1)
# print(can_reach)

# can_goal = {i for i in range(n) if visited[i]}
# print(can_goal)
