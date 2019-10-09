x = int(input())
# なんかうまくいかない
# print(max(int(x**(1/p))**p for p in range(2, 10)))

# 全探索 O(n^2)
ans = []
for b in range(1, 1000):
    for p in range(2, 10):
        tmp = b**p
        if tmp <= x:
            ans.append(tmp)
        else:
            break
print(max(ans))


# これもうまくいかない　なんで？
# ans = []
# for p in range(2, 10):
#     b = int(x**(1/p))
#     assert b in range(1, x+1), f"{b},{x},{p}"
#     tmp = b**p
#     if tmp <= x:
#         ans.append(tmp)
# print(max(ans))
