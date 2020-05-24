n = int(input())
A = list(map(int, input().split()))
INF = 10**18
ans = -INF
for i in range(n):
    aoki = -INF
    takahashi = -INF
    for j in range(n):
        # takahashi君はi番目を選ぶ
        if i == j:
            continue
        # j番目を青木君が選ぶとは限らないけど、
        # 選ぶ可能性があるので探索する
        # 選ぶ条件は、高橋君の得点が最も高いところ
        # それは、選んだi,jの区間において、1::2の和が
        # 最大の点
        # その時の、高橋君の点数も記録しておく
        if i < j:
            t = A[i:j+1]
        else:
            t = A[j:i+1]
        x = sum(t[::2])
        y = sum(t[1::2])
        if aoki < y:
            takahashi = x
            aoki = y
    if ans < takahashi:
        ans = takahashi
print(ans)
