def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a*b)//gcd(a, b)


def f(abc):
    a, b, c = abc
    return b//c-a//c


a, b, c, d = map(int, input().split())
a -= 1
# ans = b-a


print(b-a+sum(map(f, [(b, a, c), (b, a, d), (a, b, lcm(c, d))])))

# print(b-a+z-sum(xy))
# ans -= (b//c - a//c)
# ans -= (b//d - a//d)
# ans += (b//lcm(c, d)-a//lcm(c, d))
# print(ans)
