# from collections import defaultdict
# n, m = map(int, input().split())
# # カラム集計
# s = []
# for _ in range(n):
#     k, *a = map(int, input().split())
#     s.append(a)
# # 集計
# dd = defaultdict(int)
# for l in s:
#     for k in l:
#         dd[k] += 1

# print(sum(1 if v == n else 0 for k, v in dd.items()))

# 積集合で解く方がスマート
n, m = map(int, input().split())
s = set(range(1, m+1))
for _ in range(n):
    k, *a = map(int, input().split())
    s &= set(a)
print(len(s))
