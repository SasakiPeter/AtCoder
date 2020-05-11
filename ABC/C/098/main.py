n = int(input())
s = input()

cum_R = [0]*(n+1)
for i in range(n):
    cum_R[i+1] = cum_R[i]+(s[i] == 'E')
# print(cum_R)
INF = 10**18
ans = INF
for i in range(n):
    cnt_L = i-cum_R[i]
    cnt_R = cum_R[n]-cum_R[i+1]
    ans = min(ans, cnt_L+cnt_R)
print(ans)

# n = int(input())
# s = input()
# cnt_R = s.count('E')
# cnt_L = 0
# INF = 10**18
# ans = INF
# for x in s:
#     if x == 'W':
#         ans = min(ans, cnt_L+cnt_R)
#         cnt_L += 1
#     else:
#         cnt_R -= 1
#         ans = min(ans, cnt_L+cnt_R)
# print(ans)


# n = int(input())
# s = input()
# dp_L = [0]*(n+1)
# dp_R = [0]*(n+1)
# for i in range(n):
#     dp_L[i+1] = dp_L[i]+[0, 1][s[i] == 'W']

# for i in reversed(range(n)):
#     dp_R[i] = dp_R[i+1]+[0, 1][s[i] == 'E']
# print(min(L+R for L, R in zip(dp_L, dp_R)))


# n = int(input())
# s = input()
# dp = [0]*(n+1)

# cnt = 0
# for i in range(n):
#     if s[i] == 'W':
#         cnt += 1
#     dp[i+1] += cnt

# cnt = 0
# for i in reversed(range(n)):
#     if s[i] == 'E':
#         cnt += 1
#     dp[i] += cnt
# print(min(dp))
