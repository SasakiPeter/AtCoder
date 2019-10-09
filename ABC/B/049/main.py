# h, w = map(int, input().split())
# m = [list(input()) for _ in range(h)]

# for row in m:
#     print(''.join(row + ['\n'] + row))
#     # print(''.join(row))
#     # print(''.join(row))


h, w = map(int, input().split())
m = [input() for _ in range(h)]

for row in m:
    print(row + '\n' + row)
