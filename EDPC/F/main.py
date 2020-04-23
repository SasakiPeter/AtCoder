s = input()
t = input()

dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
# 貰う
for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

# # 配る
# for i in range(len(s)):
#     for j in range(len(t)):
#         dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
#         dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
#         if s[i] == t[j]:
#             dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)

# 復元
# for row in dp:
#     print(row)


ans = ""
i = len(s)
j = len(t)
while 0 < i and 0 < j:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    # elif dp[i][j] == dp[i-1][j-1]+1:
    else:
        i -= 1
        j -= 1
        ans += s[i]
print(ans[::-1])

# # 2次元DPの存在を知っているだけで、発想できたぞれこれ！！！
# # いや、足りてない、全然ダメ
# # けんちょんさんの記事と、optさんのツイートをみるのだ
# s = input()
# t = input()
# dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]

# # 貰う
# for i in range(1, len(t)+1):
#     x = t[i-1]
#     flag = 0
#     for j in range(1, len(s)+1):
#         dp[i][j] = dp[i-1][j]

#         # このxが出現するのはいつか？を記録する
#         # xが同じ文字がきたときに、問題が発生する
#         # 個数制限付きのナップサックみたいな匂いがする
#         y = s[j-1]
#         if flag:
#             dp[i][j] = dp[i][j-1]
#         elif x == y:
#             dp[i][j] = max(dp[i][j], dp[i-1][j]+1)
#             flag = 1


# # print(dp)
# for row in dp:
#     print(row)
# print(dp[-1][-1])
