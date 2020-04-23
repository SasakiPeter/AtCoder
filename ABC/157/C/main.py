from collections import defaultdict

n, m = map(int, input().split())
ans = [0]*n

# sc = set()

sc = defaultdict(set)

for _ in range(m):
    s, c = map(int, input().split())
    # sc.add((s, c))
    sc[s].add(c)
    # if ans[s-1] != 0 and ans[s-1] != c:
    #     print(-1)
    #     print('hoge')
    #     exit()
    # else:
    #     ans[s-1] = c

    ans[s-1] = c


if len(str(int(''.join(map(str, ans))))) != n or not all(len(v) == 1 for v in sc.values()):
    print(-1)
else:
    print(*ans, sep='')
