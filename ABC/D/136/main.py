# doublingで移動のシミュレーションする場合
# よくわからなかった
# s = input()

# dpでシミューレーションを行う
# よくわからなかった
# def dp(i, j):
#     if i == 1:
#         if s[j] == "L":
#             return j-1
#         else:
#             return j+1

#     return dp(i, dp(i, j))


# print(s)

# リファクタ済
s = input()
prev = part = ""
ans = [0]*len(s)


def calc_lr(block):
    retval = -(-len(block)//2), len(block)//2
    return [retval[::-1], retval][block.index("L") % 2]


for idx, c in enumerate(s):
    if (prev, c) == ("R", "L"):
        i, j = idx-1, idx

    if (prev, c) == ("L", "R"):
        ans[i], ans[j] = calc_lr(part)
        part = c
    else:
        part += c
    prev = c
else:
    ans[i], ans[j] = calc_lr(part)


print(*ans)


# 初手
# from queue import Queue
# s = input()
# prev = ""
# ls = []
# part = ""
# for c in s:
#     if prev == 'L' and c == "R":
#         ls.append(part)
#         part = c
#     else:
#         part += c
#     prev = c
# ls.append(part)

# # print(ls)

# num_ls = Queue()
# for block in ls:
#     len_block = len(block)
#     if len_block % 2 == 0:
#         num_ls.put((len_block//2, len_block//2))
#         # num_ls.append((len_block//2, len_block//2))
#     else:
#         if block.index("L") % 2 == 1:
#             num_ls.put((-(-len_block//2), len_block//2))
#             # num_ls.append((-(-len_block//2), len_block//2))
#         else:
#             num_ls.put((len_block//2, -(-len_block//2)))
#             # num_ls.append((len_block//2, -(-len_block//2)))

# # print(num_ls)

# ans = [0]*len(s)

# prev = ""
# for i, c in enumerate(s):
#     if prev == "R" and c == "L":
#         left, right = num_ls.get()
#         ans[i-1] = left
#         ans[i] = right
#     prev = c

# print(*ans)
