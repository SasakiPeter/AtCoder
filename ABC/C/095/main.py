# ABセットの買う枚数を探索した脳筋コード
A, B, C, X, Y = map(int, input().split())
ans = A*X+B*Y
for Z in range(10**5+1):
    Z *= 2
    price = A*max(X-Z//2, 0)+B*max(Y-Z//2, 0)+C*Z
    ans = min(ans, price)
print(ans)

# A, B, C, X, Y = map(int, input().split())
# if 2*C < A+B:
#     if X < Y:
#         ans = 2*C*X+(Y-X)*min(B, 2*C)
#     else:
#         ans = 2*C*Y+(X-Y)*min(A, 2*C)
# else:
#     ans = A*X+B*Y
# print(ans)
