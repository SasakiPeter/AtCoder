x = int(input())

U = 10**9

divisors = set()
for i in range(1, int(U**.5)+1):
    if x % i == 0:
        divisors |= {i, x//i}


# fact = factorization(x)
# a = fact[0][0]
# a -= 1
# b = -1
# print(divisors)


# def f(a, b):
#     return a**4+a**3*b+a**2*b**2+a*b**3+b**4

def f(a, b):
    return a**5-b**5


# print(divisors)
for b in range(-1000, 1000):
    for div in divisors:
        a = div+b
        if f(a, b) == x:
            print(a, b)
            exit()


# # a-bがxの約数になるようにする


# def f(a, b):
#     return (a**5-b**5) == x


# print(a, b, fact)

# for z in range(1, 100000):
#     if f(a*z, b*z):
#         print(a, b)
#         break
