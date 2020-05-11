from itertools import accumulate
n = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
T_cum = list(accumulate(T))
print(T_cum)
print(V)

# 速度が最大に達するまでの時間
V_max = [V[0]]
for v1, v2 in zip(V, V[1:]):
    V_max.append(abs(v1-v2))
print(V_max)
ans = 0
for i in range(n):
    t2 = T_cum[i]

    tlim = T_cum[i+1]-V_max[i+1]
    if t2 < tlim:
        # 台形、もしくは三角形になる
        t1 = V_max[i]
        # ここまだ未完成
        ans += max(0, (t2-t1))*V[i]+t1*t1/2
# 考えるのだるくなってきた
