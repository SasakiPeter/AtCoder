A, B, K, L = map(int, input().split())

# if a*l < b:
#     print(a*k)
# else:
n = K//L
print(B*n+min(B, A*(K-n*L)))
