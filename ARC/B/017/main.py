# こういう問題、デバッグのためにも集計した方が良さそう
# 実行時間もほぼ変わらないし
from collections import defaultdict
n, k = map(int, input().split())
dd = defaultdict(int)
ans = cnt = prev = 0
for _ in range(n):
    a = int(input())
    if prev < a:
        cnt += 1
    else:
        # if k <= cnt:
        #     ans += cnt-k+1
        dd[cnt] += 1
        cnt = 1
    prev = a
else:
    # if k <= cnt:
    #     ans += cnt-k+1
    dd[cnt] += 1
# print(dd)
for length, v in dd.items():
    if k <= length:
        ans += (length-k+1)*v
print(ans)
