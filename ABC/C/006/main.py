n, m = map(int, input().split())

if n*4 < m:
    print(-1, -1, -1)
else:
    for z in range(m//4+1):
        y = m-2*(n+z)
        if 0 <= y and 0 <= n-y-z:
            print(n-y-z, y, z)
            break
    else:
        print(-1, -1, -1)

    # a = m//4+1
    # for z in range(a):
    #     b = (m-4*z)//3+1
    #     for y in range(b):
    #         if 2*(n-y-z)+3*y+4*z == m:
    #             print(n-y-z, y, z)
    #             exit()
    # else:
    #     print(-1, -1, -1)

    # 貪欲にいけない
    # d, m = divmod(m, 4)
    # print(d, m)
    # baby = d
    # a, b = divmod(m, 3)
    # old = a
    # print(b, old, baby)
