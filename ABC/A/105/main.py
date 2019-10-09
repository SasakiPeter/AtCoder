n, k = map(int, input().split())
# print(1 if n % k else 0)

# True+0 -> 1 False+0 -> 0
# print((n % k > 0)+0)

# print(eval(input().replace(' ', '%')))


print(int(n % k != 0))
