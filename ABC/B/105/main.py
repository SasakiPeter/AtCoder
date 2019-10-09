# ~100
n = int(input())
ls = [4*i+7*j for i in range(n) for j in range(n)]
# O(n)
print('Yes' if n in ls else 'No')
