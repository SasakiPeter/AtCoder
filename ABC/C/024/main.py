# 早くならん
# import sys
# input = sys.stdin.readline
n, d, k = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(d)]
ST = [list(map(int, input().split())) for _ in range(k)]

ans = [0]*k
# cnt = 0
# for L, R in LR:
#     cnt += 1
for cnt, (L, R) in enumerate(LR):
    for i in range(k):
        if ans[i] != 0:
            continue
        s, t = ST[i]
        if L <= s < t:
            ST[i][0] = s = max(min(t, R), s)
        elif t < s <= R:
            ST[i][0] = s = min(max(t, L), s)
        if s == t:
            ans[i] = cnt+1

print(*ans, sep='\n')


# # 早くならん
# # import sys
# # input = sys.stdin.readline
# n, d, k = map(int, input().split())
# LR = [tuple(map(int, input().split())) for _ in range(d)]
# ST = [list(map(int, input().split())) for _ in range(k)]

# cnt = 0
# for L, R in LR:
#     cnt += 1
#     # 早くならん
#     # skip_cnt = 0
#     for i in range(k):
#         if len(ST[i]) == 3:
#             # skip_cnt += 1
#             continue
#         s, t = ST[i]
#         if L <= s < t:
#             ST[i][0] = s = max(min(t, R), s)
#         elif t < s <= R:
#             ST[i][0] = s = min(max(t, L), s)
#         if s == t:
#             ST[i].append(cnt)
#     # if skip_cnt == k:
#     #     break

# for *st, ans in ST:
#     print(ans)
