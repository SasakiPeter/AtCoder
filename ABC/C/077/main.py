import bisect
n = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
# print(A)
# print(B)
# print(C)
ans = 0
for i in range(n):
    b = B[i]
    a = bisect.bisect_left(A, b)
    c = n-bisect.bisect_right(C, b)
    # print(a, b, c)
    ans += a*c
print(ans)
