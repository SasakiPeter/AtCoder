# なんでも素因数分解から入るのはやめよう！
# 単純に約数の個数が欲しいなら列挙すればいいじゃない
n = int(input())

divisors = set()
for i in range(1, int(-(-n**.5//1))+1):
    if n % i == 0:
        divisors |= {i, n//i}

# print(divisors)
ans = set()
for div in divisors:
    x = n
    if div == 1:
        continue
    while x % div == 0:
        x = x//div
    if x % div == 1:
        ans |= {div}

# print(ans)

n -= 1
# divisors2 = set()
for i in range(1, int(-(-n**.5//1))+1):
    if n % i == 0:
        # divisors2 |= {i, n//i}
        ans |= {i, n//i}

        # divisors.append(n//i)
# print(divisors2)
ans ^= {1}
# print(ans)
print(len(ans))

# ls = []
# for k, v in f:
#     for _ in range(v):
#         ls.append(k)

# print(ls)


# print(ans+1)
