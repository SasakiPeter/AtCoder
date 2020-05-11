# 約数だけ調べると効率がいい
# なぜなら、xはa-bの倍数だから
x = int(input())


def f(a, b):
    return a**5-b**5


divisors = set()
for i in range(1, int(10**9**.5)+1):
    if x % i == 0:
        divisors |= {i, x//i}


# print(divisors)
for b in range(-1000, 1000):
    for div in divisors:
        a = div+b
        if f(a, b) == x:
            print(a, b)
            exit()


# x = int(input())


# def f(a, b):
#     return a**5-b**5
#     # この程度だと、こっちの方がむしろ遅い
#     # return pow(a, 5)-pow(b, 5)


# for a in range(-1000, 1000):
#     for b in range(-1000, 1000):
#         if f(a, b) == x:
#             print(a, b)
#             exit()
