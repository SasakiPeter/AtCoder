a, b, n = map(int, input().split())


def f(x):
    return a*x//b-a*(x//b)


print(f(min(n, b-1)))
