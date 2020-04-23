n = int(input())
# n = 10**7
k = int((2*n)**.5)
for i in range(k, k*(k+1)+1):
    if 2*n >= i*(i+1):
        continue
    k = i
    break
# print(k)


def sigma(a, b):
    if a == b:
        return a
    elif b < a:
        return 0
    else:
        return (a+b)*(b-a+1)//2


# print(sigma(1, k))

# 1~kまでの数字で、Nが作れることがわかっている
# 過剰か？
# print('excess', sigma(1, k)-n)
excess = sigma(1, k)-n
for i in range(1, k+1):
    if i == excess:
        continue
    print(i)
