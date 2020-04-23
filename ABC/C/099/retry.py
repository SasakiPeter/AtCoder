# 10**5
n = int(input())
INF = 10**5
answer = INF
# Nを6**pで引き出す分と9**qで引き出す分に分ける
for i in range(n+1):
    # 6**p担当分
    money = i
    cnt = 0
    while money > 0:
        cnt += money % 6
        money //= 6

    # 9**q担当分
    money = n-i
    while money > 0:
        cnt += money % 9
        money //= 9
    if answer > cnt:
        answer = cnt
print(answer)

# for i in range(n+1):
#     # 6**p担当分
#     cost = i
#     ans = 0
#     for p in range(8):
#         ans += (cost // 6**p) % 6

#     # 9**q担当分
#     cost = n-i
#     for q in range(7):
#         ans += (cost // 9**q) % 9
#     if answer > ans:
#         answer = ans
# print(answer)
