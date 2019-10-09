n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

# for i in range(n):
#     for j in range(n):
#         if a[i][j] == b[0][0]:
#             if j+m <= n and i+m <= n:
#                 if [a[i+k][j:j+m] for k in range(m)] == b:
#                     print('Yes')
#                     exit()
# else:
#     print('No')

# 賢い探索方法
# for i in range(n-m+1):
#     for j in range(n-m+1):
#         if [r[j:j+m] for r in a[i:i+m]] == b:
#             print('Yes')
#             exit()
# else:
#     print('No')


# まとめた方法
c = any([c[j:j+m] for c in a[i:i+m]] == b
        for j in range(n-m+1) for i in range(n-m+1))
print('Yes' if c else 'No')
