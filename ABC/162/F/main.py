n = int(input())
A = list(map(int, input().split()))
if n % 2 == 0:
    print(max(sum(A[::2]), sum(A[1::2])))
else:
    num = n//2
    ans = sum(A[1::2])
    hoge = 0
    X = A[::2]
    X.sort(reverse=True)
    Y = A[1::2]
    Y.sort(reverse=True)
    print(X)
    print(Y)
    print(num)
    print(sum(X[:num]), sum(Y[:num]))

    ans = max(ans, hoge)
    print(ans)


# x_idx = 0
    # y_idx = 0
    # print(Y)
    # print(X)
    # print(num)
    # x_turn = 0
    # for _ in range(num):
    #     if x_turn:
    #         hoge += X[x_idx]
    #         x_idx += 1
    #     else:
    #         hoge += Y[y_idx]
    #         y_idx += 1
    #     x_turn ^= 1
    # fuga = 0
    # x_turn = 1
    # for _ in range(num):
    #     if x_turn:
    #         fuga += X[x_idx]
    #         x_idx += 1
    #     else:
    #         fuga += Y[y_idx]
    #         y_idx += 1
    #     x_turn ^= 1
    # print(hoge, fuga)
