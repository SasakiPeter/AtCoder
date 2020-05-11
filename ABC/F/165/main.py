# DFSしながらLISを記録して、最後に出力
import bisect
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 問題は、再帰関数の引数に、LISの配列を持たせないといけないところ

n = int(input())
A = list(map(int, input().split()))
edges = [[]for _ in range(n)]
for _ in range(n-1):
    u, v = list(map(lambda x: int(x)-1, input().split()))
    edges[u].append(v)
    edges[v].append(u)
INF = 10**18
ans = [INF]*n


# リライトしたら、リライトしたことを子に伝えて、あとで元に戻す
def dfs(v, parent):
    x = bisect.bisect_left(lis, A[v])
    # if v == 7:
    #     print(lis)
    prev = lis[x]
    lis[x] = A[v]
    ans[v] = bisect.bisect_left(lis, INF)
    for v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, v)
        # ここで、vで行った変更を戻せばいいんじゃね？
    lis[x] = prev


lis = [INF]*n
dfs(0, -1)
# print(ans)
for x in ans:
    print(x)
