a, b = map(int, input().split())


def factorization(n):
    retval = []
    tmp = n
    for i in range(2, int(-(-n**.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            retval.append((i, cnt))
    if tmp != 1:
        retval.append((tmp, 1))
    if not retval:
        retval.append((n, 1))
    return retval


fa = set([x for x, y in factorization(a)]+[1])
fb = set([x for x, y in factorization(b)]+[1])
ans = 0
for x in fa:
    if x in fb:
        ans += 1
print(ans)
