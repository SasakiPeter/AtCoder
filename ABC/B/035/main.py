from collections import Counter
s = Counter(input())
t = int(input())

x = s['R'] - s['L']
y = s['U'] - s['D']
z = s['?']

distance = abs(x) + abs(y)
if t == 1:
    print(distance+z)
else:
    if z < distance:
        print(distance - z)
    else:
        print((z-distance) % 2)


# s = input()
# t = int(input())

# grid = [0, 0]
# wild_cnt = 0

# for c in s:
#     if c == 'U':
#         grid[1] += 1
#     elif c == 'D':
#         grid[1] -= 1
#     elif c == 'R':
#         grid[0] += 1
#     elif c == 'L':
#         grid[0] -= 1
#     elif c == '?':
#         wild_cnt += 1


# distance = sum(abs(g) for g in grid)

# if t == 1:
#     print(distance+wild_cnt)
# else:
#     if wild_cnt < distance:
#         print(distance - wild_cnt)
#     else:
#         print((wild_cnt-distance) % 2)
