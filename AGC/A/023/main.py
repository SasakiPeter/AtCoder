# 累積はitertoolsとかnumpy使うと楽
from collections import defaultdict
from itertools import accumulate
n = int(input())
A = accumulate(map(int, input().split()))
cnt = defaultdict(int)
cnt[0] += 1
for a in A:
    cnt[a] += 1
print(sum(v*(v-1)//2 for v in cnt.values()))

# from collections import defaultdict
# n = int(input())
# A = list(map(int, input().split()))
# dd = defaultdict(int)
# dd[0] += 1
# S = [0]*(n+1)
# for i in range(n):
#     S[i+1] = S[i]+A[i]
#     dd[S[i+1]] += 1
# print(sum(v*(v-1)//2 for v in dd.values()))
