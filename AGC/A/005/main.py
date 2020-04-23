# stack使った場合
x = input()
stack = []
for s in x:
    if s == 'S':
        stack.append(s)
    else:
        if not stack:
            stack.append(s)
        elif stack[-1] == 'S':
            stack.pop()
        else:
            stack.append(s)
print(len(stack))


# # 普通にカウントした場合
# x = input()
# # Sの右にあるTの数を数える
# # Sと出会ってから、Tが現れるまで
# cnt = 0
# ans = len(x)
# for s in x:
#     # print(s, cnt, ans)
#     if s == "S":
#         cnt += 1
#     else:
#         if 0 < cnt:
#             cnt -= 1
#             ans -= 2
# print(ans)

# # 自明のTLE解
# x = input()

# while True:
#     before = x
#     x = x.replace("ST", "")
#     if before == x:
#         break
# print(len(x))
