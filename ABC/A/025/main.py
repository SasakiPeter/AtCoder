s = input()
n = int(input())-1

# 5進数でnを表す
x, y = n//5, n % 5
# x, y = divmod(n, 5)
print(s[x]+s[y])
