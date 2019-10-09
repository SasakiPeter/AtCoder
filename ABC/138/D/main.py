from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, q = map(int, input().split())


# class Node:
#     def __init__(self, index):
#         self.index = index
#         self.point = 0

#     def updatePoints(self, point):
#         self.point += point


# 2*10**5
# nodes = [Node(i) for i in range(1, n + 1)]

# 2*10**5
edges = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)


# これ、メモ化すればいい
# 一度探索したpが来た場合は、すでに計算した結果を返せばいい

def memoize(f):
    memo = {}

    def memoized(*args):
        if args not in memo.keys():
            memo[args] = f(*args)
        return memo[args]
    return memoized


# parent node が与えられる
@memoize
def selectNode(p):
    selected = [p]
    ls = edges[p]
    selected += ls

    while True:
        if ls == []:
            break
        for x in ls:
            ls = edges[x]
            selected += ls
    return selected


# 一回計算結果を外に出しちゃう　ポイントとともにリストにする

dd = {i: 0} for i in range((q))

# 2*10**5
for i in range(q):
    p, x = map(int, input().split())
    for idx in selectNode(p):
        dd[idx] += x

print(*(dd[i+1] for i in range(n)))

# 実は集計すればいいだけでは？

# 2*10**5
# for idx, node in enumerate(nodes):
#     if idx + 1 in node_index_list:
#         node.updatePoints(x)

# for _ in range(q):
#     p, x = map(int, input().split())
#     node_index_list = selectNode(p)
#     # ここ遅くね
#     for idx, node in enumerate(nodes):
#         if idx + 1 in node_index_list:
#             node.updatePoints(x)

# print(*(node.point for node in nodes))
