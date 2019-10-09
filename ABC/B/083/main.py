n, a, b = map(int, input().split())
# ans = 0
# for x in range(1, n+1):
#     y = sum(map(int, str(x)))
#     if a <= y <= b:
#         ans += x
# print(ans)

print(sum(x for x in range(1, n+1) if a <= sum(map(int, str(x))) <= b))
