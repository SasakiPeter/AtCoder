A, B, C, X = [int(input()) for _ in range(4)]
# cnt = 0
# for a in range(A+1):
#     for b in range(B+1):
#         if 0 <= (X-500*a-100*b) <= C*50:
#             cnt += 1
#         # for c in range(C+1):
#         #     if 500*a+100*b+50*c == X:
#         #         cnt += 1
#         #         break
# print(cnt)

print(len([1 for a in range(A+1)
           for b in range(B+1) if 0 <= X-500*a-100*b <= C*50]))

# ダサいし重い方法
# print([500*a+100*b+50*c for a in range(A*1)
#        for b in range(B+1) for c in range(C+1)].count(X))
