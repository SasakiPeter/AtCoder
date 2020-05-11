from itertools import accumulate
n, q = map(int, input().split())
A = [0]*(n+1)
for _ in range(q):
    L, R = map(int, input().split())
    L -= 1
    A[L] += 1
    A[R] -= 1
print("".join(map(lambda x: str(x % 2), accumulate(A[:-1]))))
