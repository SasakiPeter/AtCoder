n, m = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)

bc = sorted([list(map(int, input().split()))
             for _ in range(m)], key=lambda x: x[1], reverse=True)

# print(bc)
ans = 0
for b, c in bc:
    for _ in range(b):
        if not A:
            break
        a = A.pop()
        ans += max(a, c)
else:
    ans += sum(A)

print(ans)

# print(A)
# for _ in range(m):
#     b, c = map(int, input().split())
#     # A[b] = max(A[b], c)
#     for i in range(b):
#         A[i] = max(A[i], c)
#     A = sorted(A)
# print(A)
# print(sum(A))
