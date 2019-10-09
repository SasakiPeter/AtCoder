s = input()
atgc = 'ATGC'
for x in s:
    if x not in atgc:
        s = s.replace(x, ' ')
print(max(list(map(len, s.split()))+[0]))

# 普通にカウントする場合
# m = c = 0
# for x in s:
#     if x in atgc:
#         c += 1
#     else:
#         c = 0
#     m = max(m, c)
# print(m)
