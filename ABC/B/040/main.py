n = int(input())
ans = n
for h in range(1, int(n**.5)+1):
    w = n//h
    ans = min(ans, w-h+(n-h*w))
print(ans)


# # もうちょっと効率よくかける
# n = int(input())
# ans = n
# for i in range(1, n+1):
#     diff = n-1
#     for j in reversed(range(1, int(i**.5)+1)):
#         if i % j == 0:
#             diff = abs(i//j-j)
#             break
#     cnt = diff+(n-i)
#     if cnt < ans:
#         ans = cnt
# print(ans)
