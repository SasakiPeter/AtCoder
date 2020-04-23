# とっかかりを掴むために、全探索で実験してみる←判定わからず無理
# from itertools import product
n = int(input())
A = list(map(int, input().split()))

# for i in product("01", repeat=n):
#     i = "".join(i)
#     print(i)
#     # いや、判定わからんわ

# 計算間に合うのか？　→　O（NlogN）
boxes = [None]*(n+1)
for i in range(n, 0, -1):
    coef = 1
    # tmp = boxes[i]
    tmp = 0
    while i*(coef+1) <= n:
        coef += 1
        # これが、
        tmp += boxes[i*coef]
    # if tmp % 2:
    #     # 存在しない時
    #     break
    # A[nー1]が０なら、がtmpが２で割り切れたら、0 割り切れないなら1
    # A[n-1]が1なら、tmpが２で割り切れたら１　割り切れないなら０
    # print(A[i-1], tmp, i)
    boxes[i] = A[i-1] ^ (tmp % 2)
# print(boxes)

ans = []
for idx, v in enumerate(boxes):
    if v == 1:
        ans.append(idx)

print(len(ans))
if len(ans) > 0:
    print(*ans)
