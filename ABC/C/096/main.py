# h, w = map(int, input().split())
# m = [list(input()) for _ in range(h)]

# for i in range(h):
#     for j in range(w):
#         if m[i][j] == '#':
#             cnt = sum([0 <= i-1, i+1 < h, 0 <= j-1, j+1 < w])
#             # up
#             if 0 <= i-1:
#                 if m[i-1][j] != '#':
#                     cnt -= 1

#             # down
#             if i+1 < h:
#                 if m[i+1][j] != '#':
#                     cnt -= 1
#             # left
#             if 0 <= j-1:
#                 if m[i][j-1] != '#':
#                     cnt -= 1

#             # right
#             if j+1 < w:
#                 if m[i][j+1] != '#':
#                     cnt -= 1

#             if cnt == 0:
#                 print('No')
#                 exit(0)
# else:
#     print('Yes')

# padding入れる解法賢い
h, w = map(int, input().split())
m = [['.']*(w+2)]
for _ in range(h):
    m.append(list('.' + input() + '.'))
m.append(['.']*(w+2))

for i in range(1, h+1):
    for j in range(1, w+1):
        if m[i][j] == '#':
            # if m[i-1][j] == '.' and m[i+1][j] == '.' and m[i][j-1] == '.' and m[i][j+1] == '.':
            if all(m[i+x][j+y] == '.' for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                print('No')
                exit(0)
else:
    print('Yes')
