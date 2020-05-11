import bisect
from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
junk = []
for i in range(n):
    s = input()
    L_cnt = 0
    R_cnt = 0
    for c in s:
        if c == '(':
            L_cnt += 1
        else:
            if L_cnt != 0:
                L_cnt -= 1
            else:
                R_cnt += 1
    if 0 in (L_cnt, R_cnt):
        cnt['L'] += L_cnt
        cnt['R'] += R_cnt
    else:
        junk.append((R_cnt, L_cnt, i))
        # LとRの大きい方

        # cnt['RL_L'] += L_cnt
        # cnt['RL_R'] += R_cnt

# junkが1こなら貪欲にいける
# junkが２子あると、

R_sort = sorted(junk)
L_sort = sorted(junk, key=lambda x: x[1])

while R_sort:
    R1, L1, idx1 = R_sort.pop()
    R2, L2, idx2 = L_sort.pop()


print(cnt, R_sort, L_sort)
