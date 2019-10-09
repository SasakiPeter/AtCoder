# ABC063 B - Varied

# uncopyrightable
s = input()
print('yes' if len(s) == len(set(s)) else 'no')
print('no' if len(s) - len(set(s)) else 'yes')

print([True if i else False for i in range(-4, 5)])
