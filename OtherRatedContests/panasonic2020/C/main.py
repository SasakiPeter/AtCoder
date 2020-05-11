# from decimal import Decimal, getcontext
# getcontext().prec = 1000
# a, b, c = map(Decimal, input().split())
# print("Yes" if a+b+Decimal(2)*((a*b)**Decimal(0.5)) < c else "No")


a, b, c = map(int, input().split())
if c-a-b < 0:
    print("No")
else:
    print("Yes" if (c-a-b)**2-4*a*b > 0 else "No")
