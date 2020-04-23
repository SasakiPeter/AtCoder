# youtubeの回答
s = input()
n = len(s)
A = [0]*(n+1)

for i in range(n):
    if s[i] == '<':
        A[i+1] = max(A[i+1], A[i]+1)

for i in reversed(range(n)):
    if s[i] == '>':
        A[i] = max(A[i], A[i+1]+1)

# print(A)
print(sum(A))

# # 解説の回答
# s = input()
# L = [0]*(len(s)+1)
# R = [0]*(len(s)+1)

# for i in range(len(s)):
#     if s[i] == '<':
#         L[i+1] = L[i]+1

# for i in range(len(s)-1, -1, -1):
#     if s[i] == '>':
#         R[i] = R[i+1]+1

# print(sum(max(x, y) for x, y in zip(L, R)))

# print(L)
# print(R)
# A = [max(x, y) for x, y in zip(L, R)]
# print(sum(A))


# 勇猛果敢に取り掛かったが、ぶち殺されたやつ
# 一回のループで何とかしようっていう考えから抜けた方がいい
# s = input()
# ans = 0
# inc_cnt = 0
# dec_cnt = 0
# prev = ""
# for a in s:
#     if prev+a == "><":
#         # if inc_cnt < dec_cnt:
#         #     ans += dec_cnt
#         inc_cnt = 0
#         dec_cnt = 0
#     if prev+a == "<>":
#         dec_cnt = -1
#     if a == '<':
#         inc_cnt += 1
#         ans += inc_cnt
#     else:
#         dec_cnt += 1
#         ans += dec_cnt
#         # if inc_cnt<dec_cnt:
#         #   ans+=dec_cnt
#         # if dec_cnt-1 < inc_cnt:
#         #     ans += dec_cnt-1
#         # else:
#         #     ans += dec_cnt-1+inc_cnt
#     print(a, ans, inc_cnt, dec_cnt)
#     prev = a
# print(ans)
