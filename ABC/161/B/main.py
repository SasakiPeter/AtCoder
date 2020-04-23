n, m = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
sum_A = sum(A)
ninki = A[:m]
if 4*m*ninki[-1] < sum_A:
    print("No")
else:
    print("Yes")
# cnt = 0
# for a in A:
#     if 1 < sum_A*4*m:
#         continue
#     cnt += 1
# print("Yes" if m <= cnt else "No")
