n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(n):
#     x, y, h = map(int, input().split())
#     xyh.append((x, y, h))

# 高度が０でない任意の１つの点を定める→hが決まる
x_, y_, h_ = sorted(xyh, key=lambda x: x[2], reverse=True)[1]

for cx in range(101):
    for cy in range(101):
        H = h_+abs(x_ - cx) + abs(y_ - cy)
        for x, y, h in xyh:
            if max(H - abs(x-cx)-abs(y-cy), 0) != h:
                break
        else:
            print(cx, cy, H)
            exit()

        # if len(ans) == n:
        #     print(*ans[0])
        #     exit()

        # for i in range(n):
        #     h = dots[i][2]+abs(dots[i][0] - cx) + abs(dots[i][1]-cy)
        #     h_ls.append(h)

        # if len(set(h_ls)) == 1:
        #     print(cx, cy, h_ls[0])
        #     exit()

# for cx in range(101):
#     for cy in range(101):
#         h_ls = []
#         for i in range(n):
#             h = dots[i][2]+abs(dots[i][0] - cx) + abs(dots[i][1]-cy)
#             h_ls.append(h)

#         if len(set(h_ls)) == 1 and h_ls[0]:
#             print(cx, cy, h_ls[0])
#             exit()

# print(ans)
