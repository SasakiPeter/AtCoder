# a, _, _ = input()
# _, b, _ = input()
# _, _, c = input()
# print(a+b+c)

# こっちのが早い
*a, = [input()for _ in range(3)]
print(''.join(x[i] for i, x in enumerate(a)))
