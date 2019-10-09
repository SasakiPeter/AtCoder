# s = input()
# ans = ''
# for x in s:
#     if x != 'B':
#         ans += x
#     else:
#         # if ans:
#         # 空の文字列に[:-1]しても空が返るから大丈夫
#         ans = ans[:-1]
# print(ans)


# 926
# stackを使う場合
s = input()
stack = []
for c in s:
    if c != 'B':
        stack.append(c)
    else:
        if stack:
            stack.pop()
print(*stack, sep='')
