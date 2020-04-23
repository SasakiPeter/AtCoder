from itertools import product, combinations
n = int(input())
coms = input()
INF = 10**5
ans = INF


# 適当にコマンドを生成しながらカウントする場合
it = product("ABXY", repeat=2)
for LR in combinations(it, 2):
    L, R = map(lambda x: "".join(x), LR)
# for a, b, c, d in product("ABXY", repeat=4):
#     L = a+b
#     R = c+d
    x = []
    prev = coms[0]
    for com in coms[1:]:
        if prev+com == L:
            x.append("L")
            prev = ""
            continue
        elif prev+com == R:
            x.append("R")
            prev = ""
            continue
        else:
            x.append(prev)
        prev = com
    else:
        x.append(prev)
    ans = min(ans, len("".join(x)))
print(ans)
