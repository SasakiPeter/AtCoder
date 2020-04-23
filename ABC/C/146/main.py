# にぶたん
a, b, x = map(int, input().split())
left = 0
right = 10**9+1

loop_cnt = 0
while left != right-1:
    # 中央値が条件を満たすか判定する
    loop_cnt += 1
    mid = (left+right)//2
    price = a*mid+b*len(str(mid))
    # 買える
    if price <= x:
        left = mid
    # 買えない
    else:
        right = mid

print(left)
# 30回くらいで収束する
# print(loop_cnt)

# a, b, x = map(int, input().split())
# MAX = 10**9

# ls = [0]
# for i in range(1, 20):
#     # ここがミソすぎる
#     y = min((x-b*i)//a, int("9"*i))
#     if len(str(y)) == i:
#         ls.append(y)
# # print(ls)
# print(min(max(ls), MAX))
