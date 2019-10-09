# s = [int(input()) for _ in range(3)]
# for x in s:
#     if x == max(s):
#         print(1)
#     elif x == min(s):
#         print(3)
#     else:
#         print(2)

# s = [int(input()) for _ in range(3)]
# for x in s:
#     print(sorted(s)[::-1].index(x)+1)

# indexを使うのは３流
# 坐圧で書いたコードを思い出せ
s = [int(input()) for _ in range(3)]
r = {x: i+1 for i, x in enumerate(sorted(s)[::-1])}
# for x in s:
#     print(r[x])
print(*(map(lambda x: r[x], s)), sep='\n')
