n, m, a, b = map(int, input().split())
ans = []

# for i in range(m):
#     c = int(input())
#     if n <= a:
#         n += b
#     n -= c
#     if n < 0:
#         ans.append(i+1)

# print('complete' if len(ans) == 0 else ans[0])

# for elseがあるんや
for i in range(m):
    c = int(input())
    if n <= a:
        n += b
    n -= c
    if n < 0:
        print(i+1)
        break
else:
    print('complete')
