# import numpy as np

# n, m, c = map(int, input().split())
# b = np.array(list(map(int, input().split())))
# ans = []
# for i in range(n):
#     a = np.array(list(map(int, input().split())))
#     if b.dot(a)+c > 0:
#         ans.append(i+1)
# print(len(ans))

# numpyを使わない場合 こっちのほうが圧倒的に早い
n, m, c = map(int, input().split())
b_l = list(map(int, input().split()))
# この問題の場合はintで集計もできる
ans = []
for i in range(n):
    a_l = list(map(int, input().split()))
    if sum(a*b for a, b in zip(a_l, b_l)) + c > 0:
        ans.append(i)
print(len(ans))
