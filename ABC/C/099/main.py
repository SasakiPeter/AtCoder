n = int(input())


def getNine(n):
    val = 0
    for p in range(1, n):
        tmp = 9**p
        if tmp <= n:
            val = tmp
        else:
            break
    return val


def getSix(n):
    val = 0
    for p in range(1, n):
        tmp = 6**p
        if tmp <= n:
            val = tmp
        else:
            break
    return val


# 貪欲に引いていっても、最適解は得られない　やっちまった
c = 0
while True:
    n -= max(getNine(n), getSix(n), 1)
    c += 1
    if n == 0:
        break

print(c)


# DPの基本形らしい　確かに
# DPは漸化式をたてて、問題を解く

# 状態のz取り方というのがある

# 一番簡単なのは、Nを状態にする
# これを満たす漸化式？
# dp[1]...dp[n-1]の値は知っていると仮定して
# 漸化式を立てるのがコツらしい
# 何通りかで場合分けする
# １円玉を使うかどうか？
# dp[N] = 1 + dp[n-1]
# 6円玉を使うかどうか？
# dp[n] = 1 + dp[n-6]
# dp[n] = 1 + dp[n-6**2]
# dp[n] = 1 + dp[n-6**3]
# っていうこれらの最小値を求めればいいらしい

# 全探索すればいい
# でもその全探索がわからないねん！！
n = int(input())

for i in range(n+1):
    c = 0
    # 6**pで引き出す分と、9**pで引き出す分に分ける
    while i > 0:
        # 6**p 引き出した後のあまりをcにたす
        c += i % 6

    j = n-i
    while j > 0:
        c += j % 9
