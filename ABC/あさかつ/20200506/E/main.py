# これ、シミュレーションでいけるの？
# 逆操作するとうまく求めることができる
k = int(input())
n = 50
x, y = divmod(k, n)
ans = [i+x for i in range(n)]
for i in range(y):
    i %= n
    ans[i] += n
    for j in range(n):
        if i == j:
            continue
        ans[j] -= 1
print(n)
print(*ans)


# k = int(input())
# if k < 50:
#     n = 50
#     ans = [0]*n
#     ans[0] = (n-1)+k*n
#     print(n)
#     print(*ans)
# else:
#     # n = 50
#     # 割り切れなくても、
#     for i in reversed(range(1, 51)):
#         if k % i == 0:
#             n = i
#             break
#     print(n)
#     m = k//n
#     ans = []
#     for i in range(1, n+1):
#         ans.append(i+m-1)
#     print(*ans)
