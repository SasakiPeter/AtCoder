from itertools import permutations

# from collections import defaultdict
n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     edges.append((a, b))

# listよりsetやdictの方がinが速い
# listの場合はO(n)かかるけど、setやdictだとO(1)で済むらしい
# edges = [tuple(map(int, input().split())) for _ in range(m)]
edges = {tuple(map(int, input().split())) for _ in range(m)}

# edges = defaultdict(list)
# for _ in range(m):
#     a, b = map(int, input().split())
#     edges[a] += [b]

# print(edges)

ans = 0
# 引数のイテレータの組み合わせを返す, 長さn-1のイテレータを返す
# 長さは定義しなくても大丈夫
for i in permutations(range(2, n+1), n-1):
    # 始点は固定されているため、そのほかのゴールへのありうる
    # 道順を全て列挙した。
    load = [1]+list(i)
    # 道順をさらにedge単位で分割する
    # c = 0
    # for edge in zip(load, load[1:]):
    #     print(edge)
    #     if edge in edges:
    #         c += 1
    # # これで、edge単位に分割した道順が、実現可能か調べられる
    # print(c == n-1)
    ans += sum(1 for edge in zip(load, load[1:])
               if tuple(sorted(edge)) in edges) == n-1
print(ans)


# 得た知見
# グラフの問題は、edgeをtuple in listで保持して
# 道順を通る場合は、最初にゴールに到達できる道順を列挙して、
# それぞれについて、実現可能か判定するとうまくいく
