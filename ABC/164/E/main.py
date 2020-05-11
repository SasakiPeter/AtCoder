# とりあえず、資金が潤沢にある時
n, m, s = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    graph[u-1][v-1] = graph[v-1][u-1] = b

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for x in graph[0][1:]:
    print(x)
# for row in graph:
#     print(row)

# 途中何処かを中継地として、目的地までいくときに、
# その中継地までのどこか最も効率がいいところで、両替をして、
# 最終目的地まで、いくときにかかる最小に時間？
