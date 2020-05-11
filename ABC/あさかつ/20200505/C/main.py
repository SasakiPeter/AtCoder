n = int(input())
MOD = 30
A = [1, 2, 3, 4, 5, 6]

n %= MOD

for i in range(n):
    i %= 5
    A[i], A[i+1] = A[i+1], A[i]
print("".join(map(str, A)))
