n = int(input())

U = 55555
is_prime = [1]*(U+1)
is_prime[0] = 0
is_prime[1] = 0
for p in range(2, int(U**.5)+1):
    if is_prime[p]:
        for q in range(2*p, U+1, p):
            is_prime[q] = 0
prime_list = [n for n, bl in enumerate(is_prime)if bl]
# print(len(prime_list))
A = []
for p, bl in enumerate(is_prime):
    if bl and p % 5 == 1:
        A.append(p)
# print(len(A))

print(*A[:n])
