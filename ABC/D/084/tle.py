#!/usr/bin/env python3

# q = int(input())


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


# for _ in range(q):
#     ans = 0
#     L, R = map(int, input().split())
#     for x in range(L, R+1, 2):
#         if is_prime(x) and is_prime((x+1)//2):
#             ans += 1
#     print(ans)

q = int(input())


def is_prime(x):
    if x == 1:
        return False
    d = 2
    while d**2 <= x:
        if x % d == 0:
            return False
        d += 1
    else:
        return True


# prime = [0]*(10**5+1)
primes = []
for x in range(2, 10**5+1):
    if is_prime(x):
        # prime[x] = 1
        primes.append(x)

# print(primes)
# # 10**4個
# print(len(primes))


A = [0]*(10**5+1)
for prime in primes:
    if is_prime((prime+1)//2):
        A[prime] = 1

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

S = [0]*(10**5+1)
for i in range(1, 10**5+1):
    S[i] = S[i-1]+A[i]

# # print(S)

ans = []
for _ in range(q):
    L, R = map(int, input().split())
    cnt = S[R]-S[L-1]
    ans.append(cnt)

print(*ans, sep='\n')

# ls = []
# for _ in range(q):
#     L, R = map(int, input().split())
#     cnt = 0
#     for x in range((L+1)//2, (R+1)//2+1):
#         cnt += is_prime(x)+0
#     ls.append(cnt)
# print(ls)
