
# def is_prime(x):
#     if x == 1:
#         return False
#     d = 2
#     while d**2 <= x:
#         if x % d == 0:
#             return False
#         d += 1
#     else:
#         return True


# ここ、エラトステネスの篩を使えばもっと早くなる

# prime = [0]*(10**5+1)
# primes = []
# for x in range(2, 10**5+1):
#     if is_prime(x):
#         # prime[x] = 1
#         primes.append(x)

U = 10**5
is_prime = [1]*(U+1)
is_prime[0] = 0
is_prime[1] = 0
for p in range(2, int(U**.5)+1):
    if is_prime[p]:
        for q in range(2*p, U+1, p):
            is_prime[q] = 0

primes = [p for p, tf in enumerate(is_prime) if tf]

# print(primes)
# # 10**4個
# print(len(primes))


A = [0]*(10**5+1)
for prime in primes:
    # if is_prime((prime+1)//2):
    if is_prime[(prime+1)//2]:
        A[prime] = 1

# for i in range(1, U+1, 2):
#     if is_prime[i] and is_prime[(i+1)//2]:
#         A[i] = 1


S = [0]*(10**5+1)
for i in range(1, 10**5+1):
    S[i] = S[i-1]+A[i]

# print(S)

q = int(input())
for _ in range(q):
    L, R = map(int, input().split())
    ans = S[R]-S[L-1]
    print(ans)


# like_numbers = []
# for prime in primes:
#     if is_prime((prime+1)//2):
#         like_numbers.append(prime)

# # print(like_numbers)
# # # 672個
# # print(len(like_numbers))

# A = [0]*(10**5+1)
# for x in like_numbers:
#     A[x] = 1
