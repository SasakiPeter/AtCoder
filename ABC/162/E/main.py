n, k = map(int, input().split())
U = 10**5
k = U


def factorization(n):
    retval = []
    tmp = n
    for i in range(2, int(-(-n**.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            # retval.append((i, cnt))
            for _ in range(cnt):
                retval.append(i)
    if tmp != 1:
        retval.append(tmp)
    if not retval:
        retval.append(n)
    # return retval
    return retval


ans = 0
for i in range(1, U+1):
    fact_list = factorization(i)

    print(fact_list)
print(ans)
