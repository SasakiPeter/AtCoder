n, m, k = map(int, input().split())

GRAPH = [[0]*n for _ in range(n)]
BLOCK = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    GRAPH[a][b] = GRAPH[b][a] = 1

for _ in range(k):
    a, b = map(lambda x: int(x)-1, input().split())
    BLOCK[a][b] = BLOCK[b][a] = 1


# xに0を入れると、その友達の友達を含めた配列を返す
# どうやって抜けるんだっけ？
def make_dfs():
    visited = [0]*n

    def dfs(v):
        visited[v] = 1
        # ここGRAPH[v]からとると、無限に回っちゃうので注意
        for v2 in range(n):
            if not GRAPH[v][v2]:
                continue
            if visited[v2]:
                continue
            dfs(v2)
        return visited
    return dfs


ans = []
for i in range(n):

    # 友達の友達リスト
    f = make_dfs()
    friends = f(i)
    # print(friends)

    # 相互フォローリスト
    follow = GRAPH[i]
    # print(follow)

    # ブロックリスト
    block = BLOCK[i]
    # print(block)

    # 友達の友達の中には、相互フォローの人たちは入っている
    # 友達の友達には、ブロックリストは入っていない。
    bl = sum(f and b for f, b in zip(friends, block))

    ans.append(sum(friends) - (sum(follow)+bl)-1)

print(*ans)

# n, m, k = map(int, input().split())
# f_ls = sorted(sorted(map(int, input().split())) for _ in range(m))
# b_ls = sorted(sorted(map(int, input().split())) for _ in range(k))
# print(f_ls)
# print(b_ls)
